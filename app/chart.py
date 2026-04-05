import swisseph as swe
from app.utils import get_sign, get_house, get_nakshatra, DASHA_YEARS

def calculate_lagna(jd, lat, lon):
    houses, ascmc = swe.houses(jd, lat, lon)
    return ascmc[0]

def generate_chart(year, month, day, hour, lat, lon):
    swe.set_topo(lon, lat, 0)
    jd = swe.julday(year, month, day, hour)

    asc_deg = calculate_lagna(jd, lat, lon)

    planets_raw = {
        "Sun": swe.calc_ut(jd, swe.SUN)[0][0],
        "Moon": swe.calc_ut(jd, swe.MOON)[0][0],
        "Mars": swe.calc_ut(jd, swe.MARS)[0][0],
        "Mercury": swe.calc_ut(jd, swe.MERCURY)[0][0],
        "Jupiter": swe.calc_ut(jd, swe.JUPITER)[0][0],
        "Venus": swe.calc_ut(jd, swe.VENUS)[0][0],
        "Saturn": swe.calc_ut(jd, swe.SATURN)[0][0],
    }

    planets = {}
    for p, deg in planets_raw.items():
        planets[p] = {
            "degree": deg,
            "sign": get_sign(deg),
            "house": get_house(deg, asc_deg)
        }

    moon_deg = planets_raw["Moon"]
    nakshatra, dasha_lord = get_nakshatra(moon_deg)

    return {
        "lagna": {"degree": asc_deg, "sign": get_sign(asc_deg)},
        "planets": planets,
        "nakshatra": nakshatra,
        "current_dasha": {
            "lord": dasha_lord,
            "duration": DASHA_YEARS[dasha_lord]
        }
    }
