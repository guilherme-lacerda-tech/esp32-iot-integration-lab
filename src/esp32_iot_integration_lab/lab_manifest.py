from __future__ import annotations


def module_manifest() -> list[dict]:
    return [
        {"module": "UART", "status": "active", "evidence": "synthetic serial log parser"},
        {"module": "RFID", "status": "documented", "evidence": "generic demo tag in synthetic log"},
        {"module": "CAN", "status": "documented", "evidence": "generic bench flow"},
        {"module": "GNSS", "status": "planned", "evidence": "pinout and log placeholder"},
        {"module": "Cellular", "status": "documented", "evidence": "generic modem readiness flow"},
        {"module": "MQTT", "status": "future", "evidence": "reserved for later study"},
    ]
