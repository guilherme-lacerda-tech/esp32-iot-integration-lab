# ESP32 IoT Integration Lab

[![CI](https://github.com/guilherme-lacerda-tech/esp32-iot-integration-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/guilherme-lacerda-tech/esp32-iot-integration-lab/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
[![Release](https://img.shields.io/github/v/release/guilherme-lacerda-tech/esp32-iot-integration-lab)](https://github.com/guilherme-lacerda-tech/esp32-iot-integration-lab/releases)
[![License](https://img.shields.io/github/license/guilherme-lacerda-tech/esp32-iot-integration-lab)](LICENSE)

Public ESP32 integration lab with generic firmware notes, synthetic serial logs and Python validation helpers.

## Why / Problem

IoT experiments can become hard to evaluate when UART, RFID, CAN, GNSS, Cellular and MQTT ideas are mixed together. This repository keeps the lab modular and public.

## Features

- Generic ESP32 firmware foundation.
- Module manifest for UART, RFID, CAN, GNSS, Cellular and future MQTT.
- Generic pinout documentation.
- Synthetic serial logs.
- Python parser for module readiness signals.
- CI with Ruff, PyTest and coverage for the Python helper layer.

## Architecture

```mermaid
flowchart LR
    Firmware["Generic ESP32 firmware"] --> Logs["Synthetic serial log"]
    Logs --> Parser["Python parser"]
    Docs["Bench docs"] --> Firmware
    Parser --> Summary["Module summary"]
```

## Tech Stack

Current: `ESP32` `Arduino` `Python` `Serial logs` `Synthetic data` `PyTest` `Ruff`

Planned: MQTT after the applied IoT study phase, plus one module at a time with public references.

## Quick Start

```powershell
python -m pip install -e ".[dev]"
python examples/run_demo.py
```

## Tests

```powershell
python -m pytest --cov --cov-report=term-missing
python -m ruff check .
```

## Example Output

```text
{'BOOT': 1, 'UART': 1, 'I2C': 1, 'RFID': 1, 'CAN': 1, 'GNSS': 1, 'CELLULAR': 1, 'total_lines': 7}
```

## Project Structure

- `firmware`: generic ESP32 sketch.
- `docs/bench-lab.md`: module-by-module lab plan.
- `docs/generic-pinout.md`: public pinout reference.
- `src/esp32_iot_integration_lab`: Python parser and manifest helpers.
- `tests`: parser and manifest tests.

## Engineering Decisions

- MQTT is intentionally future work, not a marketing checkbox.
- Hardware notes are generic and based on public bench concepts.
- Synthetic logs keep the repository safe and reviewable.

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## Security

No private hardware design, real operational logs, client identifiers or employer documentation are included.
