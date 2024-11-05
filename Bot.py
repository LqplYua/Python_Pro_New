import discord
from discord.ext import commands
import random
import requests

import os
files = os.listdir('img')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def mem(ctx):
    with open('img/meme_2.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def meme(ctx):
    img = random.choice(files)
    with open(f'img/{img}', 'rb') as f:
        picture = discord.File(f)
        
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def reduce_waste(ctx):
    """Fungsi untuk menjelaskan bagaimana kita bisa mengurangi sampah dalam kehidupan sehari-hari dan kode."""
    await ctx.send("Ada beberapa cara untuk mengurangi sampah dalam kehidupan kita dan kode:")
    await ctx.send("- **Mengurangi penggunaan barang sekali pakai**: Gunakan barang yang tahan lama dan bisa dipakai berulang kali.")
    await ctx.send("- **Mendaur ulang**: Pastikan sampah yang dapat didaur ulang diproses kembali untuk mengurangi tumpukan sampah.")

@bot.command()
async def jenis_sampah(ctx):
    with open('IMG/jenis-sampah.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

bot.run("GUNAKAN CODE BOT MU")
