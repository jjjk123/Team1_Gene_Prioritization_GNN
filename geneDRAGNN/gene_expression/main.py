import json
import matplotlib.pyplot as plt
import pandas as pd


def get_top_genes_from_csv(file_path, top_n):
    """
    Reads the gene scores from a CSV file and returns the top N entries based on the Score column.

    :param file_path: Path to the CSV file.
    :param top_n: Number of top entries to retrieve.
    :return: DataFrame containing the top N entries.
    """
    df = pd.read_csv(file_path)
    return df.nlargest(top_n, 'Score')


def get_gene_data_from_json(file_path):
    """
    Reads gene data from a JSON file into a pandas DataFrame.

    :param file_path: Path to the JSON file.
    :return: DataFrame containing the JSON data.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return pd.DataFrame(data['data'])


def sort_json_data_by_median(df, reverse=True):
    """
    Sorts the DataFrame by the 'median' column.

    :param df: DataFrame to sort.
    :param reverse: If True, sorts in descending order.
    :return: Sorted DataFrame.
    """
    return df.sort_values(by='median', ascending=not reverse)


def filter_top_entries(df, top_n):
    """
    Filters the top N entries from the DataFrame.

    :param df: DataFrame to filter.
    :param top_n: Number of top entries to keep.
    :return: Filtered DataFrame.
    """
    return df.head(top_n)


def extract_gene_symbols(df):
    """
    Extracts gene symbols from the DataFrame.

    :param df: DataFrame containing gene data.
    :return: List of gene symbols.
    """
    return df['geneSymbol'].tolist()


def extract_medians(df):
    """
    Extracts median values from the DataFrame.

    :param df: DataFrame containing gene data.
    :return: List of median values.
    """
    return df['median'].tolist()


def generate_histogram(gene_symbols, medians):
    """
    Generates a histogram of median values for each gene.

    :param gene_symbols: List of gene symbols.
    :param medians: List of median values.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(gene_symbols, medians, color='skyblue')
    plt.xlabel('Gene')
    plt.ylabel('Median')
    plt.title('Histogram of Median TPM Values for each gene')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def generate_boxplot(gene_symbols, medians):
    """
    Generates a boxplot of median values for each gene.

    :param gene_symbols: List of gene symbols.
    :param medians: List of median values.
    """
    plt.figure(figsize=(12, 8))
    plt.boxplot([[median] for median in medians], vert=True, patch_artist=True, boxprops=dict(facecolor='skyblue'))
    plt.xticks(ticks=range(1, len(gene_symbols) + 1), labels=gene_symbols, rotation=90)
    plt.xlabel('Gene')
    plt.ylabel('Median')
    plt.title('Boxplot of Median TPM Values for Each Gene')
    plt.tight_layout()
    plt.show()


def group_data_by_gene_symbol(df):
    """
    Groups data by gene symbol.

    :param df: DataFrame containing gene data.
    :return: Dictionary with gene symbols as keys and lists of median values as values.
    """
    return df.groupby('geneSymbol')['median'].apply(list).to_dict()


def write_gene_symbols_to_file(gene_symbols, file_path):
    """
    Writes gene symbols to a file.

    :param gene_symbols: List of gene symbols.
    :param file_path: Path to the output file.
    """
    with open(file_path, 'w') as file:
        for gene_symbol in gene_symbols:
            file.write(f"Gene: {gene_symbol}\n")
            print(f"Gene: {gene_symbol}")


def calculate_linear_correlation(file_path):
    """
    Calculates the linear correlation between the Score and TPM median columns in a TSV file.

    :param file_path: Path to the TSV file.
    :return: Correlation coefficient.
    """
    df = pd.read_csv(file_path, sep='\t')
    return df['Score'].corr(df['TPM median'])


def main():
    # File paths
    csv_file_path = 'gene_scores.csv'
    json_file_path = 'gene_data.json'
    output_file_path = 'gene_symbols.txt'
    tsv_file_path = 'TPM_genescore.tsv'

    # Parameters
    top_n = 50

    # Get top genes from CSV
    top_genes_csv = get_top_genes_from_csv(csv_file_path, top_n)

    # Get gene symbols for top genes
    top_gene_symbols = top_genes_csv['symbol'].tolist()

    # Get gene data from JSON
    gene_data_df = get_gene_data_from_json(json_file_path)

    # Sort JSON data by median
    sorted_gene_data_df = sort_json_data_by_median(gene_data_df)

    # Filter top entries
    top_entries_df = filter_top_entries(sorted_gene_data_df, top_n)

    # Extract gene symbols and medians
    gene_symbols = extract_gene_symbols(top_entries_df)
    medians = extract_medians(top_entries_df)

    # Generate histogram and boxplot
    generate_histogram(gene_symbols, medians)
    generate_boxplot(gene_symbols, medians)

    # Write gene symbols to file
    write_gene_symbols_to_file(gene_symbols, output_file_path)

    # Calculate linear correlation
    correlation = calculate_linear_correlation(tsv_file_path)
    print(f"Linear correlation between Score and TPM median: {correlation}")


if __name__ == '__main__':
    main()
