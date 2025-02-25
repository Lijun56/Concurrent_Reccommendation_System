from posixpath import join
import os.path as join
import pandas as pd
from recall.config import config
from functools import lru_cache

@lru_cache() # Cache the result of the function, so that it is not executed every time it is called
def load_dataset():
    anime_df = pd.read_csv(join(config['dataset_path'], '/anime.csv', index_col='anime_id'))
    rating_df = pd.read_csv(join(config['dataset_path'], '/rating.csv'))

    return (anime_df, rating_df)