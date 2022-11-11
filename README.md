# Proyecto Todo List

**TEC Monterrey - Machine Learning - Entregable Modulo 2 [Alex Castro Gumiel]**

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>



## Project Target 

- Organizar el código o los scripts en una estructura de directorio [ok]
- Cree los archivos necesarios de empaquetado [dev]
- Cuide las referencias (imports) intra-paquete [ok]
- Verifique que el código siga el PEP 8 [ok]
- Agregue Python annotations a sus funciones [ok]
- Verifique que sus funciones tengan docstrings [ok]
- Agregue pruebas unitarias y de integración que crea convenientes [ok]
- Hacer ejecutable el módulo y probarlo en un venv
- Cree un repositorio en su cuenta de GitHub y suba el proyecto [ok]

## Project Structuring

cookiecutter https://github.com/drivendata/cookiecutter-data-science

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Package References

   ├── src
   │   ├── main_todo.py                 <- Main: Client Methods
   │   │   ├── packages                 <- Packages Folder
   │   │   │   ├── class_todo.py        <- Class: Methods Refactored

## PEP 8 Style Guide

- black src/main_todo.py 
- black src/packages/class_todo.py 

- flake8 src/main_todo.py
- flake8 src/packages/class_todo.py 

- isort src/main_todo.py 
- isort src/packages/class_todo.py 

## Annotations 

src/main_todo.py 
src/packages/class_todo.py 

## Docstrings

<!-- pip install git+https://github.com/dadadel/pyment.git -->
pyment -w src/packages/class_todo.py

interrogate -vv src/packages/class_todo.py

pycodestyle --first src/packages/class_todo.py
pycodestyle --show-source --show-pep8 src/packages/class_todo.py
pycodestyle src/packages/class_todo.py --format=pylint

pylint src/packages/class_todo.py

## Unit & Integration Tests

pytest tests/unit/test_unit.py -v
pytest tests/integration/test_integration.py -v

## Create Packaging Files

[pip install poetry]
poetry new <project-name>
[poetry env use <path env>]
poetry install
poetry add <library-name>
poetry remove <library-name>
poetry show
poetry show --tree

## GitHub Repository

https://github.com/Lucky-IA/TEC-Mod2-Todos

git init
git add .
git commit -m "first commit"

git remote add origin https://github.com/Lucky-IA/TEC-Mod2-Todos.git
git branch -M main
git push -u origin main

git status
git add .
git commit -m "update readme"
git push

