"""data_loader.py"""
from pathlib import Path
import yaml

# Load config
with open('../configs/_default_configs.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Define paths
PROJECT_ROOT = Path(os.getcwd()).parent
DATA_DIR = PROJECT_ROOT / config['paths']['data_dir']
PROCESSED_DATA_DIR = PROJECT_ROOT / config['paths']['processed_data_dir']
NOTEBOOKS_DIR = PROJECT_ROOT / config['paths']['notebooks_dir']
MODEL_DIR = PROJECT_ROOT / config['paths']['model_dir']

# Define dataset paths
BNT_PATH= DATA_DIR / 'BNT-syntheticData_v2.xlsx'
FAS_PATH = DATA_DIR / 'FAS-syntheticData_v1.xlsx'
SVF_PATH = DATA_DIR / 'SVF-syntheticData_v1.xlsx'