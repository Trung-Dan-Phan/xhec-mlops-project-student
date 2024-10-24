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


## PR0 : Environment setup

### Environment Setup

To set up the Python environment for this project, please follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Trung-Dan-Phan/xhec-mlops-project-student
   cd xhec-mlops-project-student
   ```

2. **Create a virtual environment with Conda**:
   ```bash
   conda env create --file environment.yml
   ```

3. **Activate the virtual environment**:
    ```bash
    conda activate xhec-mlops
    ```

4. **In order to stop using this virtual environment**:
    ```bash
    (xhec-mlops) $ deactivate
    ```

5. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```

6. **Run pre-commit hooks**:
    ```bash
    pre-commit install
    ```
