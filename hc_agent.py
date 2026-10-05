#HC Agent

from openai_module import generate_text_basic
from sample_functions import get_weather

current_weather=get_weather("California")
prompt=f"""Should i take umbrella while going out in California based on the following weather conditions: {current_weather}?"""
response=generate_text_basic(prompt)
print(response)