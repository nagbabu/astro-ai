from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chart import generate_chart

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict")
def predict(
    year:int,
    month:int,
    day:int,
    hour:float,
    lat:float,
    lon:float
):
    # ✅ Always India timezone
    timezone = "Asia/Kolkata"

    return {
        "chart": generate_chart(year, month, day, hour, lat, lon, timezone)
    }
