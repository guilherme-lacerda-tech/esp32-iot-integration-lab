from __future__ import annotations

from pathlib import Path


SIGNALS = ["BOOT", "I2C", "RFID", "CAN", "CELL"]


def parse_log(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    return {signal: sum(1 for line in lines if signal in line) for signal in SIGNALS}
