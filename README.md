<div align="center">

# xhec-mlops-project-student

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue.svg)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/artefactory/xhec-mlops-project-student/blob/main/.pre-commit-config.yaml)
</div>

This repository has for purpose to industrialize the [Abalone age prediction](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) Kaggle contest.

<details>
<summary>Details on the Abalone Dataset</summary>

The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age.

**Goal**: predict the age of abalone (column "Rings") from physical measurements ("Shell weight", "Diameter", etc...)

You can download the dataset on the [Kaggle page](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset)

</details>
Certainly! Here's an updated version of the README file with a **Table of Contents** section to help users navigate the document easily.

---

## Table of Contents
- [xhec-mlops-project-student](#xhec-mlops-project-student)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Objectives](#objectives)
  - [Project Structure](#project-structure)
  - [Setup Instructions](#setup-instructions)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Set up the Environment](#2-set-up-the-environment)
      - [Using Conda (Recommended)](#using-conda-recommended)
      - [Using pip](#using-pip)
    - [3. Run the Notebooks](#3-run-the-notebooks)
  - [Dataset Information](#dataset-information)
  - [CI/CD Pipeline](#cicd-pipeline)

---

## Project Overview

This project aims to explore the [Abalone dataset](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) and build a machine learning model to **predict the age (number of rings)** of an abalone. The dataset provides various features such as length, diameter, and height, which can help in predicting the age of abalones.

The project follows **MLOps principles** for continuous integration, code quality, and reproducibility.

## Objectives

1. **Exploratory Data Analysis (EDA):**
   - Perform a detailed exploration of the Abalone dataset to understand the distribution of features, correlations, and trends.
   
2. **Modeling:**
   - Build an initial machine learning model to predict the number of rings (which corresponds to the abalone's age).

## Project Structure

```plaintext
.
├── assets/                   # Directory for storing model or dataset-related assets
├── notebooks/                # Jupyter notebooks for EDA and modeling
│   ├── eda.ipynb             # Notebook for exploratory data analysis
│   └── modelling.ipynb       # Notebook for building and training a machine learning model
├── .gitignore                # Files and directories to ignore in Git
├── environment.yml           # Conda environment setup file
├── pyproject.toml            # Project configuration (for build systems or metadata)
├── README.md                 # Project documentation (this file)
├── requirements.in           # Base dependencies
└── PR_1.md                   # Pull request describing the current changes
```

## Setup Instructions

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-repo/xhec-mlops-project-student.git
cd xhec-mlops-project-student
```

### 2. Set up the Environment

You can set up the project environment using **conda** or **pip**. Here's how to proceed.

#### Using Conda (Recommended)

If you use **conda**, create the environment using the provided `environment.yml` file:

```bash
conda env create -f environment.yml
```

To activate the environment:

```bash
conda activate <your-environment-name>
```

#### Using pip

If you prefer **pip**, you can install the dependencies from `requirements.in`:

```bash
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```

### 3. Run the Notebooks

After setting up the environment, you can explore the dataset and start modeling by opening the Jupyter notebooks in the `notebooks` directory.

1. **EDA Notebook** (`eda.ipynb`):
   - Open this notebook to perform exploratory data analysis on the Abalone dataset. This includes visualizing distributions and analyzing correlations.

2. **Modeling Notebook** (`modelling.ipynb`):
   - This notebook contains the code to build, train, and evaluate a machine learning model for predicting the abalone's age.

You can start Jupyter notebooks with:

```bash
jupyter notebook
```

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

## CI/CD Pipeline

The repository includes a **CI/CD pipeline** using GitHub Actions (configured in `.github/workflows/ci.yaml`), which automates the following tasks:
- Python environment setup.
- Dependency installation.
- Code quality checks (e.g., linting with `flake8`).
- Running unit tests (if added).

This pipeline triggers on every `push` or `pull request` to ensure consistent code quality and reproducibility.