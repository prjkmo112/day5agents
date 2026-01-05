import asyncio

from google.adk.runners import InMemoryRunner

from deepdive.adk_with_mcp.agent import root_agent


async def main():
    runner = InMemoryRunner(agent=root_agent)
    response = await runner.run_debug(
        "아이콘 목록 중에 '신발'과 관련된 게 있어?"
    )

    print(response)

    await asyncio.sleep(1)

    return response

if __name__ == "__main__":
    asyncio.run(main())