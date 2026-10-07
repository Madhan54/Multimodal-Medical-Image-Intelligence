import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models

# Preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Dataset
train_data = datasets.ImageFolder(
    "data/train",
    transform=transform
)

train_loader = DataLoader(
    train_data,
    batch_size=16,
    shuffle=True
)

# Model
model = models.densenet121(
    weights=models.DenseNet121_Weights.DEFAULT
)

# Change final layer
model.classifier = nn.Linear(
    model.classifier.in_features,
    3
)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.0001
)

# Training
for epoch in range(5):

    model.train()
    total_loss = 0

    for images, labels in train_loader:

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(
        "Epoch:",
        epoch + 1,
        "Loss:",
        total_loss
    )

# Save model
torch.save(
    model.state_dict(),
    "models/chest_model.pth"
)

print("Model training completed!")