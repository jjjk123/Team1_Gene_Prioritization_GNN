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

The aim of the project was to compare the performance of Graph Neural Networks (GNNs) with network propagation methods for disease-gene prioritization. We aimed at assessing and comparing how well these two strategies can prioritize candidate disease genes for further biological validation. As for the use case, we used genes involved in hereditary ataxia.


## Background

Medical genetics aims at diagnosing patients by finding genetic variants explaining their disease. While approximately half of the patients with rare genetic disease receive a genetic diagnosis, the other half remains undiagnosed. The reason is that some genomic variants are currently unknown to be disease-associated. Since experimental studies are usually quite expensive and time-consuming, in silico disease-gene prioritization is very useful in the discovery of new disease-genes. By ranking genes, the methods provide sets of the most promising new candidate genes relevant for a disease. Currently, novel bioinformatics methods, such as graph neural networks are increasingly popular. The huge number of such methods requires further understanding of how they compare to previous methods. In particular, it is of crucial importance for bioinformaticians to provide only high-confidence candidates for experimental validation. Therefore, during the hackathon we aimed at comparing the performance of graph neural networks with network propagation methods. Compared to network propagation, GNNs are expected to offer improved performance in recognizing complex network patterns, but are dependent on advanced configuration and limited by high  computational requirements. Our project explores the potential and limitations of these two types of models.


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

In this study, we used the following software packages: 
- https://github.com/geneDRAGNN/geneDRAGNN
- https://github.com/GiDeCarlo/XGDAG
- https://github.com/anthbapt/multixrank

