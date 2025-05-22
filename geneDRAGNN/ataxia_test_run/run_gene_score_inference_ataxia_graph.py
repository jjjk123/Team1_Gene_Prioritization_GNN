import torch
import pandas as pd
from torch_geometric.nn.models import MLP

# Load cleaned inputs
features = pd.read_csv('gene_features_ataxia_107.csv').values
gene_names = pd.read_csv('gene_names_ataxia.csv')['Gene'].tolist()

# Match LUAD-trained model architecture
model = MLP(
    in_channels=107,
    hidden_channels=128,
    out_channels=2,
    num_layers=3,
    dropout=0.0,
    norm='batch_norm',
    act='relu'
)

# Load pretrained checkpoint
checkpoint = torch.load('geneDRAGNN/models/model_checkpoints/MLP_node_trial99.ckpt',
                        map_location=torch.device('cpu'),
                        weights_only=False)

# Clean up state_dict keys
state_dict = checkpoint['state_dict']
cleaned_state_dict = {}
for k, v in state_dict.items():
    new_k = k.replace("model.", "")
    if "norms" in new_k and ".module" not in new_k:
        parts = new_k.split(".")
        new_k = f"{parts[0]}.{parts[1]}.module.{parts[2]}"
    cleaned_state_dict[new_k] = v

model.load_state_dict(cleaned_state_dict)

# Run inference
model.eval()
with torch.no_grad():
    inputs = torch.tensor(features, dtype=torch.float32)
    outputs = model(inputs)
    scores = outputs[:, 1].numpy()

# Save output
pd.DataFrame({
    "Gene": gene_names,
    "Score": scores
}).to_csv("gene_scores_ataxia.csv", index=False)

print("✅ gene_scores_ataxia.csv created successfully.")
