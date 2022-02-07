from pyrogram import Client as LuciferMoringstar_Robot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserIsBlocked, PeerIdInvalid
from LuciferMoringstar_Robot.database.autofilter_db import is_subscribed, get_file_details
from LuciferMoringstar_Robot.database._utils import get_size
from translation import LuciferMoringstar
from config import BUTTONS, FORCES_SUB, CUSTOM_FILE_CAPTION, START_MSG, DEV_NAME, bot_info, ADMINS


@LuciferMoringstar_Robot.on_callback_query()
async def cb_handler(client: LuciferMoringstar_Robot, query):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id
        pass
    if (clicked == typed):


# ---------- 🔘 [ | 𝗚𝗥𝗢𝗨𝗣 𝗙𝗜𝗟𝗧𝗘𝗥𝗦 | ] 🔘 ---------- #

        if query.data.startswith("nextgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🤖 CHECK MY PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backgroup_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🤖 CHECK MY PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🤖 CHECK MY PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )
                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backgroup_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🤖 CHECK MY PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# ---------- 🔘 [ | 𝗕𝗢𝗧 𝗣𝗠 𝗙𝗜𝗟𝗧𝗘𝗥𝗦 | ] 🔘 ---------- #


        elif query.data.startswith("nextbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backbot_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backbot_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backbot_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# ---------- 📁 [ | 𝗚𝗘𝗧 𝗙𝗜𝗟𝗘𝗦 | ] 📁 ---------- #


        elif query.data.startswith("lucifermoringstar_robot"):
            ident, file_id = query.data.split("#")
            files_ = await get_file_details(file_id)
            if not files_:
                return await query.answer('No such file exist.')
            files = files_[0]
            title = files.file_name
            size=get_size(files.file_size)
            f_caption=files.caption
            if CUSTOM_FILE_CAPTION:
                try:
                    f_caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, file_name=title, file_size=size, file_caption=f_caption)
                except Exception as e:
                        print(e)
                f_caption=f_caption
            if f_caption is None:
                f_caption = LuciferMoringstar.FILE_CAPTIONS.format(mention=query.from_user.mention, title=title, size=size)
            
            try:
                if FORCES_SUB and not await is_subscribed(client, query):
                    await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
                    return
                else:
                    SHARE_LINK = "https://t.me/share/url?url=%E0%B4%A8%E0%B4%AE%E0%B4%B8%E0%B5%8D%E0%B4%95%E0%B4%BE%E0%B4%B0%E0%B4%82%20%E0%B4%8E%E0%B4%B2%E0%B5%8D%E0%B4%B2%E0%B4%BE%E0%B4%B5%E0%B5%BC%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%81%E0%B4%82%20%E0%B4%B8%E0%B5%81%E0%B4%96%E0%B4%AE%E0%B4%BE%E0%B4%A3%E0%B5%8B%3F%0A%0A%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%B1%E0%B5%86%20%E0%B4%AA%E0%B5%87%E0%B4%B0%E0%B5%8D%20Ghost%20Rider%0A%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%B1%E0%B5%86%20TG%20Username%20%40GhostRider_Robot%0A%E0%B4%A8%E0%B4%BF%E0%B4%99%E0%B5%8D%E0%B4%99%E0%B5%BE%20%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%B1%E0%B5%86%20%20PM%E0%B5%BD%20%E0%B4%B5%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%8D%20%E0%B4%A8%E0%B4%BF%E0%B4%99%E0%B5%8D%E0%B4%99%E0%B5%BE%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%8D%20%E0%B4%86%E0%B4%B5%E0%B4%B6%E0%B5%8D%E0%B4%AF%E0%B4%AE%E0%B5%81%E0%B4%B3%E0%B5%8D%E0%B4%B3%20%E0%B4%AE%E0%B4%B2%E0%B4%AF%E0%B4%BE%E0%B4%B3%E0%B4%82%20%E0%B4%A1%E0%B4%AC%E0%B5%8D%E0%B4%AC%E0%B5%8D%20%E0%B4%9A%E0%B5%86%E0%B4%AF%E0%B5%8D%E0%B4%A4%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%E0%B4%AF%E0%B5%81%E0%B4%9F%E0%B5%86%20%E0%B4%AA%E0%B5%87%E0%B4%B0%E0%B5%8D%20%E0%B4%9F%E0%B5%88%E0%B4%AA%E0%B5%8D%E0%B4%AA%E0%B5%8D%20%E0%B4%9A%E0%B5%86%E0%B4%AF%E0%B5%8D%E0%B4%A4%E0%B4%BE%E0%B5%BD%2C%20%E0%B4%9E%E0%B4%BE%E0%B5%BB%20%E0%B4%86%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%20%E0%B4%89%E0%B4%A3%E0%B5%8D%E0%B4%9F%E0%B4%95%E0%B4%BF%E0%B5%BD%20%E0%B4%A4%E0%B5%87%E0%B4%B0%E0%B5%81%E0%B4%82...%21%0A%0A%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%8D%20Ghost%20Rider%20Robot"
                    buttons = [[
                      InlineKeyboardButton("ഷെയർ", url=SHARE_LINK)
                      ],[
                      InlineKeyboardButton('🧑‍💻 How To Own 🧑‍💻', url='https://t.me/Mo_Tech_Group')
                      ]]
                    await client.send_cached_media(
                        chat_id=query.from_user.id,
                        file_id=file_id,
                        caption=LuciferMoringstar.FILE_CAPTIONS.format(mention=query.from_user.mention, title=title, size=size),
                        reply_markup=InlineKeyboardMarkup(buttons)
                        )
                    await query.answer('🤖 Check PM, I have Sent Files In Pm 🤖',show_alert = True)
            except UserIsBlocked:
                await query.answer('Unblock the bot mahn !',show_alert = True)
            except PeerIdInvalid:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
            except Exception as e:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")

# ---------- 📁 [ | 𝗣𝗠 𝗙𝗜𝗟𝗘𝗦 | ] 📁 ---------- #

        elif query.data.startswith("pmfile"):
            if FORCES_SUB and not await is_subscribed(client, query):
                await query.answer("I Like Your Smartness, But Don't Be Oversmart 😒",show_alert=True)
                return
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=files.file_size
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, title=title, size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = LuciferMoringstar.FILE_ക്യാപ്ഷൻസ്
                SHARE_LINK = "https://t.me/share/url?url=%E0%B4%A8%E0%B4%AE%E0%B4%B8%E0%B5%8D%E0%B4%95%E0%B4%BE%E0%B4%B0%E0%B4%82%20%E0%B4%8E%E0%B4%B2%E0%B5%8D%E0%B4%B2%E0%B4%BE%E0%B4%B5%E0%B5%BC%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%81%E0%B4%82%20%E0%B4%B8%E0%B5%81%E0%B4%96%E0%B4%AE%E0%B4%BE%E0%B4%A3%E0%B5%8B%3F%0A%0A%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%B1%E0%B5%86%20%E0%B4%AA%E0%B5%87%E0%B4%B0%E0%B5%8D%20Ghost%20Rider%0A%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%B1%E0%B5%86%20TG%20Username%20%40GhostRider_Robot%0A%E0%B4%A8%E0%B4%BF%E0%B4%99%E0%B5%8D%E0%B4%99%E0%B5%BE%20%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%B1%E0%B5%86%20%20PM%E0%B5%BD%20%E0%B4%B5%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%8D%20%E0%B4%A8%E0%B4%BF%E0%B4%99%E0%B5%8D%E0%B4%99%E0%B5%BE%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%8D%20%E0%B4%86%E0%B4%B5%E0%B4%B6%E0%B5%8D%E0%B4%AF%E0%B4%AE%E0%B5%81%E0%B4%B3%E0%B5%8D%E0%B4%B3%20%E0%B4%AE%E0%B4%B2%E0%B4%AF%E0%B4%BE%E0%B4%B3%E0%B4%82%20%E0%B4%A1%E0%B4%AC%E0%B5%8D%E0%B4%AC%E0%B5%8D%20%E0%B4%9A%E0%B5%86%E0%B4%AF%E0%B5%8D%E0%B4%A4%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%E0%B4%AF%E0%B5%81%E0%B4%9F%E0%B5%86%20%E0%B4%AA%E0%B5%87%E0%B4%B0%E0%B5%8D%20%E0%B4%9F%E0%B5%88%E0%B4%AA%E0%B5%8D%E0%B4%AA%E0%B5%8D%20%E0%B4%9A%E0%B5%86%E0%B4%AF%E0%B5%8D%E0%B4%A4%E0%B4%BE%E0%B5%BD%2C%20%E0%B4%9E%E0%B4%BE%E0%B5%BB%20%E0%B4%86%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%20%E0%B4%89%E0%B4%A3%E0%B5%8D%E0%B4%9F%E0%B4%95%E0%B4%BF%E0%B5%BD%20%E0%B4%A4%E0%B5%87%E0%B4%B0%E0%B5%81%E0%B4%82...%21%0A%0A%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%8D%20Ghost%20Rider%20Robot"
                buttons = [[
                  InlineKeyboardButton("ഷെയർ", url=SHARE_LINK)
                  ],[
                  InlineKeyboardButton('🧑‍💻 How To Own 🧑‍💻', url='https://t.me/Mo_Tech_Group')
                  ]]                 
                
                await query.answer()
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=LuciferMoringstar.FILE_CAPTIONS.format(mention=query.from_user.mention, title=title, file_size=size),
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )


