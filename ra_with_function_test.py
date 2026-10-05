

from openai_module import generate_text_basic
from sample_functions import get_weather
from prompts import react_system_prompt

from json_helpers import extract_json

#Available functions are
available_actions={
    "get_weather":get_weather
}
prompt=f"Should i take umbrella while going out in California "
response=generate_text_basic(prompt,model="openai/gpt-oss-120b",system_prompt=react_system_prompt)
# print(f"Response from Model:{response}")
json_function=extract_json(response)
if json_function:
        function_name = json_function[0]['function_name']
        function_parms = json_function[0]['function_parms']
        if function_name not in available_actions:
            raise Exception(f"Unknown action: {function_name}: {function_parms}")
        print(f" -- running {function_name} {function_parms}")
        action_function = available_actions[function_name]
        #call the function
        result = action_function(**function_parms)
        function_result_message = f"Action_Response: {result}"
        print(function_result_message)

#instruct the model to to call  the action or function 
# print(f"Extracted JSON Function:{json_function}")     