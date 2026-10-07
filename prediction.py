import torch

from models.chest_model import create_model
from utils.preprocessing import preprocess_image


CLASS_NAMES = [
    "Cardiomegaly",
    "Pleural Effusion",
    "Lung Opacity"
]


def load_model():

    model.load_state_dict(
    torch.load("models/chest_model.pth")
)

    model.eval()

    return model


def predict(image, model):

    image_tensor = preprocess_image(image)

    with torch.no_grad():

        output = model(image_tensor)

        probabilities = torch.sigmoid(output)

    results = {}

    for i, name in enumerate(CLASS_NAMES):

        results[name] = float(probabilities[0][i])

    return results