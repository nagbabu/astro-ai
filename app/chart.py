import swisseph as swe

# Nakshatra list
NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra",
    "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula",
    "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mars": swe.MARS,
    "Mercury": swe.MERCURY,
    "Jupiter": swe.JUPITER,
    "Venus": swe.VENUS,
    "Saturn": swe.SATURN
}


def get_sign(degree):
    return SIGNS[int(degree // 30)]


def get_nakshatra(degree):
    index = int(degree / (13 + 20/60))
    return NAKSHATRAS[index]


def generate_chart(year, month, day, hour, lat, lon):

    # ✅ STEP 1: IST → UTC
    hour_utc = hour - 5.5
    if hour_utc < 0:
        hour_utc += 24
        day -= 1

    # ✅ STEP 2: Julian Day
    jd = swe.julday(year, month, day, hour_utc)

    # ✅ STEP 3: Set Lahiri Ayanamsa (Vedic)
    swe.set_sid_mode(swe.SIDM_LAHIRI)

    # ✅ STEP 4: Get Ayanamsa
    ayanamsa = swe.get_ayanamsa(jd)

    # ✅ STEP 5: Planets
    planet_positions = {}

    for name, planet in PLANETS.items():
        pos = swe.calc_ut(jd, planet)[0][0]
        sidereal_pos = pos - ayanamsa
        sidereal_pos = sidereal_pos % 360

        planet_positions[name] = {
            "degree": sidereal_pos,
            "sign": get_sign(sidereal_pos),
            "house": int((sidereal_pos // 30) + 1)
        }

    # ✅ STEP 6: Lagna (Ascendant)
    houses, ascmc = swe.houses(jd, lat, lon)
    lagna = ascmc[0] - ayanamsa
    lagna = lagna % 360

    # ✅ STEP 7: Moon Nakshatra
    moon_degree = planet_positions["Moon"]["degree"]
    nakshatra = get_nakshatra(moon_degree)

    return {
        "lagna": {
            "degree": lagna,
            "sign": get_sign(lagna)
        },
        "planets": planet_positions,
        "nakshatra": nakshatra,
        "current_dasha": {
            "lord": "Moon",
            "duration": 10
        }
    }
