from os import environ

from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from _bot import bot

bot_name = environ.get('bot_name', 'ᴅɪɢɪᴛᴀʟ ᴏᴄᴇᴀɴ ᴀssɪsᴛᴀɴᴛ')


def start(d: Message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton(
            text='ᴀᴅᴅ ᴀᴄᴄᴏᴜɴᴛ',
            callback_data='add_account'
        ),
        InlineKeyboardButton(
            text='ᴍᴀɴᴀɢᴇ ᴀᴄᴄᴏᴜɴᴛ',
            callback_data='manage_accounts'
        ),
        InlineKeyboardButton(
            text='ᴄʀᴇᴀᴛᴇ ᴅʀᴏᴘʟᴇᴛ',
            callback_data='create_droplet'
        ),
        InlineKeyboardButton(
            text='ᴍᴀɴᴀɢᴇ ᴅʀᴏᴘʟᴇᴛs',
            callback_data='manage_droplets'
        ),
    )
    t = f'Welcome to  <b>{bot_name}</b>\n\n' \
        'You can Use me to manage your DigitalOcean account.Create Droplets,Manage Droplets and many more features concerning your DigitalOcean account..\n\nTo use Me you need to have Permission from my owner'\
        'Here Goes My Command List :\n' \
        '➥/start - sᴛᴀʀᴛs ᴛʜᴇ ʙᴏᴛ\n' \
        '➥/add_do - ᴀᴅᴅ ᴀ ɴᴇᴡ ᴀᴄᴄᴏᴜɴᴛ\n' \
        '➥/sett_do - ᴍᴀɴᴀɢᴇ ᴀᴄᴄᴏᴜɴᴛ\n' \
        '➥/bath_do - ʙᴀᴛᴄʜ ᴛᴇsᴛ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ\n' \
        '➥/add_vps - ᴄʀᴇᴀᴛᴇ ᴅʀᴏᴘʟᴇᴛs\n' \
        '➥/sett_vps - ᴍᴀɴᴀɢᴇ ᴅʀᴏᴘʟᴇᴛs\n' \
        ' \n' \
        '<b>✔ᴅᴇᴠᴇʟᴏᴘᴇʀ: @EscaliBud</b>\n' \
        '<b>✔sᴜᴘᴘᴏʀᴛ: @InfinityHackersKE</b>'
    bot.send_message(
        text=t,
        chat_id=d.from_user.id,
        parse_mode='HTML',
        reply_markup=markup
    )
