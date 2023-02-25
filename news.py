from telethon import TelegramClient, events
from telethon import errors
import asyncio

# ----
api_id = 22176825
api_hash = "69f074b42d7e6ebb93230e8bbcfbe3e3"
# ----
channels = ['@cosplay_nudes' , "@coospart"  , "@Cosplay_18s" , "@fgfgdfgfdgdfg" , "@anicosplay"]# откуда
my_channel = '@cosplay_patreon'  # куда
# -----
KEYS = {

}
# ----
Bad_Keys = []
# ----
tags = ''
# добавление текста к посту, если не надо оставить ковычки пустыми ""
# ----
with TelegramClient('myApp13', api_id, api_hash) as client:
    print("～Activated～")

    @client.on(events.Album(chats=channels))
    async def Album(event):
        text = event.original_update.message.message
        print(text)
        if not [element for element in Bad_Keys
                if text.lower().__contains__(element)]:
            for i in KEYS:
                text = re.sub(i, KEYS[i], text)
            try:
                await client.send_message(
                    entity=my_channel,
                    file=event.messages,
                    message=text + tags,
                    parse_mode='md',
                    link_preview=False)
            except errors.FloodWaitError as e:
                print(f'[!] Ошибка флуда ждем: {e.seconds} секунд')
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print('[!] Ошибка', e)

    client.run_until_disconnected()
