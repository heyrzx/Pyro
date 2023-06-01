from pyrogram import Client, filters 
from helper.database import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**ɢɪᴠᴇ ᴛʜᴇ ᴄᴀᴩᴛɪᴏɴ\n\nᴇxᴀᴍᴩʟᴇ:- `/set_caption {filename}\n\n💾 ꜱɪᴢᴇ: {filesize}\n\n⏰ ᴅᴜʀᴀᴛɪᴏɴ: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**✅ ᴄᴀᴩᴛɪᴏɴ ꜱᴀᴠᴇᴅ**")
   
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("**yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴy ᴄᴀᴩᴛɪᴏɴ**")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**❌️ ᴄᴀᴩᴛɪᴏɴ ᴅᴇʟᴇᴛᴇᴅ**")
                                       
@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption']))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**yᴏᴜ'ʀᴇ ᴄᴀᴩᴛɪᴏɴ:-**\n\n`{caption}`")
    else:
       await message.reply_text("**yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴy ᴄᴀᴩᴛɪᴏɴ**")


@Client.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("**yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴy ᴛʜᴜᴍʙɴᴀɪʟ**") 
		
@Client.on_message(filters.private & filters.command(['del_thumb', 'delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("❌️ **ᴛʜᴜᴍʙɴᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ**")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("ᴩʟᴇᴀꜱᴇ ᴡᴀɪᴛ....")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("✅️ **ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ**")


