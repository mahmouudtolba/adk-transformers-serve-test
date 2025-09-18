import json
import os
from pathlib import Path
from datetime import datetime
import pytz
import litellm
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import random
litellm._turn_on_debug()

# --- Tool function ---
def get_random_number() -> int:
    """Return a random integer between 1 and 100."""
    return random.randint(1, 100)

local_llm = LiteLlm(model="huggingface/Qwen/Qwen3-0.6B",
api_base_url ="http://localhost:8000/v1" )

root_agent = Agent(
    model=local_llm ,
    name="tool_agent",
        description="Fetch a random number using get_random_number tool.",
    instruction="If the user asks for a random number, call the `get_random_number` tool.",
    tools=[get_random_number],  # or wrap with Tool(...) if required
)
