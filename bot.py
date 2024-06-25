# Импорт библиотек
import discord
from discord import app_commands
import config
import random
from datetime import timedelta

# Синхронизация команд
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all() )
        self.synced = False
    
    async def on_ready(self):
        await client.change_presence(activity=discord.Game(name="/help")) # Статус бота
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"Мы вошли в систему как {self.user}.")

# Псевдонимы терминов
client = aclient()
tree = app_commands.CommandTree(client)

# Команда /ping
@tree.command(name = "ping", description = "Проверить наличие бота в чате")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f":ping_pong: Понг! Задержка {round(client.latency * 1000)}ms")

# Команда /explosion
@tree.command(name = "explosion", description = "Взорвать Арта5507")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"**Art5507** [Explosion](https://media.discordapp.net/attachments/1234090523363377182/1245811443748704379/Clipchamp-ezgif.com-crop.gif?ex=665a1bd2&is=6658ca52&hm=bd48c30c4bcf7dfb7ed99d3f5f0529429961d564a6c97746c8ce0ee4a07c55c6&)")

# Команда /shdhdexplosion
@tree.command(name = "shdhdexplosion", description = "Взорвать ШадоуДемона")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"**ShadowDemonHD_** [Explosion](https://media.discordapp.net/attachments/1200897692134559926/1245989257978576986/ezgif-5-37728eef2d.gif?ex=665eb5ec&is=665d646c&hm=bed9fdbf9068b8278b5eb3b284dc19ff77d8127d39e422b7874146fee9b2bdcd&)")

# Команда /lon
@tree.command(name = "lon", description = "Пишет Лон ты скуф")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"**Лон** ты скуф <:GAGAGA:1247570395347816538>")

# Команда /help
@tree.command(name = "help", description = "Информация о боте")
async def self(interaction: discord.Interaction):
    embed = discord.Embed(
        colour=discord.Colour.teal(),
        description=f"## Справка Топтунового бота\n### Команды\nВведите `/`, чтобы просмотреть список команд или [просмотрите документацию](https://tptnbot.vercel.app/docs/category/%D1%82%D0%BE%D0%BF%D1%82%D1%83%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9-%D0%B1%D0%BE%D1%82).\n### Документация\nУзнайте о том, как использовать Топтунового бота на вашем сервере. [Просмотрите документацию](https://tptnbot.vercel.app/docs/category/%D1%82%D0%BE%D0%BF%D1%82%D1%83%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9-%D0%B1%D0%BE%D1%82).\n### Сервер поддержки\nУ вас возникла проблема, есть предложение или вы просто хотите получать уведомления о новых возможностях? [Вступайте в наш Discord сервер](https://discord.gg/BCp784Gr3x).",
    )
    embed.set_thumbnail(url="https://i.imgur.com/LkSe8du.jpeg")

    await interaction.response.send_message(embed=embed)

# Команда /random
@tree.command(name = "random", description = "Отправляет рандомное число")
async def self(interaction: discord.Interaction):
    random_number = random.randint(1, 999)
    await interaction.response.send_message(f"{random_number}")

# Команда /coin
@tree.command(name = "coin", description = "Орёл или решка?")
async def self(interaction: discord.Interaction):
    words_list = ["Орёл", "Решка"]
    random_word = random.choice(words_list)
    await interaction.response.send_message(f"{random_word}")

# Команда /prediction2
@tree.command(name = "prediction2", description = "Команда для Twitch прогнозов: Какое число выпадет в конце стрима? Режим 1 и 2")
async def self(interaction: discord.Interaction):
    random_number = random.randint(1, 2)
    await interaction.response.send_message(f"{random_number}")

# Команда /prediction3
@tree.command(name = "prediction3", description = "Команда для Twitch прогнозов: Какое число выпадет в конце стрима? Режим 1,2,3")
async def self(interaction: discord.Interaction):
    random_number = random.randint(1, 3)
    await interaction.response.send_message(f"{random_number}")

# Команда /afk
@tree.command(name = "afk", description = "Перейти в AFK режим")
async def self(interaction: discord.Interaction, сообщение: str = None):
    if сообщение == None:
        сообщение = "(нет сообщения)"
    await interaction.response.send_message(f"{interaction.user.mention} ушел в афк: {сообщение}")

# Команда /gn
@tree.command(name = "gn", description = "Перейти в режим сна")
async def self(interaction: discord.Interaction, сообщение: str = None):
    if сообщение == None:
        сообщение = "(нет сообщения)"
    await interaction.response.send_message(f"{interaction.user.mention} ушел спать: {сообщение}")

