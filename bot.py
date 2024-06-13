import discord
from discord import app_commands
import config
import random
from datetime import timedelta

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default() )
        self.synced = False
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"Мы вошли в систему как {self.user}.")

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

@tree.command(name = "help", description = "Информация о боте")
async def self(interaction: discord.Interaction):
    embed = discord.Embed(
        colour=discord.Colour.teal(),
        description="Информация о боте находится тут: https://tptnbot.vercel.app/",
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

@tree.command(name = "afk", description = "Перейти в AFK режим")
async def self(interaction: discord.Interaction, сообщение:str):
    await interaction.response.send_message(f"{interaction.user.mention} ушел в афк: {сообщение}")

@tree.command(name = "gn", description = "Перейти в режим сна")
async def self(interaction: discord.Interaction, сообщение:str):
    await interaction.response.send_message(f"{interaction.user.mention} ушел спать: {сообщение}")

@tree.command(name = "brb", description = "Перейти в режим скоро вернусь")
async def self(interaction: discord.Interaction, сообщение:str):
    await interaction.response.send_message(f"{interaction.user.mention} скоро вернется: {сообщение}")

@tree.command(name = "poop", description = "Перейти в режим какания")
async def self(interaction: discord.Interaction, сообщение:str):
    await interaction.response.send_message(f"{interaction.user.mention} сейчас какает: {сообщение}")

@tree.command(name = "shower", description = "Перейти в режим принятия душа")
async def self(interaction: discord.Interaction, сообщение:str):
    await interaction.response.send_message(f"{interaction.user.mention} принимает душ: {сообщение}")

@tree.command(name = "food", description = "Перейти в режим приема пищи")
async def self(interaction: discord.Interaction, сообщение:str):
    await interaction.response.send_message(f"{interaction.user.mention} сейчас ест: {сообщение}")

@tree.command(name = "lurk", description = "Перейти в режим скрытности")
async def self(interaction: discord.Interaction, сообщение:str):
    await interaction.response.send_message(f"{interaction.user.mention} сейчас скрывается: {сообщение}:")

@tree.command(name = "work", description = "Перейти в рабочий режим")
async def self(interaction: discord.Interaction, сообщение:str):
    await interaction.response.send_message(f"{interaction.user.mention} работает: {сообщение}")

@tree.command(name = "study", description = "Перейти в режим обучения")
async def self(interaction: discord.Interaction, сообщение:str):
    await interaction.response.send_message(f"{interaction.user.mention} сейчас учится: {сообщение}")

@tree.command(name = "nap", description = "Перейти в режим дремоты")
async def self(interaction: discord.Interaction, сообщение:str):
    await interaction.response.send_message(f"{interaction.user.mention} сейчас дремлет: {сообщение}")

@tree.command(name = "tuck", description = "Уложить человека спать")
async def self(interaction: discord.Interaction, участник:discord.Member, *, смайлик:str):
    await interaction.response.send_message(f"Вы уложили {участник.mention} спать {смайлик} :point_right: :bed:")

@tree.command(name = "hug", description = "Обнять человека")
async def self(interaction: discord.Interaction, участник:discord.Member):
    await interaction.response.send_message(f"{interaction.user.mention} обнимает {участник.mention} :hugging:")

@tree.command(name = "clear", description = "Очистить чат")
@app_commands.default_permissions(manage_messages=True)
async def self(interaction: discord.Interaction, количество:int):
    await interaction.channel.purge(limit=количество)
    embed = discord.Embed(
    colour=discord.Colour.teal(),
    description= f":white_check_mark: Удалено **{количество}** сообщений"
)

    await interaction.response.send_message(embed=embed, ephemeral=True)

@tree.command(name = "kick", description = "Выгнать участника")
@app_commands.default_permissions(kick_members=True)
async def self(interaction: discord.Interaction, участник:discord.Member, *, причина:str):
    await участник.kick(reason=причина)
    embed = discord.Embed(
    colour=discord.Colour.teal(),
    description= f":white_check_mark: **{участник}** был выгнан по причине: `{причина}`"
)

    await interaction.response.send_message(embed=embed)

@tree.command(name = "ban", description = "Забанить участника")
@app_commands.default_permissions(ban_members=True)
async def self(interaction: discord.Interaction, участник:discord.Member, *, причина:str):
    await участник.ban(reason=причина, delete_message_days=1)
    embed = discord.Embed(
    colour=discord.Colour.teal(),
    description= f":white_check_mark: **{участник}** был забанен по причине: `{причина}`"
)

    await interaction.response.send_message(embed=embed)

@tree.command(name = "timeout", description = "Заглушить участника")
@app_commands.default_permissions(moderate_members=True)
async def self(interaction: discord.Interaction, участник:discord.Member, минуты: int, причина:str):
    delta = timedelta(minutes=минуты)
    await участник.timeout(delta, reason=причина)
    embed = discord.Embed(
    colour=discord.Colour.teal(),
    description= f":white_check_mark: **{участник}** был отправлен в мут на {минуты} минуты по причине: `{причина}`"
)

    await interaction.response.send_message(f"{участник.mention}", embed=embed)

@tree.command(name = "warn", description = "Отправить предупреждение")
@app_commands.default_permissions(moderate_members=True)
async def self(interaction: discord.Interaction, участник:discord.Member, *, причина:str):
    embed = discord.Embed(
    colour=discord.Colour.teal(),
    description= f":white_check_mark: **{участник}** получил предупреждение по причине: `{причина}`"
)

    await interaction.response.send_message(f"{участник.mention}", embed=embed)

client.run(config.TOKEN)