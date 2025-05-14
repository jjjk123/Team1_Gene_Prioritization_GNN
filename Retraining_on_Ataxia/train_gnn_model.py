import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch_geometric.data import Data
from torch_geometric.nn import SGConv
import json
import os
import pandas as pd

# ===== Configuration =====
data_dir = "data/ataxia"
embedding_path = os.path.join(data_dir, "embedding.pt")
train_path = os.path.join(data_dir, "train.json")
valid_path = os.path.join(data_dir, "valid.json")

input_dim = 107
hidden_dim = 64
output_dim = 2
lr = 0.001
epochs = 100
batch_size = 16

# ===== Model Definition =====
class GNNModel(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(GNNModel, self).__init__()
        self.conv1 = SGConv(input_dim, hidden_dim)
        self.conv2 = SGConv(hidden_dim, output_dim)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return x

# ===== Load Data =====
def load_json(path):
    with open(path) as f:
        return json.load(f)

train_data = load_json(train_path)
valid_data = load_json(valid_path)

# Load embeddings
embeddings = torch.load(embedding_path)
node_list = pd.read_csv("nodes.csv")['id'].tolist()
node_index = {node: i for i, node in enumerate(node_list)}

# Convert gene-disease pairs to tensors
def build_dataset(data):
    X = []
    y = []
    for entry in data:
        gene = entry["gene"]
        if gene in node_index:
            X.append(node_index[gene])
            y.append(entry["label"])
    return torch.tensor(X), torch.tensor(y)

X_train_idx, y_train = build_dataset(train_data)
X_valid_idx, y_valid = build_dataset(valid_data)

# Create graph edge index
edges = pd.read_csv("edges.csv")

# Map gene symbols to node indices
edges_mapped = edges.replace(node_index)
edge_index = torch.tensor(edges_mapped.values.T, dtype=torch.long)


# ===== Training Setup =====
model = GNNModel(input_dim, hidden_dim, output_dim)
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

# ===== Training Loop =====
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    out = model(embeddings, edge_index)
    loss = F.cross_entropy(out[X_train_idx], y_train)
    loss.backward()
    optimizer.step()

    model.eval()
    with torch.no_grad():
        val_out = model(embeddings, edge_index)
        val_pred = val_out[X_valid_idx].argmax(dim=1)
        val_acc = (val_pred == y_valid).float().mean().item()
    print(f"Epoch {epoch+1:03d}, Loss: {loss.item():.4f}, Val Acc: {val_acc:.4f}")
torch.save(model.state_dict(), "gnn_model_ataxia.pth")
print("✅ Model saved to gnn_model_ataxia.pth")
