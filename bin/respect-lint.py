#!/usr/bin/env python3
"""
respect-lint executable entrypoint.
"""
import sys
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from respect_lint import main

if __name__ == "__main__":
    main()
