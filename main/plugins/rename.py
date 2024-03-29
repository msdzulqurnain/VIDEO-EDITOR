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

import os, time, requests

from datetime import datetime as dt
from telethon import events
from telethon.tl.types import DocumentAttributeVideo
from ethon.telefunc import fast_download, fast_upload
from ethon.pyutils import rename
from ethon.pyfunc import video_metadata

from .. import MSDZULQURNAIN, BOT_UN, MONGODB_URI

from main.Database.database import Database
from LOCAL.localisation import JPG3 as t
from LOCAL.localisation import admz, SUPPORT_LINK

async def media_rename(event, msg, new_name):
    edit = await event.client.send_message(event.chat_id, 'Sedang mengubah nama...', reply_to=msg.id)
    db = Database(MONGODB_URI, 'videoconvertor')
    T = await db.get_thumb(event.sender_id)
    if T is not None:
        ext = T.split("/")[4]
        r = requests.get(T, allow_redirects=True)
        path = dt.now().isoformat("_", "seconds") + ext
        open(path , 'wb').write(r.content)
        THUMB = path
    else:
        THUMB = t
    MSDZULQURNAIN = event.client
    DT = time.time()
    if hasattr(msg.media, "document"):
        file = msg.media.document
    else:
        file = msg.media
    mime = msg.file.mime_type
    if 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
        out = new_name + ".mp4"
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
        out = new_name + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
        out = new_name + ".mkv"            
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm" 
        out = new_name + ".webm"
    elif 'zip' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".zip" 
        out = new_name + ".zip"            
    elif 'jpg' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".jpg" 
        out = new_name + ".jpg"
    elif 'png' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".png"
        out = new_name + ".png"
    elif 'pdf' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".pdf" 
        out = new_name + ".pdf"
    elif 'rar' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".rar"
        out = new_name + ".rar"
    elif 'mp3' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp3" 
        out = new_name + ".mp3"
    elif 'ogg' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".ogg" 
        out = new_name + ".ogg"          
    elif 'flac' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".flac"  
        out = new_name + ".flac"
    elif 'wav' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".wav" 
        out = new_name + ".wav"
    elif 'webp' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webp" 
        out = new_name + ".webp"
    else:
        default_name = msg.file.name
        if not default_name:
            await edit.edit("Gagal mengambil ekstensi file Anda!")
        else:
            try:
                name = msg.file.name
                ext = (name.split("."))[1]
                out = new_name + "." + ext
                await fast_download(name, file, MSDZULQURNAIN, edit, DT, "**MENDOWNLOAD:**")
                rename(name, out)
                UT = time.time()
                uploader = await fast_upload(out, out, UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
                net_time = round(DT - UT)
                await MSDZULQURNAIN.send_file(event.chat_id, uploader, caption=f"TELAH TERUBAH NAMA dari : @{BOT_UN}\nTotal waktu:{net_time} detik\n\n Owner : {admz}👤", thumb=THUMB, force_document=True)
            except Exception as e:
                await edit.edit(f"Terjadi kesalahan saat mengupload!\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
                print(e)
                return
    try:  
        await fast_download(name, file, MSDZULQURNAIN, edit, DT, "**MENDOWNLOAD:**")
    except Exception as e:
        await edit.edit(f"Terjadi kesalahan saat mendownload!\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        print(e)
        return
    await edit.edit("Sedang mengubah nama...")
    try:
        rename(name, out)
    except Exception as e:
        await edit.edit(f"Terjadi kesalahan saat mengubah nama!\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        print(e)
        return
    try:
        if not 'video' in mime:
            UT = time.time()
            uploader = await fast_upload(out, out, UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
            net_time = round(DT - UT)
            await MSDZULQURNAIN.send_file(event.chat_id, uploader, caption=f"TELAH TERUBAH NAMA dari: @{BOT_UN}\nTotal waktu:{net_time} detik\n\n Owner : {admz}👤", thumb=THUMB, force_document=True)
        else:
            if 'mp4' in mime:
                metadata = video_metadata(out)
                width = metadata["width"]
                height = metadata["height"]
                duration = metadata["duration"]
                attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
                UT = time.time()
                uploader = await fast_upload(f'{out}', f'{out}', UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
                net_time = round(DT - UT)
                await MSDZULQURNAIN.send_file(event.chat_id, uploader, caption=f"TELAH TERUBAH NAMA dari: @{BOT_UN}\nTotal waktu:{net_time} detik\n\n Owner : {admz}👤", thumb=THUMB, attributes=attributes, force_document=False)
            elif msg.video:
                metadata = video_metadata(out)
                width = metadata["width"]
                height = metadata["height"]
                duration = metadata["duration"]
                attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
                UT = time.time()
                uploader = await fast_upload(f'{out}', f'{out}', UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
                net_time = round(DT - UT)
                await MSDZULQURNAIN.send_file(event.chat_id, uploader, caption=f"TELAH TERUBAH NAMA dari: @{BOT_UN}\nTotal waktu:{net_time} detik\n\n Owner : {admz}👤", thumb=THUMB, attributes=attributes, force_document=False)            
            else:
                UT = time.time()
                uploader = await fast_upload(out, out, UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
                net_time = round(DT - UT)
                await MSDZULQURNAIN.send_file(event.chat_id, uploader, caption=f"TELAH TERUBAH NAMA dari: @{BOT_UN}\nTotal waktu:{net_time} detik\n\n Owner : {admz}👤", thumb=THUMB, force_document=True)
    except Exception as e:
        await edit.edit(f"Terjadi kesalahan saat mengupload!\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        print(e)
        return
    await edit.delete()
    os.remove(out)
