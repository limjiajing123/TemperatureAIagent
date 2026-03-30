import ollama
import subprocess

# THE TOOL: This function gets the real hardware data
def get_gpu_temp():
    try:
        cmd = "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits"
        temp = subprocess.check_output(cmd, shell=True).decode().strip()
        return f"The GPU temperature is {temp}°C."
    except:
        return "Could not read GPU temperature."

# THE AGENT LOGIC
def run_agent(user_prompt):
    print(f"--- Agent is thinking about: '{user_prompt}' ---")
    
    system_instructions = (
            "COMMAND: You are a Hardware Monitor. "
            "If the user asks about temperature, heat, or how the laptop feels, "
            "you MUST respond with exactly one word: RUN_TEMP_CHECK. "
            "Do not apologize. Do not give advice. Just say RUN_TEMP_CHECK."
        )

    response = ollama.chat(model='qwen2.5:1.5b', messages=[
        {'role': 'system', 'content': system_instructions},
        {'role': 'user', 'content': user_prompt},
    ])

    content = response['message']['content']

    # THE 'ACTION' LOOP
    if "RUN_TEMP_CHECK" in content:
        print("Action: Agent triggered a hardware scan...")
        real_data = get_gpu_temp()
        
        # Second pass: Give the AI the real data to summarize
        final_output = ollama.chat(model='qwen2.5:1.5b', messages=[
            {'role': 'system', 'content': "You are a helpful AI. Explain this hardware data to the user."},
            {'role': 'user', 'content': f"The sensor says: {real_data}"},
        ])
        print("\nAgent Response:", final_output['message']['content'])
    else:
        print("\nAgent Response:", content)

# TEST IT
run_agent("How is my laptop feeling? Is it too hot?")