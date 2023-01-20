from pathlib import Path
import os
import sys

# ====================== sys.path BASE_DIR 추가 ======================
BASE_DIR : str = os.path.dirname(Path(__file__).resolve().parent)
sys.path.append(BASE_DIR)
from main import Naver
# ======================                        ======================