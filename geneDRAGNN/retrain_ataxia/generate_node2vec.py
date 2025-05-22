import pandas as pd
import networkx as nx
from node2vec import Node2Vec
import torch

# === Load edges ===
df_edges = pd.read_csv("edges.csv")
G = nx.from_pandas_edgelist(df_edges, source="source", target="target", create_using=nx.Graph())

# === Run Node2Vec ===
node2vec = Node2Vec(G, dimensions=107, walk_length=10, num_walks=20, workers=2, seed=42)
model = node2vec.fit(window=5, min_count=1, batch_words=4)

# === Build tensor ===
node_list = list(G.nodes())
node_to_idx = {node: idx for idx, node in enumerate(node_list)}
embedding_tensor = torch.zeros((len(node_list), 107))
for node in node_list:
    embedding_tensor[node_to_idx[node]] = torch.tensor(model.wv[node])

# === Save ===
torch.save(embedding_tensor, "embedding.pt")  # For geneDRAGNN
pd.DataFrame(embedding_tensor.numpy(), index=node_list).to_csv("embedding.csv")  # Optional
