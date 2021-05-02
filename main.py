import config

import logging

from aiogram import Bot as tg_Bot, Dispatcher, executor, types
from instabot import Bot as inst_Bot

API_TOKEN = config.token;

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
tg_bot = tg_Bot(token=API_TOKEN)
dp = Dispatcher(tg_bot)

inst_bot = inst_Bot()
inst_bot.login(username=config.username, password=config.password)#, proxy="http://194.5.206.179:443")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['check_follow'])
async def check_follow(message: types.Message):
    followers = inst_bot.get_user_followers(
        user_id = inst_bot.get_user_id_from_username(
            username = 'nt_crckr'
        )
    )
    s = ""
    for i in range(10):
        s += inst_bot.get_username_from_user_id(followers[i]) + " "
    await message.answer(s)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
