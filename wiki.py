#!/usr/bin/env python3
import discord
from discord import app_commands
import feedparser
import datetime
from discord.ext import tasks
import asyncio

TOKEN =  "XXXXXXXXX"##botのTOKENを載せる
RSS_URL = 'XXX'##登録したいRSSファイルのリンクを書き込み

intents=discord.Intents.none()
intents.reactions = True
intents.guilds = True
# discord.py Ver2.0 以降は必要
#intent.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました',discord.__version__)
    await client.change_presence(activity=discord.Game(name="おねんね", type=1))
    wiki_check.start()

@tasks.loop(minutes=10)##10分毎に確認する場合。間隔を短くしても良い
async def wiki_check():
    wiki_channel_ID = client.get_channel(XXXXX)##投稿したいチャンネルのIDを送信
    #最終確認時刻を更新する
    txt = []
    with open('log/wikilog.txt', encoding='UTF-8') as f:##24時間ログイン出来ない時に新しいファイルを作成
        for line in f:
           txt.append(line)
    dte = datetime.datetime.strptime(txt[1], '%Y-%m-%d %H:%M:%S.%f')
    dt_now = datetime.datetime.now()
    print(dt_now,dte)
    g = open('log/wikilog.txt', 'w')##最終確認時間を更新
    g.write(txt[0]+str(dt_now))


    d = feedparser.parse(RSS_URL)
    for entry in d.entries:
        time = entry.description
        time_mod = datetime.datetime.strptime(time, "%a, %d %b %Y %X JST")
#        print(entry.title, entry.link,time_mod)
        if dte < time_mod:
            print(dt_now,time_mod,entry.title)
            await wiki_channel_ID.send(
                str(time_mod)+"に「"+entry.title.replace("_","\\_")+"」が編集されました。\n"+entry.link
                )

client.run(TOKEN)
quit()


