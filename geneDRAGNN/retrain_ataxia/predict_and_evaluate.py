import torch
import torch.nn.functional as F
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import pandas as pd
from train_gnn_model import GNNModel, input_dim, output_dim, node_index

# === Load Data ===
embedding = torch.load("data/ataxia/embedding.pt")
edges = pd.read_csv("edges.csv").replace(node_index)
edge_index = torch.tensor(edges.values.T, dtype=torch.long)

# Load labels
df = pd.read_csv("labels_final.csv")
genes = df["Gene"].tolist()
labels = df["Label"].tolist()
X_idx = [node_index[g] for g in genes if g in node_index]
y_true = [labels[i] for i, g in enumerate(genes) if g in node_index]

# === Load Trained Model ===
model = GNNModel(input_dim, 64, output_dim)
model.load_state_dict(torch.load("gnn_model_ataxia.pth"))
model.eval()

# === Predict ===
with torch.no_grad():
    logits = model(embedding, edge_index)[X_idx]
    probs = F.softmax(logits, dim=1)[:, 1].numpy()
    y_pred = (probs > 0.5).astype(int)

# === Save Scores ===
df_results = pd.DataFrame({
    "Gene": [genes[i] for i in range(len(genes)) if genes[i] in node_index],
    "True_Label": y_true,
    "Predicted_Label": y_pred,
    "Probability_Pathogenic": probs
})
df_results.to_csv("ataxia_gene_predictions.csv", index=False)

# === Save Evaluation Metrics ===
metrics = {
    "Accuracy": accuracy_score(y_true, y_pred),
    "Precision": precision_score(y_true, y_pred),
    "Recall": recall_score(y_true, y_pred),
    "F1_Score": f1_score(y_true, y_pred),
    "AUC": roc_auc_score(y_true, probs)
}
pd.DataFrame([metrics]).to_csv("ataxia_evaluation_metrics.csv", index=False)

print("✅ Prediction and evaluation results saved.")
