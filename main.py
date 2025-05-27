import asyncio
import logging
from src.utils.logger import LoggerConfigurator
from src.telegram_core.bot import BotManager
from src.telegram_core.handlers import start


async def main():
    LoggerConfigurator().configure()
    logging.info("Start bot")
    # Объект бота
    bot_manager = BotManager()
    bot_manager.get_pager_bot().add_routes([
        start.start_route,
    ])
    logging.debug("Start polling")
    # await BaseRequest.init_database()

    await bot_manager.start_bot()


if __name__ == "__main__":
    asyncio.run(main())
