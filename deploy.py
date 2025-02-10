from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError
import os

client = MiraClient(config={"API_KEY": "sb-84299630b147af844212eda6c964af61"})     

flow = Flow(source="flow.yaml")                    
try:
    client.flow.deploy(flow)                                
except FlowError as e:
    print(f"Error occurred: {str(e)}")                    
