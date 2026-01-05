import dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.tools import ToolContext, google_search
from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams
from mcp import StdioServerParameters

dotenv.load_dotenv()

# https://google.github.io/adk-docs/tools-custom/mcp-tools/#step-1-define-your-agent-with-mcptoolset
mcp_tool_hugeicons = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='npx',
            args=[
                "-y",
                "@hugeicons/mcp-server"
            ]
        )
    )
)

root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction="""You are a helpful icon search assistant. 
1. When searching for icons, you MUST translate the user's search query into English. 
2. If the tool returns no results, clearly inform the user that no icons were found for that keyword.
3. DO NOT finish the conversation with an empty response.""",
    tools=[mcp_tool_hugeicons]
)
