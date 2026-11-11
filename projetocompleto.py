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
    await ctx.send("O que você pode fazer!: 1) !curiosidade(1,2,3,4...). 2) !plantio.")
    
    
@robo.command()
async def curiosidade1(ctx):
    await ctx.send("Possui tronco reto e longo com galhos concentrados no topo, formando um desenho que lembra um guarda-chuva.")

@robo.command()
async def curiosidade2(ctx):
    await ctx.send("Árvore de pequeno a médio porte, muito resistente ao frio do sul. Possui folhas aromáticas e produz a pitanga.")
    
       
@robo.command()
async def curiosidade3(ctx):
    await ctx.send("Durante o inverno ou início da primavera, produz uma floração exuberante em tons de rosa, magenta ou roxo.")   
              
robo.command()
async def plantio(ctx):
    await ctx.send("Ao plantar uma árvore, é necessário que cave um buraco de até 0,5m no chão(dependendo da árvore) para poder plantar ela.")
    
async def regar(ctx):
    await ctx.send("É necessário regar uma árvore em fase de crescimento por até três vezes na semana (dependendo do local[se possui muito sol] e árvore).")
    
async def fruto(ctx):
    await ctx.send("Se a árvore for frutífera (pitangueira, etc), os frutos precisam estar maduros(duros), de acordo com a coloração da fruta.")
    
    
robo.run("token")
