import botpy
from botpy.types.message import Message
from botpy.audio import Audio
from model import Chat
appid = "102090954"
secret = "0aAkKuU4fGrS3eFrT5hJvXAnQ3gJwaEs"
class MyClient(botpy.Client):

    async def on_at_message_create(self, message: Message):
        await message.reply(content=f"{Chat.chat(message.content)}")
        #await message.reply(content=f"机器人{self.robot.name}收到你的@消息了: {message.content}")
intents = botpy.Intents(public_guild_messages=True, direct_message=True, guilds=True,audio_action=True)
client = MyClient(intents=intents)
client.run(appid="102090954", secret="0aAkKuU4fGrS3eFrT5hJvXAnQ3gJwaEs")
