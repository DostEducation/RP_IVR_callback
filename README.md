# RP IVR Callback

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![](https://github.com/DostEducation/RP_IVR_callback/actions/workflows/pre-commit.yml/badge.svg)
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
    python -m venv venv
    ```
3. Activate the virtual environment
    ```sh
    source ./venv/bin/activate
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
## Unit Testing
- Run ```flask db migrate``` to migrate requried database schema.
- Run ```flask db seed``` to populate required data in the database.
- Run ```pytest``` to ensure the integrity of the functions. 

## License
GNU Affero General Public License v3.0
