import asyncio
from time import sleep


class BotClient:
    def __init__(self, bot):
        self.bot = bot

    async def edit_text(self, chat_id, message_id, new_text, keyboard=None):
        await self.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=new_text, reply_markup=keyboard, parse_mode='Markdown')

    async def send_text(self, chat_id, text, keyboard=None, timeout=0):
        sleep(timeout)
        await self.bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard, parse_mode='Markdown')

    async def send_multi_text(self, chat_id, arr, time=2):
        messages = arr.split('$%')
        for message in messages:
            await self.send_text(chat_id, message)
            await asyncio.sleep((time))

    async def send_photo(self, chat_id, photo_name, keyboard):
        await self.bot.send_photo(chat_id=chat_id, photo=open(photo_name, "rb"), reply_markup=keyboard)

    async def send_double_dice(self, chat_id, photo_name, keyboard):
        await self.bot.send_photo(chat_id=chat_id, photo=open(photo_name, "rb"), reply_markup=keyboard)
