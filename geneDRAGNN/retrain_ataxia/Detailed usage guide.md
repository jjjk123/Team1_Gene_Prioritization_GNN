# ✅ How to Use the Model
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt

### Load the model:

python
Copy
Edit
import torch
from train_gnn_model import GNNModel  # Or define the class manually

### Reconstruct model architecture
model = GNNModel(input_dim=107, hidden_dim=64, output_dim=2)
model.load_state_dict(torch.load("gnn_model_ataxia.pth"))
model.eval()

### Prepare inputs:

python
Copy
Edit

### Load embeddings and edge list
import pandas as pd
embedding = torch.load("data/ataxia/embedding.pt")

### Map edges to integer indices
edges = pd.read_csv("edges.csv")
nodes = pd.read_csv("nodes.csv")['id'].tolist()
node_index = {node: i for i, node in enumerate(nodes)}
edge_index = torch.tensor(edges.replace(node_index).values.T, dtype=torch.long)

### Run inference:

python
Copy
Edit
with torch.no_grad():
    logits = model(embedding, edge_index)
    probs = torch.softmax(logits, dim=1)[:, 1]  # Probability of class 1

📊 Predict on New Genes
You can modify predict_and_evaluate.py to load your own gene list and get predictions, using the model and embeddings provided.

📁 Included Files

![image](https://github.com/user-attachments/assets/71f8fa5c-5e6b-4ff3-b3f9-d128e0c76ea0)

