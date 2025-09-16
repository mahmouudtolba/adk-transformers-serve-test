import json
import os
from pathlib import Path
from datetime import datetime
import pytz
import litellm
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


def get_current_time(timezone: str = "UTC") -> str:
    """
    Returns the current time in the specified timezone.
    
    Args:
        timezone (str): Timezone name (e.g., "UTC", "Africa/Cairo", "America/New_York")
    
    Returns:
        str: Current time formatted as 'YYYY-MM-DD HH:MM:SS'
    """
    try:
        tz = pytz.timezone(timezone)
    except Exception:
        tz = pytz.UTC  # Fallback to UTC if invalid timezone
    
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")


local_model = LiteLlm(
    model="ollama_chat/qwen3:1.7b",          
)

root_agent = Agent(
    model=local_model ,
    name="tool_agent",
    description=(
        "and fetch the current time using the get_current_time tool."

    ),
    instruction="""
      If the user asks for the current time, call the `get_current_time` tool.
    """,
    tools=[
        get_current_time,
    ],
)