"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","pyro-botz")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>👋 Hi {},
I am a powerful rename bot! custom thumbnail and caption features.

Click help button to know more about me</b>"""

    ABOUT_TXT = """○ 𝖬𝗒 𝖭𝖺𝗆𝖾 : {}
○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href='https://t.me/hell_botz'>˹ʜᴇʟʟ ʙᴏᴛᴢ˼</a>
○ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : <a href='https://docs.pyrogram.org/'>ᴩʏʀᴏɢʀᴀᴍ</a>
○ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <a href='https://www.python.org/download/releases/3.0/'>ᴩyᴛʜᴏɴ 3</a>
○ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏDB</a>
○ 𝖲𝖾𝗋𝗏𝖾𝗋 : <a href='https://t.me/source_Codez/3/'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
○ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : v3.0.0 [ ꜱᴛᴀʙʟᴇ ]"""


    HELP_TXT = """
ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:

● /start - ᴄʜᴇᴄᴋ ɪ'ᴍ ᴀʟɪᴠᴇ 
● /set_caption - ᴛᴏ ᴀᴅᴅ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ
● /see_caption - ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ
● /del_caption - ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ
● /viewthumb - ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ
● /delthumb - ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ

● sᴇɴᴅ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴇ ᴛᴏ ᴀᴅᴅ ᴀs ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ
● sᴇɴᴅ ʏᴏᴜʀ ғɪʟᴇs ᴛᴏ ᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ.. """

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @ᴩyʀᴏ_ʙᴏᴛᴢ🙏🥲
    DEV_TXT = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : ᴜɴᴋɴᴏᴡɴ
• ᴜꜱᴇʀɴᴀᴍᴇ : @imanonadmin
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='t.me/imanonadmin'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰𝖯𝖱𝖮𝖢𝖤𝖲𝖲 𝖡𝖠𝖱❱━➣
┣⪼ 🗃️ 𝖲𝗂𝗓𝖾: {1} | {2}
┣⪼ ⏳️ 𝖣𝗈𝗇𝖾 : {0}%
┣⪼ 🚀 𝖲𝗉𝖾𝖾𝖽: {3}/s
┣⪼ ⏰️ 𝖤𝗍𝖺: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""


