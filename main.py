import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
import handlers
from config import token

dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=token)
    dp.include_routers(handlers.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
