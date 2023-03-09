from dvc import api
import pandas as pd
from io import StringIO
import sys
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logger.info('Fetching data...')

movies_data_path = api.read('dataset/movies.csv', remote='dataset-track')
finantials_data_path = api.read('dataset/finantials.csv', remote='dataset-track')
opening_gross_data_path = api.read('dataset/opening_gross.csv', remote='dataset-track')

movies_data = pd.read_csv(StringIO(movies_data_path))
finantials_data = pd.read_csv(StringIO(finantials_data_path))
opening_gross_data = pd.read_csv(StringIO(opening_gross_data_path))

numeric_columns_mask = (movies_data.dtypes == float) | (movies_data.dtypes == int)
numeric_columns = [column for column in numeric_columns_mask.index if numeric_columns_mask[column]]

movies_data = movies_data[numeric_columns+['movie_title']]

fin_data = finantials_data[['movie_title', 'production_budget', 'worldwide_gross']]

fin_movies_data = pd.merge(fin_data, movies_data, on='movie_title', how='left')
full_movies_data = pd.merge(opening_gross_data, fin_movies_data, on='movie_title', how='left')

full_movies_data = full_movies_data.drop(['gross','movie_title'], axis=1)

full_movies_data.to_csv('dataset/full_data.csv',index=False)

logger.info('Data Fetched and prepared...')
