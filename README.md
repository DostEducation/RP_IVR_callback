# RP IVR Callback

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![](https://github.com/DostEducation/RP_IVR_callback/actions/workflows/pre-commit.yml/badge.svg)
[![build-and-deployment](https://github.com/DostEducation/RP_IVR_callback/actions/workflows/build.yml/badge.svg)](https://github.com/DostEducation/RP_IVR_callback/actions/workflows/build.yml)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

This is a cloud function that receives a callback from telephony systems to capture the details of a call. Currently it support Ozonetel's Kookoo telephony system.

## Installation

### Prerequisite
1. pyenv
2. python 3.8

### Steps
1. Clone the repository
    ```sh
    git clone https://github.com/DostEducation/RP_IVR_callback.git
    ```
2. Switch to project folder and setup the vertual environment
    ```sh
    cd RP_IVR_callback
    python3 -m venv venv
    ```
3. Activate the virtual environment
    For Unix or MacOS, using the bash shell:
    ```sh
    source ./venv/bin/activate
    ```
    For Windows using the Command Prompt. For example it may look like `c:/RP_IVR_analytics/venv/Scripts/Activate.bat`:
    ```sh
     ./venv/bin/activate.bat
    ```
    For windows using PowerShell. For example it may look like `c:/RP_IVR_analytics/venv/Scripts/Activate.ps1`:
    ```sh
     ./venv/bin/activate.ps1
    ```
4. Install the dependencies:
    ```sh
    pip install -r requirements-dev.txt
    ```
5. Set up your .env file by copying .env.example
    ```sh
    cp .env.example .env
    ```
6. Add/update variables in your `.env` file for your environment.
7. Run the following command to get started with pre-commit
    ```sh
    pre-commit install
    ```
8. Start the server by following command
    ```sh
    functions_framework --target=callback --debug
    ```

## License
GNU Affero General Public License v3.0
