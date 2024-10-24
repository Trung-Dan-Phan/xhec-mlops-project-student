<div align="center">

# xhec-mlops-project-student

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue.svg)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/artefactory/xhec-mlops-project-student/blob/main/.pre-commit-config.yaml)
</div>

This repository has for purpose to industrialize the [Abalone age prediction](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) Kaggle contest.



The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age.

**Goal**: predict the age of abalone (column "Rings") from physical measurements ("Shell weight", "Diameter", etc...)

## PR0 : Environment setup
### Environment Setup
To set up the Python environment for this project, please follow these steps:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Trung-Dan-Phan/xhec-mlops-project-student
   cd xhec-mlops-project-student
2. **Create a virtual environment with Conda**:
   ```bash
   conda env create -file environment.yml
3. **Activate the virtual environment**:
    ```bash
    conda activate xhec-mlops
4. **In order to stop using this virtual environment**:
    ```bash
    (xhec-mlops) $ deactivate
5. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
6. **Run pre-commit hooks**:
    ```bash
    pre-commit install



## Dataset Information

The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age.

**Goal**: predict the age of abalone (column "Rings") from physical measurements ("Shell weight", "Diameter", etc...)

The [Abalone dataset](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) contains the following features:

- **Sex**: Male, Female, or Infant (categorical)
- **Length**: Longest shell measurement (continuous)
- **Diameter**: Perpendicular to length (continuous)
- **Height**: With meat in the shell (continuous)
- **Whole weight**: Weight of the whole abalone (continuous)
- **Shucked weight**: Weight of meat (continuous)
- **Viscera weight**: Gut weight (continuous)
- **Shell weight**: After being dried (continuous)
- **Rings**: Age indicator (target variable)

### PR1 : EDA and Modelling on notebooks 

After setting up the environment, we explore the dataset and start modeling by opening the Jupyter notebooks in the `notebooks` directory. 

#### EDA Notebook (`eda.ipynb`)
   In this part, we created graphs for the distribution of the target variable and all the numeric features' distribution across *Sex*.  
  
   Besides, we provide a pairplot which helps in visually understanding how different variables relate to each other, and how those relationships vary based on *Sex*.


#### Modeling Notebook (`modelling.ipynb`)
   The dataset is divided in to train and test (8:2). We encode the *Sex*, use random forest regression and take rmse as the metric. We put forward the model initially and then use mlfow to track the model's performance across different *n_estimator*. We create an experiment to test different *n_estimator* value and then we log the parameter value, the metric, and register the model of the best performance on test set. Finally, we use MLflow UI (http://127.0.0.1:5000) to compare all the run under the experiment.

You can start Jupyter notebooks with:

```bash
jupyter notebook
```