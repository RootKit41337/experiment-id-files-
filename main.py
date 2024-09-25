import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import  user


logger = logging.getLogger(__name__)

async def main() -> None:
        #logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    #config
    config: Config = load_config()

    #bot
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    #routers
    dp.include_routers(
        user.router,
    )

    #start
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())