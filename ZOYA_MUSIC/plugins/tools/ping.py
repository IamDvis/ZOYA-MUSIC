from datetime import datetime
import random

from pyrogram import filters
from pyrogram.types import Message

from ZOYA_MUSIC import app
from ZOYA_MUSIC.core.call import ZOYA
from ZOYA_MUSIC.utils import bot_sys_stats
from ZOYA_MUSIC.utils.decorators.language import language
from ZOYA_MUSIC.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=random.choice(PING_IMG_URL),
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await ZOYA.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
