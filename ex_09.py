"""argv"""
import sys
from pathlib import Path


try:
    path = Path(sys.argv[1])
    print(path.exists())
except IndexError as e:
    print(f"Sorry. No parameter.")