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

import os, subprocess, time

from datetime import datetime as dt
from telethon import events
from telethon.tl.types import DocumentAttributeVideo
from ethon.telefunc import fast_download, fast_upload
from ethon.pyfunc import bash, video_metadata
from ethon.pyutils import rename

from .. import BOT_UN

from LOCAL.localisation import admz, SUPPORT_LINK, JPG, JPG2

async def mp3(event, msg):
    MSDZULQURNAIN = event.client
    edit = await MSDZULQURNAIN.send_message(event.chat_id, "Sedang mengconvert...", reply_to=msg.id)
    if hasattr(msg.media, "document"):
        file = msg.media.document
    else:
        file = msg.media
    x = msg.file.name
    mime = msg.file.mime_type
    if x:
        name = msg.file.name
    elif 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm"      
    if x:
        out = ((msg.file.name).split("."))[0]
    else:
        out = dt.now().isoformat("_", "seconds")
    try:
        DT = time.time()
        await fast_download(name, file, MSDZULQURNAIN, edit, DT, "**MENDOWNLOAD:**")
    except Exception as e:
        os.rmdir("audioconvert")
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mendownload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        await edit.edit("Converting.")
        bash(f"ffmpeg -i {name} -codec:a libmp3lame -q:a 0 {out}.mp3")
    except Exception as e:
        os.rmdir("audioconvert")
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengconvert!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        UT = time.time()
        uploader = await fast_upload(f'{out}.mp3', f'{out}.mp3', UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
        await MSDZULQURNAIN.send_file(event.chat_id, uploader, thumb=JPG, caption=f'AUDIO TERCONVERT dari: @{BOT_UN}\n\n Owner : {admz}👤', force_document=True)
    except Exception as e:
        os.rmdir("audioconvert")
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengupload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    await edit.delete()
    os.remove(name)
    os.remove(f'{out}.mp3')                           
                       
async def flac(event, msg):
    MSDZULQURNAIN = event.client
    edit = await MSDZULQURNAIN.send_message(event.chat_id, "Sedang mengconvert...", reply_to=msg.id)
    if hasattr(msg.media, "document"):
        file = msg.media.document
    else:
        file = msg.media
    x = msg.file.name
    mime = msg.file.mime_type
    if x:
        name = msg.file.name
    elif 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm"      
    if x:
        out = ((msg.file.name).split("."))[0]
    else:
        out = dt.now().isoformat("_", "seconds")
    try:
        DT = time.time()
        await fast_download(name, file, MSDZULQURNAIN, edit, DT, "**MENDOWNLOAD:**")
    except Exception as e:
        os.rmdir("audioconvert")
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mendownload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        await edit.edit("Converting.")
        bash(f"ffmpeg -i {name} -codec:a libmp3lame -q:a 0 {out}.mp3")
        bash(f'ffmpeg -i {out}.mp3 -c:a flac {out}.flac')
    except Exception as e:
        os.rmdir("audioconvert")
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengconvert!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        UT = time.time()
        uploader = await fast_upload(f'{out}.flac', f'{out}.flac', UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
        await MSDZULQURNAIN.send_file(event.chat_id, uploader, thumb=JPG, caption=f'AUDIO TEREKSTRAK dari: @{BOT_UN}\n\n Owner : {admz}👤', force_document=True)
    except Exception as e:
        os.rmdir("audioconvert")
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengupload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    await edit.delete()
    os.remove(name)
    os.remove(f'{out}.mp3')                           
    os.remove(f'{out}.flac')                 

async def wav(event, msg):
    MSDZULQURNAIN = event.client
    edit = await MSDZULQURNAIN.send_message(event.chat_id, "Sedang mengconvert...", reply_to=msg.id)
    if hasattr(msg.media, "document"):
        file = msg.media.document
    else:
        file = msg.media
    x = msg.file.name
    mime = msg.file.mime_type
    if x:
        name = msg.file.name
    elif 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm"      
    if x:
        out = ((msg.file.name).split("."))[0]
    else:
        out = dt.now().isoformat("_", "seconds")
    try:
        DT = time.time()
        await fast_download(name, file, MSDZULQURNAIN, edit, DT, "**MENDOWNLOAD:**")
    except Exception as e:
        os.rmdir("audioconvert")
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mendownload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        await edit.edit("Converting.")
        bash(f"ffmpeg -i {name} -codec:a libmp3lame -q:a 0 {out}.mp3")
        bash(f'ffmpeg -i {out}.mp3 {out}.wav')
    except Exception as e:
        os.rmdir("audioconvert")
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengconvert!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        UT = time.time()
        uploader = await fast_upload(f'{out}.wav', f'{out}.wav', UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
        await MSDZULQURNAIN.send_file(event.chat_id, uploader, thumb=JPG, caption=f'AUDIO TEREKSTRAK dari: @{BOT_UN}\n\n Owner : {admz}👤', force_document=True)
    except Exception as e:
        os.rmdir("audioconvert")
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengupload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    await edit.delete()
    os.remove(name)
    os.remove(f'{out}.mp3')                           
    os.remove(f'{out}.wav')                 
                                       
async def mp4(event, msg):
    MSDZULQURNAIN = event.client
    edit = await MSDZULQURNAIN.send_message(event.chat_id, "Sedang mengconvert...", reply_to=msg.id)
    if hasattr(msg.media, "document"):
        file = msg.media.document
    else:
        file = msg.media
    x = msg.file.name
    mime = msg.file.mime_type
    if x:
        name = msg.file.name
    elif 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm"      
    if x:
        out = ((msg.file.name).split("."))[0] 
    else:
        out = dt.now().isoformat("_", "seconds")
    try:
        DT = time.time()
        await fast_download(name, file, MSDZULQURNAIN, edit, DT, "**MENDOWNLOAD:**")
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mendownload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        await edit.edit("Converting.")
        rename(name, f'{out}.mp4')
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengconvert!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        UT = time.time()
        uploader = await fast_upload(f'{out}.mp4', f'{out}.mp4', UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
        await MSDZULQURNAIN.send_file(event.chat_id, uploader, thumb=JPG, caption=f'TELAH TERCONVERT dari: @{BOT_UN}\n\n Owner : {admz}👤', force_document=True)
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengupload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    await edit.delete()                      
    os.remove(f'{out}.mp4')                 
                                           
async def mkv(event, msg):
    MSDZULQURNAIN = event.client
    edit = await MSDZULQURNAIN.send_message(event.chat_id, "Sedang mengconvert...", reply_to=msg.id)
    if hasattr(msg.media, "document"):
        file = msg.media.document
    else:
        file = msg.media
    x = msg.file.name
    mime = msg.file.mime_type
    if x:
        name = msg.file.name
    elif 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm"      
    if x:
        out = ((msg.file.name).split("."))[0] + ".mkv"
    else:
        out = dt.now().isoformat("_", "seconds") + ".mkv"
    try:
        DT = time.time()
        await fast_download(name, file, MSDZULQURNAIN, edit, DT, "**MENDOWNLOAD:**")
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mendownload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        await edit.edit("Converting.")
        rename(name, f'{out}')
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengconvert!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        UT = time.time()
        uploader = await fast_upload(f'{out}', f'{out}', UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
        await MSDZULQURNAIN.send_file(event.chat_id, uploader, thumb=JPG, caption=f'TELAH TERCONVERT dari: @{BOT_UN}\n\n Owner : {admz}👤', force_document=True)
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengupload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    await edit.delete()                        
    os.remove(f'{out}')
             
async def webm(event, msg):
    MSDZULQURNAIN = event.client
    edit = await MSDZULQURNAIN.send_message(event.chat_id, "Sedang mengconvert...", reply_to=msg.id)
    if hasattr(msg.media, "document"):
        file = msg.media.document
    else:
        file = msg.media
    x = msg.file.name
    mime = msg.file.mime_type
    if x:
        name = msg.file.name
    elif 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm"      
    if x:
        out = ((msg.file.name).split("."))[0] + ".webm"
    else:
        out = dt.now().isoformat("_", "seconds") + ".webm"
    try:
        DT = time.time()
        await fast_download(name, file, MSDZULQURNAIN, edit, DT, "**MENDOWNLOAD:**")
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mendownload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        await edit.edit("Converting.")
        rename(name, f'{out}')
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengconvert!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        UT = time.time()
        uploader = await fast_upload(f'{out}', f'{out}', UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
        await MSDZULQURNAIN.send_file(event.chat_id, uploader, thumb=JPG, caption=f'TELAH TERCONVERT dari: @{BOT_UN}\n\n Owner : {admz}👤', force_document=True)
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengupload\n\nContact [SUPPORT]({SUPPORT_LINK})")
    await edit.delete()                 
    os.remove(f'{out}')
             
async def file(event, msg):
    MSDZULQURNAIN = event.client
    edit = await MSDZULQURNAIN.send_message(event.chat_id, "Sedang mengconvert...", reply_to=msg.id)
    if hasattr(msg.media, "document"):
        file = msg.media.document
    else:
        file = msg.media
    x = msg.file.name
    mime = msg.file.mime_type
    if x:
        name = msg.file.name
    elif 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm"      
    try:
        DT = time.time()
        await fast_download(name, file, MSDZULQURNAIN, edit, DT, "**MENDOWNLOAD:**")
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mendownload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        UT = time.time()
        uploader = await fast_upload(f'{name}', f'{name}', UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
        await MSDZULQURNAIN.send_file(event.chat_id, uploader, thumb=JPG, caption=f'TELAH TERCONVERT dari: @{BOT_UN}\n\n Owner : {admz}👤', force_document=True)
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengupload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    await edit.delete()
    os.remove(name)                           
    
async def video(event, msg):
    MSDZULQURNAIN = event.client
    edit = await MSDZULQURNAIN.send_message(event.chat_id, "Sedang mengconvert...", reply_to=msg.id)
    if hasattr(msg.media, "document"):
        file = msg.media.document
    else:
        file = msg.media
    x = msg.file.name
    mime = msg.file.mime_type
    if x:
        name = msg.file.name
    elif 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm"      
    if x:
        out = ((msg.file.name).split("."))[0] + '.mp4'
    else:
        out = dt.now().isoformat("_", "seconds") + '.mp4'
    try:
        DT = time.time()
        await fast_download(name, file, MSDZULQURNAIN, edit, DT, "**MENDOWNLOAD:**")
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mendownload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        await edit.edit("Converting.")
        rename(name, f'{out}')
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengconvert!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    try:
        metadata = video_metadata(out)
        width = metadata["width"]
        height = metadata["height"]
        duration = metadata["duration"]
        attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]           
        UT = time.time()
        uploader = await fast_upload(f'{out}', f'{out}', UT, MSDZULQURNAIN, edit, '**MENGUPLOAD:**')
        await MSDZULQURNAIN.send_file(event.chat_id, uploader, thumb=JPG2, caption=f'*TELAH TERCONVERT dari: @{BOT_UN}\n\n Owner : {admz}👤', attributes=attributes, force_document=False)
    except Exception as e:
        print(e)
        return await edit.edit(f"Terjadi kesalahan saat mengupload!\n\nContact [SUPPORT]({SUPPORT_LINK})")
    await edit.delete()
    os.remove(out)                           
    
