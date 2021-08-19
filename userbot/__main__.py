import sys

import userbot
from userbot import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import catub
from .utils import (
    add_bot_to_logger_group,
    ipchange,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("JMTHON")

print(userbot.__copyright__)
print("Licensed under the terms of the " + userbot.__license__)

cmdhr = Config.COMMAND_HAND_LER


try:
    LOGS.info("Starting Userbot")
    catub.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()


async def startup_process():
    check = await ipchange()
    if check is not None:
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("بوت آيس ثون يعمل بنجاح .!!!")
    print(
        f"مبروك اكتمل التنصيب ارسل {cmdhr}فحص للتاكد من ان البوت شغال \
        \nجميع الحقوق محفوظة لقناه آيس ثون  - @ICE16"
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()


catub.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    catub.disconnect()
else:
    try:
        catub.run_until_disconnected()
    except ConnectionError:
        pass
