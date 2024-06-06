import discord
from discord import app_commands
import config
import random

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default() )
        self.synced = False
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = "ping", description = "Проверить наличие бота в чате")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f":ping_pong: Понг! Задержка {round(client.latency * 1000)}ms")

@tree.command(name = "explosion", description = "Взорвать Арта5507")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"**Art5507** [Explosion](https://media.discordapp.net/attachments/1234090523363377182/1245811443748704379/Clipchamp-ezgif.com-crop.gif?ex=665a1bd2&is=6658ca52&hm=bd48c30c4bcf7dfb7ed99d3f5f0529429961d564a6c97746c8ce0ee4a07c55c6&)")

@tree.command(name = "shdhdexplosion", description = "Взорвать ШадоуДемона")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"**ShadowDemonHD_** [Explosion](https://media.discordapp.net/attachments/1200897692134559926/1245989257978576986/ezgif-5-37728eef2d.gif?ex=665eb5ec&is=665d646c&hm=bed9fdbf9068b8278b5eb3b284dc19ff77d8127d39e422b7874146fee9b2bdcd&)")

@tree.command(name = "lon", description = "Пишет Лон ты скуф")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"**Лон** ты скуф <:GAGAGA:1247570395347816538>")

@tree.command(name = "murg", description = "Пишет Мург купи сталкер")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"**Мург** купи сталкер <:PLEASE:1246757757760180287>")

@tree.command(name = "help", description = "Информация о боте")
async def self(interaction: discord.Interaction):
    embed = discord.Embed(
        colour=discord.Colour.teal(),
        description="Информация о боте находится тут: https://bit.ly/TptnBot",
        title="Помощь"
    )

    await interaction.response.send_message(embed=embed)

@tree.command(name = "random", description = "Отправляет рандомное число")
async def self(interaction: discord.Interaction):
    random_number = random.randint(1, 999)
    await interaction.response.send_message(f"{random_number}")

@tree.command(name = "coin", description = "Орёл или решка?")
async def self(interaction: discord.Interaction):
    words_list = ["Орёл", "Решка"]
    random_word = random.choice(words_list)
    await interaction.response.send_message(f"{random_word}")

@tree.command(name = "prediction2", description = "Команда для Twitch прогнозов: Какое число выпадет в конце стрима? Режим 1 и 2")
async def self(interaction: discord.Interaction):
    random_number = random.randint(1, 2)
    await interaction.response.send_message(f"{random_number}")

@tree.command(name = "prediction3", description = "Команда для Twitch прогнозов: Какое число выпадет в конце стрима? Режим 1,2,3")
async def self(interaction: discord.Interaction):
    random_number = random.randint(1, 3)
    await interaction.response.send_message(f"{random_number}")

client.run(config.TOKEN)