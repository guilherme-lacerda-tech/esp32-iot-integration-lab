# Generic ESP32 Bench Pinout

This is a public, generic reference for future bench experiments. It is not copied from a private design.

| Function | Example GPIO | Notes |
| --- | ---: | --- |
| UART TX | 17 | Generic serial console or module TX path |
| UART RX | 16 | Generic serial console or module RX path |
| I2C SDA | 21 | Generic sensor bus |
| I2C SCL | 22 | Generic sensor bus |
| RFID CS | 5 | Placeholder for SPI RFID reader |
| CAN TX | 27 | Placeholder for CAN transceiver TX |
| CAN RX | 26 | Placeholder for CAN transceiver RX |
| GNSS RX | 34 | Input-only GPIO example for serial data |
| Cellular PWR | 4 | Generic modem control placeholder |

Validate pin choices against the exact ESP32 board and public module datasheets before wiring hardware.
