<table>
  <tr>
    <td><img src="https://github.com/SFGLab/Team1_Gene_Prioritization_GNN/blob/7859e3105290c2c5733b58ca13d16c30292abee2/raw.png" alt="Logo" width="150"/></td>
    <td>
      <p><em>BioAI Hackathon at the University of Warsaw (May 12–15, 2025)</em></p>
      <h1>D-GRIP: Disease-Gene Ranking via Inference and Propagation</h1>
      <h1>GRAIL: Gene Ranking for Ataxia using Interactome-based Learning</h1>
    </td>
  </tr>
</table>





## Aim

To identify new genes potentially involved in Hereditary Ataxia by applying graph-based machine learning methods to biological networks. We compare Network Propagation with state-of-the-art Graph Neural Networks (GNNs), using protein-protein interaction data and known disease genes. We aim to assess and compare how well these methods can prioritize candidate genes for further biological validation.

## Why?

Hereditary Ataxia is a rare, genetically complex disease, with many cases still unexplained despite genome-wide studies. Network-based methods can highlight functionally related genes that don't stand out in standard analyses. Compared to Network Propagation, GNNs may offer less bias and improved performance in recognizing complex patterns, but are dependent on advanced configuration and more computationally demanding. Our project explores the potential and limitations of these two types of models.

## Contributors

- Jędrzej Kubica
- German Demidov
- Anna Simonyan
- Abolhassan Bahari
- Rahaf Ahmad
- Sreeram Peela
- Mikolaj Kocikowski
- Paulina Domek

## Methods

Main tools to base our work on: https://github.com/geneDRAGNN/geneDRAGNN and https://github.com/GiDeCarlo/XGDAG 

Case/control variants statistics: https://azphewas.com/phenotypeView/6319c068-fd59-46d8-85ee-82d82482eb14/VW5pb24jRzExI0hlcmVkaXRhcnkgYXRheGlh/glr

### Workflow

![Flowchart](https://github.com/SFGLab/Team1_Gene_Prioritization_GNN/blob/main/GNN%20for%20GD%20proiritization.drawio%20(4).png?raw=true)

### Pipeline testing 
README


geneDRAGNN testing pipeline

This project demonstrates how to use the pretrained model from the geneDRAGNN repository to generate disease relevance scores for genes using a Multi-Layer Perceptron (MLP) model trained on lung adenocarcinoma (LUAD) data.

🔍 What This Does
- Loads a pretrained MLP model: MLP_node_trial99.ckpt
- Accepts node features of shape (N, 107)
- Outputs predicted gene scores in gene_scores.csv

🧪 Setup

1. Clone the Repo
git clone https://github.com/hanikhatib/geneDRAGNN.git
cd geneDRAGNN

2. Install Requirements (CPU)
pip install torch torchvision torchaudio pandas numpy
pip install torch-scatter -f https://data.pyg.org/whl/torch-2.1.0+cpu.html
pip install torch-sparse -f https://data.pyg.org/whl/torch-2.1.0+cpu.html
pip install torch-geometric

3. Prepare Input Files
Place gene_features_107.csv and gene_names.csv in the repo folder.

4. Run Inference
python3 run_gene_score_inference_final_v2.py

✅ Output:
gene_scores.csv with pathogenicity relevance scores.

⚠️ Notes
- The pretrained model is trained for Lung Adenocarcinoma (LUAD).
- Using this model for other diseases will require retraining.


## Results

## Conclusions

## How to use this repo

Why clone it? How to use it? Why and how build upon it?

Draft: to apply the methods we validated as working, to research further rare diseases in a similar fashion. To expand this project into a more comprehensive benchmarking of available methods.

## References

1) Altabaa, A., Huang, D., Byles-Ho, C., Khatib, H., Sosa, F., & Hu, T. (2022). GeneDRAGNN: Gene disease prioritization using graph neural networks. 2022 IEEE Conference on Computational Intelligence in Bioinformatics and Computational Biology (CIBCB), 1–10. https://doi.org/10.1109/cibcb55180.2022.9863043
2) Ata, S. K., Wu, M., Fang, Y., Ou-Yang, L., Kwoh, C. K., & Li, X.-L. (2021). Recent advances in network-based methods for disease gene prediction. Briefings in Bioinformatics, 22(4). https://doi.org/10.1093/bib/bbaa303
3) Bekker, J., & Davis, J. (2020). Learning from positive and unlabeled data: a survey. Machine Learning, 109(4), 719–760. https://doi.org/10.1007/s10994-020-05877-5
4) Laman Trip, D. S., van Oostrum, M., Memon, D., Frommelt, F., Baptista, D., Panneerselvam, K., Bradley, G., Licata, L., Hermjakob, H., Orchard, S., Trynka, G., McDonagh, E. M., Fossati, A., Aebersold, R., Gstaiger, M., Wollscheid, B., & Beltrao, P. (2025). A tissue-specific atlas of protein-protein associations enables prioritization of candidate disease genes. Nature Biotechnology. https://doi.org/10.1038/s41587-025-02659-z
5) Mastropietro, A., De Carlo, G., & Anagnostopoulos, A. (2023). XGDAG: explainable gene-disease associations via graph neural networks. Bioinformatics (Oxford, England), 39(8). https://doi.org/10.1093/bioinformatics/btad482
6) Shi, Y., Huang, Z., Wang, W., Zhong, H., Feng, S., & Sun, Y. (2020). Masked label prediction: Unified message passing model for semi-supervised classification. In arXiv [cs.LG]. arXiv. http://arxiv.org/abs/2009.03509
