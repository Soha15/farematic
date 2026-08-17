import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()

# The key now comes from an environment variable instead of being hardcoded.
# Locally: set it before running, e.g.
#   export ORS_API_KEY="your-key-here"          (Mac/Linux)
#   $env:ORS_API_KEY="your-key-here"             (Windows PowerShell)
# On Azure: set it as an Application Setting (shown in the deployment steps).
API_KEY = os.environ.get("ORS_API_KEY")


@app.get("/recommend")
def recommend(start: str, end: str):
    if not API_KEY:
        return {"error": "Server is missing its API key. Set ORS_API_KEY."}

    headers = {"Authorization": API_KEY}

    start_response = requests.get(
        "https://api.openrouteservice.org/geocode/search",
        headers=headers,
        params={"text": start},
    )
    end_response = requests.get(
        "https://api.openrouteservice.org/geocode/search",
        headers=headers,
        params={"text": end},
    )

    if start_response.status_code != 200 or end_response.status_code != 200:
        return {"error": "Unable to find locations"}

    start_data = start_response.json()
    end_data = end_response.json()

    if not start_data["features"] or not end_data["features"]:
        return {"error": "Location not found"}

    start_coords = start_data["features"][0]["geometry"]["coordinates"]
    end_coords = end_data["features"][0]["geometry"]["coordinates"]

    route_response = requests.post(
        "https://api.openrouteservice.org/v2/directions/driving-car",
        headers={"Authorization": API_KEY, "Content-Type": "application/json"},
        json={"coordinates": [start_coords, end_coords]},
    )

    if route_response.status_code != 200:
        return {"error": "Unable to calculate route"}

    route = route_response.json()
    distance = route["routes"][0]["summary"]["distance"] / 1000
    duration = route["routes"][0]["summary"]["duration"] / 60

    fares = {
        "Uber": round(50 + distance * 18, 2),
        "Ola": round(45 + distance * 17, 2),
        "Rapido": round(40 + distance * 15, 2),
    }
    eta = {
        "Uber": round(duration + 3),
        "Ola": round(duration + 5),
        "Rapido": round(duration + 2),
    }
    best = min(fares, key=fares.get)

    return {
        "source": start,
        "destination": end,
        "distance_km": round(distance, 2),
        "estimated_time_minutes": round(duration, 2),
        "recommended": best,
        "estimated_fares": fares,
        "Duration_Time": eta,
    }


# Serves index.html (and any other files in /static) at the site root.
# Keep this mounted LAST so it doesn't swallow the /recommend route above.
app.mount("/", StaticFiles(directory="static", html=True), name="static")
