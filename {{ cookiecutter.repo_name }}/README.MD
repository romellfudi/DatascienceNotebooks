# TODO: please update badge link in config.yml and readme

# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## How to Use this repo
- By running the code using the Jupyter notebooks available in this repository's [notebooks](./notebooks) directory.
- By launching executable versions of these notebooks using binder: [![Binder](https://mybinder.org/badge.svg)](binder_link in config)
- By launching executable versions of these notebooks using Google Colab: [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](colab_link in config)
- By reading the online (non-executable) version of the notebooks using nbviewer: [![Nbviewer](https://raw.github.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg?sanitize=true)](nbviewer_link in config)

## About
See [Index.ipynb](nbviewer_link in config) for an index of the notebooks available to accompany the text.

## Software
The packages we used to run the code in these tutorials are listed in [environment.yml](environment.yml).

To create a stand-alone environment named `{{cookiecutter.project_name}}` with Python 3 and all the required package versions, run the following:

```bash
$ conda env create -n {{cookiecutter.project_name}} -f environment.yml
```

You can read more about using conda environments in the [Managing Environments](http://conda.pydata.org/docs/using/envs.html) section of the conda documentation.

---
Project based on the romainmartinez's [cookiecutter jupyter notebooks template](https://github.com/romainmartinez/cookiecutter-jupyter-notebooks).