# Promethium
> Promethium, 61st Element of the periodic table with the *Pm* Symbol. And a good looking name for a quick fun API project.

Promethium is a FastAPI-based web application that provides information about chemical elements from the periodic table. The application serves data from a JSON file and offers various endpoints to retrieve element details.
This API is not intentionnally designed for real world use. It's a learning project to explore FastAPI and compare it to ExpressJS.

## Features
- Retrieve a complete list of chemical elements.
- Fetch details of a specific element by :
    - Atomic number
    - Symbol
    - Name
- Getting Stats about the elements (Coming Soon).

The FastAPI framework comes with an automatic API Documentation feature, accessible at `/docs` or `/redoc` once the server is running.

## Installation
There is two installations methods available: Using Docker or setting up a local Python environment.

### Using Python
1. Clone the repository:
    ```bash
    git clone git@github.com:WyliGr/Promethium.git
    cd Promethium
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ``` 
4. Run the FastAPI application:
    ```bash
    fastapi run
    ```
5. Access the API at `http://localhost:8000` and the documentation at `http://localhost:8000/docs`.

### Using Docker
1. Ensure you have Docker installed on your machine.
2. Clone the repository:
    ```bash
    git clone git@github.com:WyliGr/Promethium.git
    cd Promethium
    ```
3. Build and run the Docker compose:
    ```bash
    docker compose up --build -m .
    ```
4. Access the API at `http://localhost:8080` and the documentation at `http://localhost:8080/docs`.

## Note
The big JSON Data file is provided by @Bowserinator on GitHub and can be found on this repo : [Bowserinator/Periodic-Table-JSON](https://github.com/Bowserinator/Periodic-Table-JSON/blob/master/PeriodicTableJSON.json). (I don't even use 2% of the Data provided)