from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_KEY"
)

def analyze_chart(chart):
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{
            "role": "user",
            "content": f"Analyze this astrology chart: {chart}"
        }]
    )
    return response.choices[0].message.content