# End-to-End Agentic AI Trip Planner ✈️ 🌍

## 📖 Overview

This project is an ******End-to-End Agentic AI Trip Planner built using LangChain, Streamlit, and Python 3.12.*** It leverages the power of Large Language Models (LLMs) and a suite of external tools (APIs) to act as an intelligent travel agent.

Unlike simple chatbots, this system utilizes an Agentic Workflow. The AI autonomously decides which tools to use (Weather, Currency, Search, etc.) to generate a comprehensive travel plan. It follows MLOps best practices with modular coding, custom logging, and exception handling.

## 🚀 Key Features

- Dual Itinerary Generation: Automatically generates two distinct plans:

    1. Generic/Tourist Plan: Popular attractions and standard routes.

    2. Off-Beat Plan: Hidden gems and less crowded locations.

- Real-Time Data Fetching: Uses live tools for weather, currency exchange rates, and place information.

- Comprehensive Logistics: Provides hotel recommendations, restaurant suggestions, transportation modes, and detailed cost breakdowns.

- Budget Management: Calculates approximate per-day expenses and total trip costs.

- Modular MLOps Structure: specific modules for logging, exception handling, and configuration management.

## 🏗️ Project Structure

The project follows a production-ready directory structure:

```bash
├── Agent/
│   ├── agenticWorkFlow.py   # Core logic for the Agent's decision-making process
├── config/                  # Configuration management
├── exception/
│   └── excHandel.py         # Custom exception handling
├── logger/
│   └── logging.py           # Centralized logging configuration
├── promptLibrary/
│   └── prompt.py            # LLM System prompts and instruction sets
├── tools/                   # Tool definitions for the Agent
│   ├── airthmatic.py        # Calculation tools
│   ├── currencyConversion.py
│   ├── placeSearch.py
│   └── waeatherInfo.py
├── utils/                   # Utility helper functions
│   ├── configLoader.py
│   ├── modelLoader.py
│   ├── saveToDoc.py
│   └── ...
├── streamlitApp.py          # Frontend UI entry point
├── pyproject.toml           # Project metadata
├── requirements.txt         # Dependencies
├── setup.py                 # Package setup
├── .env                     # Environment variables (Secrets)
└── README.md
```
## 🛠️ Tech Stack & Tools

- Language: Python 3.12.2

- Package Manager: ```uv``` (An extremely fast Python package installer and resolver)

- Framework: LangChain (for Agentic orchestration)

- UI: Streamlit

- APIs Integrated:

    1. OpenAI / Groq (LLM Inference)

    2. Google Places & Serper/Tavily (Location Data)

    3. OpenWeatherMap (Weather Forecasts)

    4. Exchange Rate API (Currency Conversion)

## ⚙️ Installation & Setup

This project uses ```uv``` for high-performance dependency management.

1. Prerequisites

Ensure you have uv installed. If not:

```bash
pip install uv
```

2. Clone and Initialize
```bash
git clone <repository-url>
cd <repository-name>

# Initialize uv project
uv init
````

3. Environment Setup

Create a virtual environment with the specific Python version:
```bash
uv venv .venv --python 3.12.2

# Activate the environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

4. Install Dependencies
```bash
# Install core requirements
uv pip install -r requirements.txt

# Install the project in editable mode
uv pip install -e .
```

🔐 Configuration

Create a .env file in the root directory to store your API keys. The Agent requires these to function correctly:
```bash
OPENAI_API_KEY="sk-..."
GROQ_API_KEY="gsk_..."
GOOGLE_API_KEY="..."
GPLACES_API_KEY="..."
TAVILAY_API_KEY="tvly-..."
FOURSQURE_API_KEY="..."
OPENWEATHERMAP_API_KEY="..."
EXCHANGE_RATE_KEY="..."
```
## 🏃‍♂️ Usage

1. Ensure your virtual environment is active.

2. Run the Streamlit application:
```bash
streamlit run streamlitApp.py
```

3. In the App:

    - Enter the Source location.

     - Enter the Destination.

    - Specify the Date of Travel.

    - Click Plan My Trip.

The Agent will display the thought process (tracing tools used) and output a detailed Markdown report with the dual itinerary.

## 🧠 How the Agent Works

1. User Input: The user provides destination details via Streamlit.

2. Prompt Engineering: The input is wrapped in the System Prompt defined in promptLibrary/prompt.py.

3. Tool Selection: The LLM analyzes the request and decides which tools to call (e.g., "I need to check the weather in Paris" -> calls weatherInfoSearch).

4. Data Aggregation: The Agent gathers data from Google, Weather APIs, and Currency converters.

5. Synthesis: The LLM synthesizes the raw data into a human-readable, formatted travel plan.

## 📄 License

[MIT License](LICENSE)