#  This file is part of the VIDEOconvertor distribution.
#  Copyright (c) 2021 vasusen-code ; All rights reserved. 
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License for more details.
#
#  License can be found in < https://github.com/vasusen-code/VIDEOconvertor/blob/public/LICENSE> .

from telethon import events, Button
from decouple import config

from .. import MSDZULQURNAIN, AUTH_USERS, MONGODB_URI

from main.Database.database import Database

#Database command handling--------------------------------------------------------------------------

db = Database(MONGODB_URI, 'videoconvertor')

@MSDZULQURNAIN.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def incomming(event):
    if not await db.is_user_exist(event.sender_id):
        await db.add_user(event.sender_id)

@MSDZULQURNAIN.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="/pengguna"))
async def pengguna(event):
    xx = await event.reply("Menghitung total pengguna di Database...")
    x = await db.total_users_count()
    await xx.edit(f"Total pengguna(s) {int(x)}")

@MSDZULQURNAIN.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="/broadcast"))
async def broadcast(event):
    ids = []
    msg = await event.get_reply_message()
    if not msg:
        await event.reply("reply pesan untuk broadcast!")
    xx = await event.reply("Menghitung total pengguna di Database...")
    x = await db.total_users_count()
    await xx.edit(f"Total pengguna(s) {int(x)}")
    all_users = await db.get_users()
    sent = []
    failed = []
    async for user in all_users:
        user_id = user.get("id", None) 
        ids.append(user_id)
    for id in ids:
        try:
            try:
                await event.client.send_message(int(id), msg)
                sent.append(id)
                await xx.edit(f"Total pengguna : {x}", 
                             buttons=[
                                 [Button.inline(f"TERKIRIM: {len(sent)}", data="none")],
                                 [Button.inline(f"GAGAL: {len(failed)}", data="none")]])
                await asyncio.sleep(1)
            except FloodWaitError as fw:
                await asyncio.sleep(fw.seconds + 10)
                await event.client.send_message(int(id), msg)
                sent.append(id)
                await xx.edit(f"Total pengguna : {x}", 
                             buttons=[
                                [Button.inline(f"TERKIRIM: {len(sent)}", data="none")],
                                [Button.inline(f"GAGAL: {len(failed)}", data="none")]])
                await asyncio.sleep(1)
        except Exception:
            failed.append(id)
            await xx.edit(f"Total pengguna : {x}", 
                             buttons=[
                                 [Button.inline(f"TERKIRIM: {len(sent)}", data="none")],
                                 [Button.inline(f"GAGAL: {len(failed)}", data="none")]])
    await xx.edit(f"Broadcast selesai:v\n\nTotal pengguna di Database: {x}", 
                 buttons=[
                     [Button.inline(f"TERKIRIM: {len(sent)}", data="none")],
                     [Button.inline(f"GAGAL: {len(failed)}", data="none")]])
    
    
@MSDZULQURNAIN.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="^/banned (.*)" ))
async def banned(event):
    c = event.pattern_match.group(1)
    if not c:
        await event.reply("Banned siapa!?")
    AUTH = config("AUTH_USERS", default=None)
    admins = []
    admins.append(f'{int(AUTH)}')
    if c in admins:
        return await event.reply("Saya tidak bisa banned AUTH_USER")
    xx = await db.is_banned(int(c))
    if xx is True:
        return await event.reply("Pengguna telah dibanned!")
    else:
        await db.banning(int(c))
        await event.reply(f"{c} sekarang dibanned")
    admins.remove(f'{int(AUTH)}')
    
@MSDZULQURNAIN.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="^/unbanned (.*)" ))
async def unbanned(event):
    xx = event.pattern_match.group(1)
    if not xx:
        await event.reply("Unbanned siapa?")
    xy = await db.is_banned(int(xx))
    if xy is False:
        return await event.reply("Pengguna telah bebas!")
    await db.unbanning(int(xx))
    await event.reply(f"{xx} Bebas! ")
    

    


   
    
