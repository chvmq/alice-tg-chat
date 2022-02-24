from aiogram import Dispatcher

from .handlers import (
    send_welcome,
    echo,
)


def register_message_handlers(dispather: Dispatcher):
    dispather.register_message_handler(send_welcome, commands=["start", "help"])
    dispather.register_message_handler(echo)
