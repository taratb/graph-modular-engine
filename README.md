# Graph Modular Engine
Modular graph visualization platform with plugin architecture and Django web interface

## Team

- Tara Bogdanić (SV 33/2024)
- Staša Stamenković (SV 50/2024)
- Ignjatije Ignjatović (SV 19/2024)

## Requirements

- Python 3.10 or newer (tested with Python 3.15.0)
- Git

## API setup

Run these commands from the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ./api
```

## Running tests

From the repository root, with the virtual environment activated:

```powershell
python -m unittest discover -s api/tests -v
```