import dotenv
dotenv.load_dotenv()

import os
from logging import root
import vertexai
from vertexai import agent_engines
from travel_advisor_agent.agent import root_agent
from vertexai.preview import reasoning_engines

PROJECT_ID = "gugak-382907"
LOCATION = "asia-northeast1"
BUCKET = "gs://deockpal-weather_agent"

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=BUCKET,
)

app = reasoning_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,
)

remote_app = agent_engines.create(
    display_name="Travel Advisor Agent",
    agent_engine=app,
    requirements=[
        "google-cloud-aiplatform[adk,agent_engines]", 
        "litellm",
    ],
    extra_packages=[
        "travel_advisor_agent"
    ],
    env_vars={
        "OPENAI_API_KEY": os.environ.get("OPENAI_API_KEY"),
    }
)