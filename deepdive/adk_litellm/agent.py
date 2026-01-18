from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool import MCPToolset, SseConnectionParams

# tools
mcp_tool_ddgs = MCPToolset(
    connection_params=SseConnectionParams(
        url="http://localhost:8000/sse"
    )
)

searcher_agent = Agent(
    name="searcher_agent",
    model=LiteLlm(model="ollama_chat/gpt-oss:20b"),
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant.",
    tools=[mcp_tool_ddgs]
)

root_agent = Agent(
    name="root_agent",
    model=LiteLlm(model="ollama_chat/gpt-oss:20b"),
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant.",
    sub_agents=[searcher_agent]
)