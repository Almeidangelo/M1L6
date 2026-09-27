import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Você logou como {bot.user}')

@bot.command()
async def dica1(ctx):
    await ctx.send("Para poder reduzir a quantidade de lixo que você produz, uma boa dica é pensar: O que são coisas em qual eu exagero? Se você tiver um carro para ir trabalhar, mas vive pertinho, optar por uma alternativa como uma bicicleta não seria má ideia! ")

@bot.command()
async def dica2(ctx):
    await ctx.send("Outra dica é comprar produtos mais ecológicos. Por exemplo, embalagens recicláveis(hoje em dia quase todas são) ou comidas mais naturais.")

@bot.command()
async def dica3(ctx):
    await ctx.send("Uma terceira dica é reutilizar coisas que você já tem. Por exemplo, se você tem uma camisa que não cabe mais em você , você pode dar ela para seus filhos ou outras pessoas menores que você conhece.")
bot.run("Seu token aqui!")
