"""normalizer.py"""
import pandas as pd
import re

def norm(s: pd.Series) -> pd.Series:
    """Normalize pd.Series by lowercasing, stripping whitespace, and removing punctuation."""
    s = s.astype(str).str.lower().str.strip()
    s = s.str.replace(r"[^\wåäö\- ]+", " ", regex=True)   # remove punctuation
    s = s.str.replace(r"\s+", " ", regex=True).str.strip()
    return s