# ---------- 📁 [ | 𝗠𝗢𝗗𝗨𝗟𝗘𝗦 | ] 📁 ---------- #


        elif query.data == "start":
            if query.from_user.id not in ADMINS: 
                buttons = [[
                 InlineKeyboardButton("➕️ Add me to Your Chat ➕️", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
                 ],[
                 InlineKeyboardButton("ℹ️ നോട്ടീസ്സ്", callback_data="help"),
                 InlineKeyboardButton("😎 എബൌട്ട്‌", callback_data="about") 
                 ],[
                 InlineKeyboardButton("🗳 Deploy", url="https://youtu.be/FCU_XJmyG_U"),
                 InlineKeyboardButton("🤖 Update", url="https://t.me/Mo_Tech_Group")
                 ]]
            else:
                buttons = [[
                 InlineKeyboardButton("➕️ Add me to Your Chat ➕️", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
                 ],[
                 InlineKeyboardButton("ℹ️ നോട്ടീസ്സ്", callback_data="bot_owner"),
                 InlineKeyboardButton("😎 എബൌട്ട്‌", callback_data="about") 
                 ],[
                 InlineKeyboardButton("🗳 ഡെപ്ലോയ്", url="https://youtu.be/FCU_XJmyG_U"),
                 InlineKeyboardButton("🤖 അപ്ഡേറ്റ്", url="https://t.me/Mo_Tech_Group")
                 ]]               
            await query.message.edit(text=START_MSG.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "help":
            buttons = [[
              InlineKeyboardButton("🔔 Enable Notification 🔔", url="https://t.me/GhostRider_Updates")
              ],[
              InlineKeyboardButton("🏠 ഹോം", callback_data="start"),
              InlineKeyboardButton("എബൌട്ട്‌ 😎", callback_data="about")
              ]]               
            await query.message.edit(text=LuciferMoringstar.HELP_MSG.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "about":
            buttons = [[
             InlineKeyboardButton("🏠 ഹോം", callback_data="start"),
             InlineKeyboardButton("ക്ലോസ് 🗑️", callback_data="close")
             ]]               
            await query.message.edit(text=LuciferMoringstar.ABOUT_MSG.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "bot_owner":
            buttons = [[
             InlineKeyboardButton('🏠 Home', callback_data="start"),
             InlineKeyboardButton('About 😎', callback_data="about")
             ]]               
            await query.message.edit(text=LuciferMoringstar.PR0FESS0R_99.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "pages":
            await query.answer()

    else:
        await query.answer("Please Request",show_alert=True)




