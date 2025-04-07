
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import os

# Configura il logging
logging.basicConfig(level=logging.INFO)

# Token del bot
API_TOKEN = 'TUO_TOKEN_BOT'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Gruppo dove inviare i messaggi (ID del gruppo)
GROUP_ID = 'ID_DEL_TUO_GRUPPO'

# Funzione per inviare messaggi nel gruppo
async def forward_to_group(message):
    user_name = message.from_user.username
    topic_name = f"Aiuta {user_name}"
    await bot.send_message(GROUP_ID, f"Nuovo messaggio da {user_name}:
{message.text}", parse_mode=ParseMode.MARKDOWN)

# Comando start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Ciao! Mandami un messaggio e ti inoltrerò nel gruppo!")

# Gestisci i messaggi degli utenti
@dp.message_handler()
async def echo(message: types.Message):
    # Inoltra il messaggio nel gruppo
    await forward_to_group(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
