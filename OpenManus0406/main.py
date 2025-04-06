import asyncio

from app.agent.manus import Manus
from app.logger import logger


async def main():
    agent = Manus()
    try:
        prompt = input("Enter your prompt: ")
        if not prompt.strip():
            logger.warning("Empty prompt provided.")
            return

        logger.warning("Processing your request...")
        await agent.run(prompt)
        logger.info("Request processing completed.")
    except KeyboardInterrupt:
        logger.warning("Operation interrupted.")
    finally:
        # Ensure agent resources are cleaned up before exiting
        await agent.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
    # html生成贪吃蛇游戏
    # 搜索 Manus Agent 的信息和报道，生成一个 html 用来汇总和报告这个 Agent，你的 html 应该尽可能美观。需要每一步保存文件