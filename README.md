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

## PR1 : EDA and Modelling on notebooks 

After setting up the environment, you can explore the dataset and start modeling by opening the Jupyter notebooks in the `notebooks` directory. 

#### EDA Notebook (`eda.ipynb`)
   In this part, we created graphs for the distribution of the target variable and all the numeric features' distribution across *Sex*.  
  
   Besides, we provide a pairplot which helps in visually understanding how different variables relate to each other, and how those relationships vary based on *Sex*.


#### Modeling Notebook (`modelling.ipynb`)
   We encode the *Sex*, use random forest regression and take rmse as the metric. We put forward the model initially and then use mlfow to track the model's performance across different *n_estimator*. We create an experiment to test different *n_estimator* value and then we log the parameter value, the performance metric, and register the model for each run. Finally, we use MLflow UI to compare all the run under the experiment.

You can start Jupyter notebooks with:

```bash
jupyter notebook
```

## PR2 : From notebooks to modules 

### Objectives:

- Adapt the training code from the notebooks to Python scripts for modularization.
- Prepare the model deployment using **pickle** for serialization.
- Set up a Continuous Integration (CI) pipeline to enforce code formatting and linting.

### Steps:

#### 1. Modifying the `src/modelling` Folder
We have refactored the code from the Jupyter notebooks and moved it into Python scripts in the `src/modelling` folder. This includes data preprocessing, model training, and evaluation. All the logic previously present in the notebooks is now organized into functions and modules to improve maintainability and scalability.

#### 2. Model Deployment with Pickle
To prepare for deployment, the trained model is serialized using the **pickle** library, allowing it to be saved and loaded later in different environments.

#### 3. Continuous Integration (CI) Setup
A CI pipeline has been set up to automatically check code quality before merging any changes. The pipeline runs the following tools:

- **Black**: for code formatting.
- **Flake8** and **Ruff**: for linting and checking for any coding style violations.
- **Pre-commit**: for enforcing these checks before committing changes to the repository.

To install and set up pre-commit hooks:

```bash
pre-commit install
```
### Running the Part 2:
After setting up the environment and installing the dependencies, you can run the training script as follows:

From the root of the repository, run the `main.py` script using the command:

```bash
python src/modelling/main.py data/abalone.csv
```

## PR3 : From notebooks to modules 

### 1. Start the Prefect UI

To monitor the workflow execution in real-time and view the tasks, start the Prefect Orion UI:

```bash
prefect server start
```
This will launch the Prefect UI at localhost:4200, where you can visualize the flow, inspect task executions, and manage the system.

### 2. Scheduling the Model Retraining

The deployment setup includes a scheduling mechanism for regular model retraining. To start and manage scheduled runs, use the Prefect UI or define schedules directly in the Prefect flows. For example, you can set up a daily schedule to retrain the model with new data. The UI allows you to trigger, pause, or monitor scheduled runs.

## PR4: FastAPI Deployment

### 1. Run the FastAPI Application

```bash
uvicorn src.web_service.main:app --host 0.0.0.0 --port 8001 --reload
```
Access the API at http://localhost:8001/docs to view the interactive API documentation.

### 2. Docker Deployment

Build the Docker image :

```bash
docker build -t mlops-project -f Dockerfile.app .
```

Run the Docker container : 

```bash
docker run -p 0.0.0.0:8000:8001 -p 0.0.0.0:4200:4201 mlops-project
```
Access the API :

Once the container is running, you can access the FastAPI application at http://localhost:8001/docs