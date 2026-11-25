# Playwright Practice

This repository contains examples and experiments for learning how Playwright works.

## Prerequisites

- Python
- `pip`
- A virtual environment

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

For Command Prompt, activate the environment with:

```bat
.venv\Scripts\activate.bat
```

Upgrade `pip` and install Playwright:

```powershell
python -m pip install --upgrade pip
python -m pip install playwright
```

Install Playwright's supported browsers:

```powershell
playwright install
```

This downloads the browser builds managed by Playwright, helping ensure that browser behavior and dependencies are consistent across environments.