from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from pathlib import Path

from esp32_iot_integration_lab.serial_log import parse_log


ROOT = Path(__file__).resolve().parents[1]
summary = parse_log(ROOT / "data" / "sample" / "synthetic_serial_log.txt")
print(summary)
