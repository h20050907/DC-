#導入Discord.py
import discord
#client是我們與Discord連結的橋樑
client = discord.Client()

#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果以「歪賣」開頭
    if message.content.startswith('吃')or message.content.startswith('吃什麼')or message.content.startswith('歪賣'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("你要吃什麼啦 吃咖哩拌飯喔？")
      else:
        await message.channel.send('你要吃')
        await message.channel.send(tmp[1])
        await message.channel.send('喔 啊怎麼不吃咖哩拌飯')
    elif message.content.startswith('直播'):
        await message.channel.send("我是爆哥 我不只會直播 會吃外賣 還會跳遠和跳舞")
    elif message.content.startswith('笑死'):
        await message.channel.send("笑死")

client.run('OTA1MDY0NjA5NDE1ODM1NjY4.YYEpGg.UrJL0ywaj36g-4prOirm9TuhPH4') #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面
