#HC Agent

from openai_module import generate_text_basic
from sample_functions import get_weather
from prompts import react_system_prompt
prompt=f"Should i take umbrella while going out in California "
response=generate_text_basic(prompt,model="openai/gpt-oss-120b",system_prompt=react_system_prompt)
print(response)     