# Команда /brb
@tree.command(name = "brb", description = "Перейти в режим скоро вернусь")
async def self(interaction: discord.Interaction, сообщение: str = None):
    if сообщение == None:
        сообщение = "(нет сообщения)"
    await interaction.response.send_message(f"{interaction.user.mention} скоро вернется: {сообщение}")

# Команда /poop
@tree.command(name = "poop", description = "Перейти в режим какания")
async def self(interaction: discord.Interaction, сообщение: str = None):
    if сообщение == None:
        сообщение = "(нет сообщения)"
    await interaction.response.send_message(f"{interaction.user.mention} сейчас какает: {сообщение}")

# Команда /shower
@tree.command(name = "shower", description = "Перейти в режим принятия душа")
async def self(interaction: discord.Interaction, сообщение: str = None):
    if сообщение == None:
        сообщение = "(нет сообщения)"
    await interaction.response.send_message(f"{interaction.user.mention} принимает душ: {сообщение}")

# Команда /food
@tree.command(name = "food", description = "Перейти в режим приема пищи")
async def self(interaction: discord.Interaction, сообщение: str = None):
    if сообщение == None:
        сообщение = "(нет сообщения)"
    await interaction.response.send_message(f"{interaction.user.mention} сейчас ест: {сообщение}")

# Команда /lurk
@tree.command(name = "lurk", description = "Перейти в режим скрытности")
async def self(interaction: discord.Interaction, сообщение: str = None):
    if сообщение == None:
        сообщение = "(нет сообщения)"
    await interaction.response.send_message(f"{interaction.user.mention} сейчас скрывается: {сообщение}:")

# Команда /work
@tree.command(name = "work", description = "Перейти в рабочий режим")
async def self(interaction: discord.Interaction, сообщение: str = None):
    if сообщение == None:
        сообщение = "(нет сообщения)"
    await interaction.response.send_message(f"{interaction.user.mention} работает: {сообщение}")

# Команда /study
@tree.command(name = "study", description = "Перейти в режим обучения")
async def self(interaction: discord.Interaction, сообщение: str = None):
    if сообщение == None:
        сообщение = "(нет сообщения)"
    await interaction.response.send_message(f"{interaction.user.mention} сейчас учится: {сообщение}")

# Команда /nap
@tree.command(name = "nap", description = "Перейти в режим дремоты")
async def self(interaction: discord.Interaction, сообщение: str = None):
    if сообщение == None:
        сообщение = "(нет сообщения)"
    await interaction.response.send_message(f"{interaction.user.mention} сейчас дремлет: {сообщение}")

# Команда /tuck
@tree.command(name = "tuck", description = "Уложить человека спать")
async def self(interaction: discord.Interaction, участник:discord.Member, *, смайлик: str = None):
    if смайлик == None:
        смайлик = "<:Okay:1252987035539603528>"
    await interaction.response.send_message(f"Вы уложили {участник.mention} спать {смайлик} :point_right: :bed:")

# Команда /hug
@tree.command(name = "hug", description = "Обнять человека")
async def self(interaction: discord.Interaction, участник:discord.Member):
    await interaction.response.send_message(f"{interaction.user.mention} обнимает {участник.mention} :hugging:")

# Команда /clear
@tree.command(name = "clear", description = "Очистить чат")
@app_commands.default_permissions(manage_messages=True)
async def self(interaction: discord.Interaction, количество:int):
    await interaction.channel.purge(limit=количество)
    embed = discord.Embed(
        colour=discord.Colour.teal(),
        description= f":white_check_mark: Удалено **{количество}** сообщений"
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)

# Команда /kick
@tree.command(name = "kick", description = "Выгнать участника")
@app_commands.default_permissions(kick_members=True)
async def self(interaction: discord.Interaction, участник:discord.Member, *, причина:str):
    await участник.kick(reason=причина)
    embed1 = discord.Embed(
        colour=discord.Colour.teal(),
        description= f":white_check_mark: **{участник}** был выгнан по причине: `{причина}`"
    )
    guild_name = interaction.guild.name
    embed2 = discord.Embed(
        colour=discord.Colour.teal(),
        description= f":door: Вы были изгнаны из сервера **{guild_name}** по причине: `{причина}`"
    )

    await interaction.response.send_message(embed=embed1)
    await участник.send(embed=embed2)

# Команда /ban
@tree.command(name = "ban", description = "Забанить участника")
@app_commands.default_permissions(ban_members=True)
async def self(interaction: discord.Interaction, участник:discord.Member, *, причина:str):
    await участник.ban(reason=причина, delete_message_days=1)
    embed1 = discord.Embed(
        colour=discord.Colour.teal(),
        description= f":white_check_mark: **{участник}** был забанен по причине: `{причина}`"
    )
    guild_name = interaction.guild.name
    embed2 = discord.Embed(
        colour=discord.Colour.teal(),
        description= f":no_entry_sign: Вы были забанены на сервере **{guild_name}** по причине: `{причина}`"
    )

    await interaction.response.send_message(embed=embed1)
    await участник.send(embed=embed2)

