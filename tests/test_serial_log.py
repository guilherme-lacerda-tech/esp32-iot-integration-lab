from __future__ import annotations

from pathlib import Path

from esp32_iot_integration_lab.lab_manifest import module_manifest
from esp32_iot_integration_lab.serial_log import parse_log


def test_parse_log_counts_public_lab_signals() -> None:
    root = Path(__file__).resolve().parents[1]
    summary = parse_log(root / "data" / "sample" / "synthetic_serial_log.txt")

    assert summary["BOOT"] == 1
    assert summary["UART"] == 1
    assert summary["RFID"] == 1
    assert summary["CAN"] == 1
    assert summary["GNSS"] == 1
    assert summary["CELLULAR"] == 1


def test_manifest_marks_mqtt_as_future() -> None:
    manifest = {item["module"]: item["status"] for item in module_manifest()}

    assert manifest["MQTT"] == "future"
    assert manifest["UART"] == "active"
