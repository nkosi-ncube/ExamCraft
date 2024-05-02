import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.softmax(out)
        return out

# Example data for training (dummy data)
X_train = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y_train = torch.tensor([[1, 0], [0, 1], [0, 1], [1, 0]], dtype=torch.float32)

# Hyperparameters
input_size = 2
hidden_size = 5
output_size = 2
learning_rate = 0.001
num_epochs = 1000

# Initialize model, loss function, and optimizer
model = SimpleNN(input_size, hidden_size, output_size)
criterion = nn.BCELoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# Training the model
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(X_train)
    loss = criterion(outputs, y_train)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Print progress
    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Example usage: Generate study materials based on input text
input_text = "Key concepts extracted from exam paper analysis."
# Convert input text to tensor
input_tensor = torch.tensor(np.array(input_text.split(), dtype=np.float32))
# Forward pass through the model
output = model(input_tensor)
# Print the output probabilities (example)
print("Output probabilities:", output)
