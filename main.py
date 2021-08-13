import os
import time
import os.path
import discord
from discord.ext import commands
import pafy 
import youtube_dl
import contextlib
import pyshorteners
from flask import Flask
from keep_alive import keep_alive
from discord.ext.commands import Bot
import asyncio

my_secret1 = os.environ['tokenbitly']
my_secret2 = os.environ['token']

Client = commands.Bot(command_prefix='!')

@Client.event
async def on_ready():
    print("we have logged in as {0.user}".format(Client))\
  

@Client.command()
async def downloadlink(ctx, url):
  print('user requested download link')
  video = pafy.new(url) 
  if video.length > 360:
    await ctx.send('requested file too big')
    return
  await ctx.send("{}'s requested file is being processed please wait.....".format(ctx.message.author))
  audiostreams = video.audiostreams
  Url = audiostreams[3].url_https
  s = pyshorteners.Shortener(api_key=my_secret1)
  video_link = s.bitly.short(Url)
  await ctx.send(" {} \nVideos from certain Artists might be not accessible due to copyright laws".format(video_link))

@Client.command()
async def downloadmp4(ctx, url):
  await ctx.send("{}'s requested file is being processed please wait.....".format(ctx.message.author))
  print('user requested mp4 file')
  video = pafy.new(url)
  if video.length > 360:
    await ctx.send('requested file too big')
    return
  await ctx.send("{}'s requested file is being processed please wait.....".format(ctx.message.author))
  videostreams = video.videostreams
  mp4 = videostreams[3].download(filepath = ('{}.mp4'.format(video.title)))
  while not os.path.exists('{}.mp4'.format(video.title)):
      time.sleep(1)

  if os.path.exists('{}.mp4'.format(video.title)):
    print("file downloaded")
    await ctx.send(file=discord.File(r'{}.mp4'.format(video.title)))
    os.remove('{}.mp4'.format(video.title))

@Client.command()
async def download(ctx, url):
  print('user requested mp3 file')
  video = pafy.new(url)
  if video.length > 360:
    await ctx.send('requested file too big')
    return
  await ctx.send("{}'s requested file is being processed please wait.....".format(ctx.message.author))
  audiostreams = video.audiostreams
  mp4 = audiostreams[3].download(filepath = ('{}.mp3'.format(video.title)))
  while not os.path.exists('{}.mp3'.format(video.title)):
      time.sleep(1)

  if os.path.exists('{}.mp3'.format(video.title)):
    print("file downloaded")
    await ctx.send(file=discord.File(r'{}.mp3'.format(video.title)))
    os.remove('{}.mp3'.format(video.title))
    return



#keeping the bot online

keep_alive()
Client.run(my_secret2)