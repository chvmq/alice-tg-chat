from aiogram import types


async def send_welcome(message: types.Message):
    print(message.as_json())
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


async def echo(message: types.Message):
    await message.answer(message.text)
