from asyncio import run as asyncio_run

from aiogram import Bot, Dispatcher

from src.config import TOKEN
from src.models.base import Base, engine
from src.registers import register_message_handlers


async def main():

    bot = Bot(TOKEN)

    dp = Dispatcher(bot)

    register_message_handlers(dp)

    await dp.skip_updates()

    await dp.start_polling()

if __name__ == "__main__":
    from src.models.user import User
    Base.metadata.create_all(bind=engine)
    asyncio_run(main())
    