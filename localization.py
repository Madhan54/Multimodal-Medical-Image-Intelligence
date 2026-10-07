import torch
import numpy as np
import cv2

from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget
from pytorch_grad_cam.utils.image import show_cam_on_image


def generate_heatmap(model, image_tensor, image, class_index):

    target_layer = model.features[-1]

    cam = GradCAM(
        model=model,
        target_layers=[target_layer]
    )

    targets = [
        ClassifierOutputTarget(class_index)
    ]

    grayscale_cam = cam(
        input_tensor=image_tensor,
        targets=targets
    )[0]

    original = np.array(image.convert("RGB"))

    original = cv2.resize(
        original,
        (224, 224)
    )

    original = original.astype(np.float32) / 255.0

    visualization = show_cam_on_image(
        original,
        grayscale_cam,
        use_rgb=True
    )

    return visualization