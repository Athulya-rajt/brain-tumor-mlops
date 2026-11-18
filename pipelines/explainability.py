import numpy as np
import cv2
import tensorflow as tf
import plotly.graph_objects as go

def generate_gradcam_heatmap(model, img_tensor, last_conv_layer_name=None):
    """
    Computes Grad-CAM heatmap highlighting where the CNN focused its classification nodes.
    """
    if last_conv_layer_name is None:
        for layer in reversed(model.layers):
            if len(layer.output_shape) == 4:
                last_conv_layer_name = layer.name
                break

    grad_model = tf.keras.models.Model(
        inputs=model.inputs,
        outputs=[model.get_layer(last_conv_layer_name).output, model.output]
    )

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_tensor)
        pred_index = tf.argmax(predictions[0])
        class_channel = predictions[:, pred_index]

    grads = tape.gradient(class_channel, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    conv_outputs = conv_outputs[0]
    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0) / (tf.math.reduce_max(heatmap) + 1e-8)
    return heatmap.numpy()

def overlay_gradcam(original_img, heatmap, alpha=0.45):
    """
    Overlays the Grad-CAM heatmap onto the original MRI slice.
    """
    if len(original_img.shape) == 2:
        original_img = cv2.cvtColor(original_img, cv2.COLOR_GRAY2RGB)
    h, w, _ = original_img.shape
    heatmap_resized = cv2.resize(heatmap, (w, h))
    heatmap_colored = cv2.applyColorMap(np.uint8(255 * heatmap_resized), cv2.COLORMAP_JET)
    heatmap_colored = cv2.cvtColor(heatmap_colored, cv2.COLOR_BGR2RGB)
    superimposed = cv2.addWeighted(original_img.astype(np.uint8), 1 - alpha, heatmap_colored, alpha, 0)
    return superimposed

def render_3d_brain_tumor(mri_slice, tumor_detected=True):
    """
    Generates an interactive, rotatable 3D surface & volumetric intensity map of the brain scan
    and highlights high-intensity tumor boundaries in 3D space.
    """
    if len(mri_slice.shape) == 3:
        gray = cv2.cvtColor(mri_slice, cv2.COLOR_RGB2GRAY)
    else:
        gray = mri_slice

    small = cv2.resize(gray, (80, 80)).astype(np.float32)
    x = np.linspace(-1, 1, 80)
    y = np.linspace(-1, 1, 80)
    X, Y = np.meshgrid(x, y)

    # Create a dome-like cranial depth profile modulated by MRI tissue intensity
    cranial_dome = np.sqrt(np.maximum(0, 1 - (X**2 + Y**2))) * 40.0
    Z = cranial_dome + (small / 255.0) * 25.0

    fig = go.Figure()

    # Brain tissue 3D surface
    fig.add_trace(go.Surface(
        z=Z, x=X, y=Y,
        colorscale="Viridis" if tumor_detected else "Greys",
        opacity=0.88,
        name="Cranial Tissue Matrix",
        showscale=False
    ))

    # Highlight anomaly peak region if tumor is detected
    if tumor_detected:
        threshold = np.percentile(small, 92)
        ty, tx = np.where(small >= threshold)
        fig.add_trace(go.Scatter3d(
            x=X[ty, tx],
            y=Y[ty, tx],
            z=Z[ty, tx] + 2.5,
            mode="markers",
            marker=dict(size=4, color="red", symbol="circle"),
            name="Detected Anomaly Cluster"
        ))

    fig.update_layout(
        title="Interactive 3D Intracranial Structural & Tumor Boundary Map",
        scene=dict(
            xaxis_title="Lateral (X)",
            yaxis_title="Anterior-Posterior (Y)",
            zaxis_title="Axial Elevation (Z)",
            bgcolor="rgb(15, 17, 26)"
        ),
        margin=dict(l=0, r=0, b=0, t=40),
        height=450
    )
    return fig