We used the following input data:
- a biological network (protein-protein interactions from BioGRID and Reactome)
- a list of known disease genes for ataxia (from https://www.genomicsengland.co.uk/)
- as node features, we used gene expression (from the GTEx database, https://www.gtexportal.org; "cerebellum") and case/control variants statistics (from the AstraZeneca PheWAS Portal, https://azphewas.com/)


### Workflow

![Flowchart](https://github.com/SFGLab/Team1_Gene_Prioritization_GNN/blob/b790a73be0bdb8c3d208f48653adf3c490986681/GNN%20for%20GD%20proiritization.drawio%20(7).png)


### How to use this repository?

Everyone is welcome to clone this repository and build upon the project, for example, to expand the benchmarking of network-based methods for identifying disease-associated genes, or to obtain a functional XGDAG and geneDRAGNN setup.  

### Software:

#### 1. geneDRAGNN

We demonstrate below how to use the pretrained model from the geneDRAGNN repository to generate disease-gene scores using a Multi-Layer Perceptron (MLP) model trained on lung adenocarcinoma (LUAD) data.

🔍 What This Does
- loads a pretrained MLP model: MLP_node_trial99.ckpt
- accepts node features of shape (N, 107)
- outputs predicted gene scores in gene_scores.csv

🚀 How to Run

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
gene_scores.csv with pathogenicity relevance scores

⚠️ Notes
- The pretrained model is trained for Lung Adenocarcinoma (LUAD).
- Using this model for other diseases will require retraining.


##### geneDRAGNN – Ataxia Variant Prediction

This repository applies the geneDRAGNN graph neural network to predict gene associations with Hereditary Ataxia.

🚀 How to Run

Our scripts to retrain geneDRAGNN are in [geneDRAGNN/retrain_ataxia/]([geneDRAGNN/retrain_ataxia/]).

🧪 Model

GNN architecture: SGConv

Input features: 107D Node2Vec embeddings

Output: Binary classification (pathogenic / non-pathogenic)


#### 2. XGDAG

We were not able to utilize the XGDAG GNN due to challenges in reproducing a functional environment for this software. The provided Conda environments were not functional and we could not resolve all dependencies. We requested the authores provide a containerized, platform-independent solution, however, due to the time limitations of the hackathon, we created a compatible Docker image from scratch. This way we were able to run the tool on the included, default data. This allowed us to realize several input files for XGDAG must be prepared with another tool, with limited documentation of the process. The tool set up unfortunately left us with not enough time to process and analyze our own data.


#### 3. MultiXrank

As a network propagation method, we used Random Walk with Restart, as implemented in MultiXrank (https://github.com/anthbapt/multixrank).

🔍 What This Does
- Loads a biological network (interactome_human.tsv) and known disease genes (seeds.txt)
- Outputs gene scores (multixrank_output_ataxia.tsv)

🚀 How to Run

Our scripts to run MultiXrank for ataxia are in [multixrank/](multixrank/).

🧪 Setup

1. Clone the Repo
git clone https://github.com/anthbapt/multixrank
cd multixrank

2. Install Requirements (CPU)
pip install multixrank

4. Prepare Input Files
Place interactome_human.tsv (format: ENSG1\tENSG2) and seeds.txt (ENSG per row) in the ataxia/ folder.

5. Run MultiXrank as described in https://github.com/anthbapt/multixrank

✅ Output:
multixrank_output_ataxia.tsv with gene scores

⚠️ Notes
- We used the default MultiXrank parameters (r = 0.7, self-loops = 1).


## Results

### geneDRAGNN

The list of the top 20 prioritized genes for ataxia using geneDRAGNN that was trained on LUAD (default model):

![image](https://github.com/user-attachments/assets/fc1c939c-bbe4-4e32-be99-c4d8fd3ec6c5)


The list of the top 20 genes for ataxia using the retrained geneDRAGNN:

![image](https://github.com/user-attachments/assets/911e5d61-987d-4831-80b9-a69718437a43)


### Method Comparison

Comparison of the top 20 genes from geneDRAGNN, retrained geneDRAGNN and MultiXrank:

![image](https://github.com/user-attachments/assets/e5e571f2-5b8c-46ae-8ff1-0e6aecd26e4e)


## Conclusions

During the hackathon, we conducted the project entitled "GRAIL: Gene Ranking for Ataxia using Interactome-based Learning" to compare the performance of two promising strategies for disease gene prioritization: graph neural networks and network propagation methods. Despite challenges with usability and limited time, we ran geneDRAGNN (a graph neural network) and MultiXrank (a network propagation method). We used an example dataset consisting of a protein-protein interaction network and known gene for hereditary ataxia. Our results show that both methods produce distinct sets of top-ranked genes, which suggests that they might provide complementary results. The retraining of geneDRAGNN using disease-specific features might improve its performance. To conclude, a combined strategy that leverages the interpretability and scalability of network propagation with the expressive power of GNNs may yield the best results for the identification of new disease-associated genes. 


## Future directions

1. Retrain XGDAG and geneDRAGNN using disease-specific input data.
2. Benchmark XGDAG, geneDRAGNN and MultiXrank: leave-one-out cross-validation, compare the annotations of the top 20 highest scoring genes
3. Use explainable AI strategies to compute explanation subgraphs and interpret the scoring
4. Compare the performance of GNN vs network propagation on multi-layer networks (e.g., protein-protein interactions, gene co-expression, gene regulatory networks)
5. Improve the usability of GNNs researchers
6. Perform a validation of candidate genes using the internal database of 30K+ of exomes and genomes of rare disease patients at [IMGAG Tübingen](https://www.medizin.uni-tuebingen.de/de/das-klinikum/einrichtungen/institute/medizinische-genetik-und-angewandte-genomik).


## References

1) Altabaa, A., Huang, D., Byles-Ho, C., Khatib, H., Sosa, F., & Hu, T. (2022). GeneDRAGNN: Gene disease prioritization using graph neural networks. 2022 IEEE Conference on Computational Intelligence in Bioinformatics and Computational Biology (CIBCB), 1–10. https://doi.org/10.1109/cibcb55180.2022.9863043
2) Ata, S. K., Wu, M., Fang, Y., Ou-Yang, L., Kwoh, C. K., & Li, X.-L. (2021). Recent advances in network-based methods for disease gene prediction. Briefings in Bioinformatics, 22(4). https://doi.org/10.1093/bib/bbaa303
3) Bekker, J., & Davis, J. (2020). Learning from positive and unlabeled data: a survey. Machine Learning, 109(4), 719–760. https://doi.org/10.1007/s10994-020-05877-5
4) Laman Trip, D. S., van Oostrum, M., Memon, D., Frommelt, F., Baptista, D., Panneerselvam, K., Bradley, G., Licata, L., Hermjakob, H., Orchard, S., Trynka, G., McDonagh, E. M., Fossati, A., Aebersold, R., Gstaiger, M., Wollscheid, B., & Beltrao, P. (2025). A tissue-specific atlas of protein-protein associations enables prioritization of candidate disease genes. Nature Biotechnology. https://doi.org/10.1038/s41587-025-02659-z
5) Mastropietro, A., De Carlo, G., & Anagnostopoulos, A. (2023). XGDAG: explainable gene-disease associations via graph neural networks. Bioinformatics (Oxford, England), 39(8). https://doi.org/10.1093/bioinformatics/btad482
6) Shi, Y., Huang, Z., Wang, W., Zhong, H., Feng, S., & Sun, Y. (2020). Masked label prediction: Unified message passing model for semi-supervised classification. In arXiv [cs.LG]. arXiv. http://arxiv.org/abs/2009.03509
