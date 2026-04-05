from fastapi import FastAPI
from app.chart import generate_chart
from app.ai_engine import analyze_chart

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Astro AI Running"}

@app.get("/predict")
def predict(year: int, month: int, day: int, hour: float, lat: float, lon: float):
    chart = generate_chart(year, month, day, hour, lat, lon)
    analysis = analyze_chart(chart)
    return {"chart": chart, "analysis": analysis}
