import ollama
import subprocess
from pydantic import BaseModel, Field
from typing import Literal

# 1. THE SCHEMA: This defines exactly what 'Success' looks like for the AI
class AgentResponse(BaseModel):
    action: Literal["check_temp", "chat"] = Field(description="The tool the AI wants to use.")
    thought: str = Field(description="The internal reasoning behind the action.")
    message: str = Field(description="The text to show the user.")

def get_gpu_temp():
    try:
        cmd = "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits"
        return f"{subprocess.check_output(cmd, shell=True).decode().strip()}°C"
    except:
        return "Sensor Error"

def run_v2_agent(user_input):
    # We tell Ollama to follow our Pydantic schema
    system_prompt = (
        "You are a Hardware Assistant. You must respond in JSON format. "
        f"Schema: {AgentResponse.model_json_schema()}"
    )

    response = ollama.chat(
        model='qwen2.5:1.5b',
        format='json', # This is the 'magic' setting for reliability
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_input}
        ]
    )

    # 2. VALIDATION: We turn the AI's text into a real Python object
    data = AgentResponse.model_validate_json(response['message']['content'])
    
    print(f"\n🧠 AI Thought: {data.thought}")
    
    if data.action == "check_temp":
        current_temp = get_gpu_temp()
        print(f"🌡️ Action: Checking Hardware... Result: {current_temp}")
    
    print(f"💬 Agent: {data.message}\n")

# Test it
run_v2_agent("Hey, check my GPU heat please!")