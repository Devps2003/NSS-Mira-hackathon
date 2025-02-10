from dotenv import load_dotenv
from mira_sdk import MiraClient, Flow
import os

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

flow = Flow(source="flow.yaml")

input_dict = {"fitness_goal": "Lose weight", "experience_level": "Beginner", "available_days": 3}

response = client.flow.test(flow,input_dict)

print(response)