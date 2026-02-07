# Space Satellite Telemetry Decoder

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Construct](https://img.shields.io/badge/Construct-2.10-red.svg)](https://construct.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade telemetry decoder** for satellite ground stations. Designed to parse raw binary data streams into structured, human-readable formats using declarative binary structures.

## 🚀 Features

- **Binary Parsing**: Declarative schemas for complex binary data using the `Construct` library.
- **Multi-Frame Support**: Handles CCSDS-like packets and custom telemetry frames.
- **Validation**: CRC and checksum verification for data integrity.
- **Extensible**: Easily add new packet definitions for different satellite subsystems (EPS, ADCS, OBC).
- **Exporting**: Supports exporting decoded data to JSON or CSV for further analysis.
- **Containerized**: Ready-to-use Docker environment.

## 📁 Project Structure

```
space-satellite-telemetry-decoder/
├── src/
│   ├── models/       # Binary definitions (Subsystems, Frames)
│   ├── core/         # Decoder engine and validation logic
│   ├── utils/        # Converters and hex processing
│   └── cli.py        # Command-line interface
├── data/             # Sample telemetry binary files
├── tests/            # Unit and integration tests
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/space-satellite-telemetry-decoder.git

# Install
pip install -r requirements.txt

# Decode a sample file
python src/cli.py decode data/sample_telem.bin
```

## 📄 License

MIT License
