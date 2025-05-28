import asyncio
import logging
from src.utils.config import get_config_from_args
from src.utils.logger import LoggerConfigurator
from src.telegram_core.bot import BotManager
from src.telegram_core.handlers import start


async def main():
    # Загружаем конфигурацию
    config = get_config_from_args()
    
    # Настраиваем логгер с конфигурацией
    LoggerConfigurator(config).configure()
    logging.info("Start bot")
    
    # Создаем менеджер бота с конфигурацией
    bot_manager = BotManager(config)
    bot_manager.get_pager_bot().add_routes([
        start.start_route,
    ])
    
    logging.debug("Start polling")
    # await BaseRequest.init_database()

    await bot_manager.start_bot()


if __name__ == "__main__":
    asyncio.run(main())