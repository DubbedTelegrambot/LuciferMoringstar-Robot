import re, asyncio, random
# from pyrogram import Client as LuciferMoringstar_Robot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from LuciferMoringstar_Robot.database._utils import get_size, split_list
from LuciferMoringstar_Robot.database.autofilter_db import get_filter_results
from config import BUTTONS, bot_info, BOT_PICS, FORCES_SUB
from translation import LuciferMoringstar


#@LuciferMoringstar_Robot.on_message(Worker.text & Worker.group & Worker.incoming & Worker.chat(AUTH_GROUPS) if AUTH_GROUPS else Worker.text & Worker.group & Worker.incoming)
async def group_filters(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 50:    
        btn = []
        search = message.text
        
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                filename = f"{get_size(file.file_size)} {file.file_name}"
                btn.append(
                    [InlineKeyboardButton(text=f"{filename}", callback_data=f"lucifermoringstar_robot#{file_id}")]
                )
        else:
            LuciferMoringstar=await client.send_message(
                chat_id = message.chat.id,
                text=f"""നിങ്ങൾ ആവശ്യപ്പെട്ട {search} എന്ന സിനിമ മലയാളത്തിലേക്ക് മൊഴിമാറ്റം ചെയ്തിട്ടില്ല""",
                parse_mode="html",
                reply_to_message_id=message.message_id
                )
            await asyncio.sleep(30) # in seconds
            await LuciferMoringstar.delete()
            return
        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="📃 Pages 1/1",callback_data="pages"),
                 InlineKeyboardButton("Close 🗑️", callback_data="close")]
            )
            buttons.append(
                [InlineKeyboardButton(text="🤖 CHECK MY PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
            )

            dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=LuciferMoringstar.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=message.chat.title), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")
            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="Next Page ➡",callback_data=f"nextgroup_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"📃 Pages 1/{data['total']}",callback_data="pages"),
             InlineKeyboardButton("Close 🗑️", callback_data="close")]
        )
        buttons.append(
            [InlineKeyboardButton(text="🤖 CHECK MY PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
        )

        dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=LuciferMoringstar.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=message.chat.title), reply_markup=InlineKeyboardMarkup(buttons))
        await asyncio.sleep(1000)
        await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")



# ---------- Bot PM ---------- #



#@LuciferMoringstar_Robot.on_message(Worker.text & Worker.private & Worker.incoming & Worker.chat(AUTH_GROUPS) if AUTH_GROUPS else Worker.text & Worker.group & Worker.incoming)
async def pm_autofilter(client, message):
    if message.text.startswith("/"):
        return
    if FORCES_SUB:
        invite_link = await client.create_chat_invite_link(int(FORCES_SUB))
        try:
            user = await client.get_chat_member(int(FORCES_SUB), message.from_user.id)
            if user.status == "kicked":
                await client.send_message(
                    chat_id=message.from_user.id,
                    text="Sorry Sir, You are Banned to use me.",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.from_user.id,
                text="**Please Join My Updates Channel to use this Bot!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link.invite_link)
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await client.send_message(
                chat_id=message.from_user.id,
                text="Something went Wrong.",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 50:    
        btn = []
        search = message.text
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                filename = f"{get_size(file.file_size)} {file.file_name}"
                btn.append(
                    [InlineKeyboardButton(text=f"{filename}", callback_data=f"pmfile#{file_id}")]
                )
        else:
            LuciferMoringstar=await client.send_message(
                chat_id = message.chat.id,
                text=f"""നിങ്ങൾ ആവശ്യപ്പെട്ട {search} എന്ന സിനിമ മലയാളത്തിലേക്ക് മൊഴിമാറ്റം ചെയ്തിട്ടില്ല""",
                parse_mode="html",
                reply_to_message_id=message.message_id
                )
            await asyncio.sleep(30) # in seconds
            await LuciferMoringstar.delete()
            return
        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="📃 Pages 1/1",callback_data="pages"),
                 InlineKeyboardButton("Close 🗑️", callback_data="close")]
            )


            dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=LuciferMoringstar.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=bot_info.BOT_NAME), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")

            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="Next Page ➡",callback_data=f"nextgroup_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"📃 Pages 1/{data['total']}",callback_data="pages"),
             InlineKeyboardButton("Close 🗑️", callback_data="close")]
        )

      
        dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=LuciferMoringstar.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=bot_info.BOT_NAME), reply_markup=InlineKeyboardMarkup(buttons))
        await asyncio.sleep(1000)
        await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")
