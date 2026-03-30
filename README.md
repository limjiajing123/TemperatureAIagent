# 🤖 Local Hardware Monitor Agent (Agent Alpha)

A lightweight AI Agent designed to run on resource-constrained hardware. This project demonstrates the ability to bridge **Large Language Models (LLMs)** with **system-level tools** using a local reasoning loop.

---

## 🌟 Why I Built This
Most AI Agents require high-end GPUs or expensive cloud APIs. I built this to prove that a **quantized 1.5B model** can act as a reliable system controller on a consumer-grade laptop (NVIDIA MX250 2GB) with near-zero latency.

## 🛠️ Tech Stack
- **Model:** Qwen 2.5 1.5B (via Ollama)
- **Language:** Python 3.12
- **Environment:** Ubuntu 24.04 (WSL2/Native)
- **Libraries:** `ollama`, `subprocess` (System-level bridge)

## 🧠 How it Works (The ReAct Loop)
The agent follows a **Reasoning + Acting (ReAct)** pattern:
1. **Analyze:** The model receives a user prompt (e.g., "Is my laptop too hot?").
2. **Decision:** It identifies if it needs external data.
3. **Action:** If needed, it triggers a custom Python function to run `nvidia-smi` and fetch real GPU temperatures.
4. **Observation:** It parses the hardware data and explains it back to the user in natural language.

## 🚀 Getting Started

### Prerequisites
- [Ollama](https://ollama.com/) installed and running.
- `qwen2.5:1.5b` model pulled: `ollama pull qwen2.5:1.5b`

### Installation
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/limjiajing123/TemperatureAIagent.git](https://github.com/limjiajing123/TemperatureAIagent.git)
   cd hardware-monitor-agent

### Setup Virtual Environment (Sandbox)
python3 -m venv venv
source venv/bin/activate

### Install Dependencies
pip install -r requirements.txt

### Run the Agent
python3 agent.py
