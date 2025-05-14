
---

## 🧾 report_summary.txt (Sample content)

```txt
# Ataxia Gene Testing Summary – geneDRAGNN

Date: May 14, 2025


✅ Goal:
Test whether the LUAD-trained geneDRAGNN MLP model can score Ataxia-specific genes using real node2vec-based features.

✅ Inputs:
- Ataxia gene list from Genes_hereditary_ataxia.tsv
- PPI network: interactome_human.sif
- Features generated using pecanpy (SparseOTF, 128D)


✅ Adjustments:
- Feature matrix truncated to 107 dimensions to match the LUAD model
- All malformed lines and missing values were cleaned
- Final gene list aligned with model input expectations

✅ Output:
- `gene_scores_ataxia.csv` contains probability scores for each gene being functionally important (as per LUAD training)

📌 Note:
This is a technical test and not a disease-specific prediction. Retraining on Ataxia-specific data is required for valid inference.
