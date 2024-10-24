from pathlib import Path

# [1] means go up 1 level from the current file
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIRPATH = str(PROJECT_ROOT / "data")
MODELS_DIRPATH = str(PROJECT_ROOT / "src/web_service/local_objects")
