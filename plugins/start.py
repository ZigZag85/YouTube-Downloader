from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["start"]), group=-2)

async def start(client, message):

    # return

    joinButton = InlineKeyboardMarkup([

        [InlineKeyboardButton(

            "✈ Follow me on Instagram ✈", url="https://instagram.com/rizad__x96?utm_medium=copy_link")]

    ])

    welcomed = f"""ʜᴇʏ {message.from_user.first_name}
ɪᴀᴍ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ..
sᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴜʀʟ(ʟɪɴᴋ) ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ..

➪ Bot Name : ʏᴏᴜᴛᴜʙᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ
➪ Author : [rizadッ](https://telegram.me/riz4d)
➪ Donate : [Paypal](https://www.payPal.com/paypalme/rizadx96)
➪ Language : Python
➪ License Type : GNU(GPL)"""

    await message.reply_text(welcomed, reply_markup=joinButton)

    raise StopPropagation

