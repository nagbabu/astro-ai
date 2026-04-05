SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
         "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]

def get_sign(deg):
    return SIGNS[int(deg // 30)]

def get_house(planet_deg, asc_deg):
    diff = (planet_deg - asc_deg) % 360
    return int(diff // 30) + 1

NAKSHATRAS = [
    ("Ashwini","Ketu"),("Bharani","Venus"),("Krittika","Sun"),
    ("Rohini","Moon"),("Mrigashira","Mars"),("Ardra","Rahu"),
    ("Punarvasu","Jupiter"),("Pushya","Saturn"),("Ashlesha","Mercury"),
    ("Magha","Ketu"),("Purva Phalguni","Venus"),("Uttara Phalguni","Sun"),
    ("Hasta","Moon"),("Chitra","Mars"),("Swati","Rahu"),
    ("Vishakha","Jupiter"),("Anuradha","Saturn"),("Jyeshtha","Mercury"),
    ("Mula","Ketu"),("Purva Ashadha","Venus"),("Uttara Ashadha","Sun"),
    ("Shravana","Moon"),("Dhanishta","Mars"),("Shatabhisha","Rahu"),
    ("Purva Bhadrapada","Jupiter"),("Uttara Bhadrapada","Saturn"),
    ("Revati","Mercury")
]

DASHA_YEARS = {
    "Ketu":7,"Venus":20,"Sun":6,"Moon":10,
    "Mars":7,"Rahu":18,"Jupiter":16,
    "Saturn":19,"Mercury":17
}

def get_nakshatra(moon_deg):
    index = int(moon_deg // (360/27))
    return NAKSHATRAS[index]
