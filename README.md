# Self-Assist
Self-Assist is a idea of two college friends, which aims to automate the day to day computer related tasks :)

## Pre-requisites
- llama3:8b model. You can download it using the ollama's CLI.
    ```sh
    ollama pull llama3:8b
    ```

- Download the ollama's CLI on Linux
    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
- Else, Download the ollama's CLI from website [here](https://ollama.com/download)

## Intial Setup

1. Create Virtual Enviornment
    ```sh
    python -m venv env
    ```

2. Activate Virtual Enviornment
- Linux/Mac:
    ```sh
    source env/bin/activate
    ```
- Windows:
    ```sh
    .\env\Scripts\activate
    ```

3. Install Requirements
    ```sh
    pip install -r requirements.txt
    ```
4. Run the application
    ```sh
    python main.py
    ```
