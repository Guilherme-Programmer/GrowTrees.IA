import discord
from discord.ext import commands
import requests

permissão = discord.Intents.default()
permissão.message_content = True
robo = commands.Bot(command_prefix="!", intents=permissão)

def resposta():
    "araucária", "pitangueira", "ipê-roxo"

@robo.command()
async def oi(ctx):
    await ctx.send("Olá, meu nome é GrowTrees.IA! Para obter informações extras, use: (@ajuda)")
    

@robo.command()
async def ajuda(ctx):
    await ctx.send("O que você pode fazer!: 1) !curiosidades. 2) !plantio.")
    
    
@robo.command()
async def curiosidades(ctx):
    await ctx.send(input("De que árvore você quer uma curiosidade? Opções: Araucária/Pitangueira/Ipê-Roxo."))
    if resposta == "araucária":
        await ctx.send("Possui tronco reto e longo com galhos concentrados no topo, formando um desenho que lembra um guarda-chuva.")

    if resposta == "pitangueira":
        await ctx.send("Árvore de pequeno a médio porte, muito resistente ao frio do sul. Possui folhas aromáticas e produz a pitanga.")

    if resposta == "ipê-roxo":
        await ctx.send("Durante o inverno ou início da primavera, produz uma floração exuberante em tons de rosa, magenta ou roxo.")
                
        
robo.run("token")
