<table>
  <tr>
    <td><img src="https://github.com/SFGLab/Team1_Gene_Prioritization_GNN/blob/7859e3105290c2c5733b58ca13d16c30292abee2/raw.png" alt="Logo" width="150"/></td>
    <td>
      <p><em>BioAI Hackathon at the University of Warsaw (May 12–15, 2025)</em></p>
      <h1>GRAIL: Gene Ranking for Ataxia using Interactome-based Learning</h1>
    </td>
  </tr>
</table>





## Aim

The aim of the project is to compare the performance of Graph Neural Networks (GNNs) with network propagation methods in disease-gene prioritization. We aim to assess and compare how well these methods can prioritize candidate genes for further biological validation. As for the use case, we use genes involved in hereditary ataxia.

## Background

Medical genetics aims at diagnosing patients by finding genetic variants explaining their disease. While approximately half of the patients with rare genetic disease receive a genetic diagnosis, the other half remains undiagnosed, and one of the reasons is genetic variants in genes currently unknown to be disease-associated. Since experimental studies are usually quite expensive and time-consuming, in silico disease-gene prioritization is very useful in the discovery of new disease-genes. By ranking genes, the methods provide sets of the most promising new candidate genes relevant for a disease.

Currently, novel bioinformatics methods, such as graph neural networks are increasingly popular. The huge number of such methods requires further understanding of how they compare to previous methods and how useful they can be for further studies. In particular, it is of crucial importance for bioinformaticians to provide only high-confidence candidates for experimental validation. Therefore, during the hackathon we aimed at comparing the performance of graph neural networks with network propagation methods.

As an illustrative case we used hereditary ataxia - a rare, genetically complex disease, with many cases still unexplained despite years of investigations. Network-based methods can highlight functionally related genes that don't stand out in standard analyses. Compared to Network Propagation, GNNs may offer less bias and improved performance in recognizing complex patterns, but are dependent on advanced configuration and more computationally demanding. Our project explores the potential and limitations of these two types of models.


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

We used the following software packages: 
- https://github.com/geneDRAGNN/geneDRAGNN
- https://github.com/GiDeCarlo/XGDAG
- https://github.com/anthbapt/multixrank

Input:
- biological network (protein-protein interaction constructed with BioGRID and Reactome)
- a list of known disease genes for ataxia from https://www.genomicsengland.co.uk/
- node features: we used gene expression in cerebellum from the GTEx database (https://www.gtexportal.org) and case/control variants statistics from the AstraZeneca PheWAS Portal (https://azphewas.com/)

### Workflow

![Flowchart](https://github.com/SFGLab/Team1_Gene_Prioritization_GNN/blob/b790a73be0bdb8c3d208f48653adf3c490986681/GNN%20for%20GD%20proiritization.drawio%20(7).png)


### How to use this repository?

Use it to expand the benchmarking of network-based methods for identifying disease-associated genes, or to obtain a functional XGDAG environment and geneDRAGNN setup.  

#### geneDRAGNN Pipeline testing

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

### XGDAG

We were not able to utilize the XGDAG GNN due to challenges in reproducing a functional environment for this tool, across systems from a Windows laptop to a Linux HPC. The provided Conda setups were not functional and we could not resolve all dependencies. We requested the authores provide a containerized, platform-independent solution, however, due to the time limitations of the hackathon, we created a compatible Docker image from scratch. This way we were able to run the tool on the included, default data. This allowed us to realize several input files for XGDAG must be prepared with another tool, with limited documentation of the process. The tool set up unfortunately left us with not enough time to process and analyze our own data.

### geneDRAGNN
The list of the top 20 prioritized genes for Ataxia using the geneDRAGNN tool that was trained on LUAD 

![image](https://github.com/user-attachments/assets/fc1c939c-bbe4-4e32-be99-c4d8fd3ec6c5)

### MultiXrank (Random Walk with Restart)

All scripts to run MultiXrank for ataxia genes are in [multixrank/](multixrank/)


## Conclusions


## Future directions
1. Retrain XGDAG and geneDRAGNN using disease-specific input data
2. GNN vs network propagation: leave-one-out cross-validation, compare the top 20 highest scoring genes (the most promising candidates for ataxia)
3. Use XAI strategies to compute explanation subgraphs
4. Construct multi-layer networks for GNN imputation
5. Improve the usability of GNNs for non-CS researchers
6. Perform external validation of candidate genes using the internal database of 30K+ of exomes and genomes of rare disease patients at [IMGAG Tübingen](https://www.medizin.uni-tuebingen.de/de/das-klinikum/einrichtungen/institute/medizinische-genetik-und-angewandte-genomik).


## References

1) Altabaa, A., Huang, D., Byles-Ho, C., Khatib, H., Sosa, F., & Hu, T. (2022). GeneDRAGNN: Gene disease prioritization using graph neural networks. 2022 IEEE Conference on Computational Intelligence in Bioinformatics and Computational Biology (CIBCB), 1–10. https://doi.org/10.1109/cibcb55180.2022.9863043
2) Ata, S. K., Wu, M., Fang, Y., Ou-Yang, L., Kwoh, C. K., & Li, X.-L. (2021). Recent advances in network-based methods for disease gene prediction. Briefings in Bioinformatics, 22(4). https://doi.org/10.1093/bib/bbaa303
3) Bekker, J., & Davis, J. (2020). Learning from positive and unlabeled data: a survey. Machine Learning, 109(4), 719–760. https://doi.org/10.1007/s10994-020-05877-5
4) Laman Trip, D. S., van Oostrum, M., Memon, D., Frommelt, F., Baptista, D., Panneerselvam, K., Bradley, G., Licata, L., Hermjakob, H., Orchard, S., Trynka, G., McDonagh, E. M., Fossati, A., Aebersold, R., Gstaiger, M., Wollscheid, B., & Beltrao, P. (2025). A tissue-specific atlas of protein-protein associations enables prioritization of candidate disease genes. Nature Biotechnology. https://doi.org/10.1038/s41587-025-02659-z
5) Mastropietro, A., De Carlo, G., & Anagnostopoulos, A. (2023). XGDAG: explainable gene-disease associations via graph neural networks. Bioinformatics (Oxford, England), 39(8). https://doi.org/10.1093/bioinformatics/btad482
6) Shi, Y., Huang, Z., Wang, W., Zhong, H., Feng, S., & Sun, Y. (2020). Masked label prediction: Unified message passing model for semi-supervised classification. In arXiv [cs.LG]. arXiv. http://arxiv.org/abs/2009.03509
