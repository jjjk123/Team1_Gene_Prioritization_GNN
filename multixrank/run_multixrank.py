import multixrank

multixrank_obj = multixrank.Multixrank(config="ataxia/config.yml", wdir="ataxia")

ranking_df = multixrank_obj.random_walk_rank()

multixrank_obj.write_ranking(ranking_df, path="output_ataxia")
