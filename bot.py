from pyrogram import Client, Filters
import requests

app = Client("bot", api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e", bot_token="*")


@app.on_message(Filters.command(["start"]) & Filters.private)
def basla(client, message):
    message.reply_text("Hello {}, send photo/video/document for upload to TmpNinja.".format(message.from_user.first_name))

@app.on_message(Filters.media & Filters.private)
def yukle(client, message):
    ilk = message.reply_text("Downloading media...")
    download = message.download()
    ilk.edit_text("Media is downloaded succesfully. Uploading to TmpNinja")

    files = {
        'file': (download, open(download, 'rb')),
    }

    response = requests.post('https://tmp.ninja/api.php?d=upload-tool', files=files)
    ilk.edit_text(response.content.decode("utf-8"))

app.run()
