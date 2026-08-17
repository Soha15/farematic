# Farematic

> **Know your fare before you flag one down.**

Farematic is a ride fare comparison web application that estimates fares for **Uber, Ola, and Rapido** based on a user's pickup and destination locations, then recommends the most affordable option. The project combines a **FastAPI** backend with a responsive HTML, CSS, and JavaScript frontend to deliver a clean, real-time comparison experience.

**Live app:** [farematic.azurewebsites.net](https://farematic.azurewebsites.net/)

## Features

- Compare estimated fares across Uber, Ola, and Rapido
- Enter any pickup and destination location
- Calculate driving distance and estimated travel time
- Recommend the lowest estimated fare automatically
- Display ETA for each ride provider
- Responsive interface for desktop and mobile
- Secure API key management using environment variables

## How It Works

1. Enter a pickup and destination.
2. The backend geocodes both locations using OpenRouteService.
3. The route distance and travel duration are calculated.
4. Estimated fares and ETAs are generated for each provider.
5. Farematic highlights the recommended ride based on the lowest estimated fare.

## Tech Stack

**Backend**

- Python
- FastAPI
- Requests
- Uvicorn

**Frontend**

- HTML5
- CSS3
- JavaScript

**API**

- OpenRouteService Geocoding API
- OpenRouteService Directions API

**Deployment**

- Azure App Service (Linux, Python runtime)

## Project Structure

```
Farematic/
│
├── main.py
├── requirements.txt
├── README.md
│
└── static/
    └── index.html
```

## Installation

### 1. Clone the repository

```
git clone https://github.com/YOUR-USERNAME/Farematic.git
cd Farematic
```

### 2. Create a virtual environment

**macOS / Linux**

```
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

## Configure the API Key

Create an OpenRouteService API key and set it as an environment variable.

**macOS / Linux**

```
export ORS_API_KEY="your_api_key_here"
```

**Windows PowerShell**

```
$env:ORS_API_KEY="your_api_key_here"
```

> Never commit your API key to GitHub.

## Run the Application

Start the FastAPI server:

```
uvicorn main:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

## Deployment

Farematic is deployed on **Azure App Service** (Linux, Python 3.11 runtime), with `ORS_API_KEY` set as an App Service environment variable rather than committed to the repo.

Live at: **https://farematic.azurewebsites.net/**

## API Endpoint

### GET `/recommend`

Returns the route details, estimated travel time, estimated fares, and the recommended ride provider.

Example request:

```
/recommend?start=Gachibowli&end=Secunderabad
```

## Future Improvements

- Live pricing integration from ride providers
- Interactive route map
- Location autocomplete
- GPS-based current location
- Fare history and price trends
- User authentication and saved trips
- Automated CI/CD pipeline (GitHub Actions to Azure)
- Logging and monitoring dashboard

## Disclaimer

Farematic provides **estimated fare comparisons** for educational and portfolio purposes. Actual ride prices and ETAs may vary depending on traffic, demand, surge pricing, and provider policies.

## License

This project is released under the MIT License.