# Команда /timeout
@tree.command(name = "timeout", description = "Заглушить участника")
@app_commands.default_permissions(moderate_members=True)
async def self(interaction: discord.Interaction, участник:discord.Member, минуты: int, причина:str):
    delta = timedelta(minutes=минуты)
    await участник.timeout(delta, reason=причина)
    embed1 = discord.Embed(
        colour=discord.Colour.teal(),
        description= f":white_check_mark: **{участник}** был отправлен в мут на {минуты} минуты по причине: `{причина}`"
    )
    guild_name = interaction.guild.name
    embed2 = discord.Embed(
        colour=discord.Colour.teal(),
        description= f":clock1: Вы были отправлены в мут на сервере **{guild_name}** по причине: `{причина}`"
    )

    await interaction.response.send_message(embed=embed1)
    await участник.send(embed=embed2)

# Команда /warn
@tree.command(name = "warn", description = "Отправить предупреждение")
@app_commands.default_permissions(moderate_members=True)
async def self(interaction: discord.Interaction, участник:discord.Member, *, причина:str):
    embed1 = discord.Embed(
        colour=discord.Colour.teal(),
        description= f":white_check_mark: **{участник}** получил предупреждение по причине: `{причина}`"
    )
    guild_name = interaction.guild.name
    embed2 = discord.Embed(
        colour=discord.Colour.teal(),
        description= f":warning: Вы получили предупреждение на сервере **{guild_name}** по причине: `{причина}`"
    )

    await interaction.response.send_message(embed=embed1)
    await участник.send(embed=embed2)

# Авто-выдача ролей
@client.event
async def on_member_join(member=discord.Member):
    role = discord.utils.get(member.guild.roles, id=1255106807760814080) # Сервер Топтуновый бот
    await member.add_roles(role)

# Удаление сообщения и отправка другого сообщения в личные сообщения при добавлении реакции ✅ в канале ➕┃доп-функции на сервере Топтуновый бот
@client.event
async def on_reaction_add(reaction=discord.Reaction, user=discord.User):
    user2 = reaction.message.author
    embed = discord.Embed(
        colour=discord.Colour.teal(),
        description= f":white_check_mark: Ваш запрос на добавление функции подтвержден"
    )

    if reaction.emoji == "✅" and reaction.message.channel.id == 1255104075356307566:
         await reaction.message.delete()
         await user2.send(embed=embed)

# Создание новой ветки и добавление реакций 👍👎 на новые сообщения
@client.event
async def on_message(message=discord.Message):
    if message.channel.id == 1255095910916952086: # Сервер Топтуновый бот (обновления)
      await message.create_thread(name="Комментарии")
      await message.add_reaction("\U0001F44D")
      await message.add_reaction("\U0001F44E") 
    if message.channel.id == 1212026711311392809: # Сервер Топтуновое (картинки)
      await message.create_thread(name="Комментарии")
      await message.add_reaction("\U0001F44D")
      await message.add_reaction("\U0001F44E") 
    if message.channel.id == 1239197262748450908: # Сервер Топтуновое (ирл)
      await message.create_thread(name="Комментарии")
      await message.add_reaction("\U0001F44D")
      await message.add_reaction("\U0001F44E") 
    if message.channel.id == 1242114997874589817: # Сервер Топтуновое (клипы)
      await message.create_thread(name="Комментарии")
      await message.add_reaction("\U0001F44D")
      await message.add_reaction("\U0001F44E")
    if message.channel.id == 1209028289407090728: # Сервер tipo_Lon (картинки)
      await message.create_thread(name="Комментарии") 
      await message.add_reaction("\U0001F44D")
      await message.add_reaction("\U0001F44E")
    if message.channel.id == 1208879658494591027: # Сервер tipo_Lon (ирл)
      await message.create_thread(name="Комментарии")
      await message.add_reaction("\U0001F44D")
      await message.add_reaction("\U0001F44E")
    if message.channel.id == 1208840805205414019: # Сервер tipo_Lon (творчество)
      await message.create_thread(name="Комментарии")
      await message.add_reaction("\U0001F44D")
      await message.add_reaction("\U0001F44E")
    if message.channel.id == 1208840805205414018: # Сервер tipo_Lon (музыка)
      await message.create_thread(name="Комментарии")
      await message.add_reaction("\U0001F44D")
      await message.add_reaction("\U0001F44E")

# Запуск бота
client.run(config.TOKEN)