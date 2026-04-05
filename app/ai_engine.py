import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_chart(chart):
    prompt = f"""
    You are a Vedic astrologer.

    Chart:
    {chart}

    Analyze:
    - Personality
    - Career
    - Finance
    - Relationships
    - Next 5 years

    Return JSON.
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
