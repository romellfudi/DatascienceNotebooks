# cookiecutter-jupyter-notebooks

Project structure for doing and sharing data science work.

Allows to automatically generate Jupyter content (repo info, navigation bar, index) from a configuration file (`config.yml`) and Jupyter notebooks (`notebooks/*.ipynb`).

Inspired by [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) and [PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook).

##  Project Organization

```
.
├── data
│   ├── processed            <- The final, canonical data sets for modeling
│   └── raw                  <- The original, immutable data dump
├── models                   <- Trained and serialized models, model predictions, or model summaries
├── notebooks                <- Jupyter notebooks
├── reports                  <- Generated analysis as HTML, PDF, LaTeX, etc
│   └── figures              <- Generated graphics and figures to be used in reporting
├── src                      <- Source code for use in this project
│   ├── data                 <- Scripts to download or generate data
│   │   ├── __init__.py
│   │   └── make_dataset.py
│   ├── features             <- Scripts to turn raw data into features for modeling
│   │   ├── build_features.py
│   │   └── __init__.py
│   ├── models               <- Scripts to train models
│   │   ├── __init__.py
│   │   ├── predict_model.py
│   │   └── train_model.py
│   ├── visualization        <- Scripts to create exploratory and results oriented visualizations
│   │   ├── __init__.py
│   │   └── visualize.py
│   └── __init__.py
├── config.yml
├── environment.yml          <- The requirements file for reproducing the analysis environment
├── LICENSE
├── Makefile                 <- Makefile with commands like `make create_env` or `make data`
├── README.md                <- The top-level README for developers using this project
└── setup.py                 <- makes project pip installable (pip install -e .) so src can be imported

```
