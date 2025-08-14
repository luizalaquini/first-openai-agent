from agents import Agent, ModelSettings, function_tool, Runner
from loguru import logger

@function_tool
def get_weather(city: str) -> str:
    """returns weather info for the specified city."""
    logger.debug("agent calling get_weather tool")
    return f"The weather in {city} is sunny"

agent = Agent(
    name="Haiku agent",
    instructions="Always respond in haiku form",
    model="gpt-4.1-nano-2025-04-14",
    tools=[get_weather],
)

# ----------------------------------------------------------------------
# Define functions to run the agent and print the result

# Sync function
def run_agent():
    result = Runner.run_sync(agent, "How is the weather in Paris?")
    logger.info(f"Reponse:\n{result.final_output}")

# Async function
async def run_agent_async():
    result = await Runner.run(agent, "How is the weather in Paris?")
    logger.info(f"Reponse:\n{result.final_output}")

# Run the agent synchronously
run_agent()

# # Uncomment the following line to run the agent asynchronously
# import asyncio
# asyncio.run(run_agent_async())