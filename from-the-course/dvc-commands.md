# dvc commands

``` 
# inicia repo
dvc init

# agregar remote tracker 
dvc remote add [nombre-tracker] [url-bucket]

dvc remote add dataset-track gs://intro-ml-deploy.appspot.com/dataset

# agregar file a remote tracker
dvc add [file] --to-remote -r [nombre-tracker]

dvc add dataset/movies.csv --to-remote -r dataset-track

# agregar pipeline
dvc run -n [nombre-step] -o [artefacto-final] python [codigo-python-principal]

dvc run -n prepare-data -o dataset/full_data.csv python src/prepare.py

dvc run -n training -d dataset/full_data.csv python src/train.py

# ejecuta todo el pipeline completo
dvc repro

# muestra un grafico del pipeline completo
dvc dag
```