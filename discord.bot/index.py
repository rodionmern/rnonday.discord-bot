import discord
import sqlite3
import asyncio

bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
	print('Ready')
	cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INT, name TEXT, reallyname TEXT, age INT, rulesaccept TEXT)""")
	await bot.change_presence(status = discord.Status.dnd, activity = discord.Activity(name = f'rodeosmith.github.io', type = discord.ActivityType.watching)) #Инфа о количестве серверов, на котором находится бот.
	await asyncio.sleep(99)
	await bot.change_presence(status = discord.Status.dnd, activity = discord.Activity(name = f'rodeosmith.github.io', type = discord.ActivityType.watching)) #Инфа о количестве серверов, на котором находится бот.
	await asyncio.sleep(99)

@bot.command(description="This command allows you to see if you have ping from rnonday.")
async def ping(ctx):
	embed = discord.Embed(title = " ", description = "** Ponk! **", color = discord.Color.from_rgb(77,195,255))
	await ctx.respond(embed = embed)
	
@bot.command(description="This command allows you to see the test embed of rnonday.")
async def test_embed(ctx):
	embed = discord.Embed(title = "Title", description = "Desc", color = discord.Color.from_rgb(1, 2, 3), url = "https://russia.uk.com")
	embed.add_field(name = "I`m genius", value = "Europa.Plus", inline = False)
	embed.set_thumbnail(url = bot.user.avatar.url)
	embed.set_author(name = "Hah", icon_url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.H8PeRfX5VkvEgMeTWUVAbwHaIA%26pid%3DApi&f=1&ipt=e62fa4f2da3c9edffac98d578f8776e358b9b82af5cd658f7928bca730f017ff&ipo=images")
	embed.set_footer(text = "Hah", icon_url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.H8PeRfX5VkvEgMeTWUVAbwHaIA%26pid%3DApi&f=1&ipt=e62fa4f2da3c9edffac98d578f8776e358b9b82af5cd658f7928bca730f017ff&ipo=images")
	
	
	await ctx.respond(embed = embed)

@bot.command(description="This command allows you to learn the rules for using the bot from rnonday.")
async def bot_rules(ctx):
	embed = discord.Embed(title = "***Bot Rules***", description = "** **\n🇷🇺 - Русский\n\n**ʙᴄᴇ чᴛо нᴀходиᴛᴄя зᴀ ᴦᴩᴀнью боᴛᴀ, нᴇ яʙᴧяᴇᴛᴄя оᴛʙᴇᴛᴄᴛʙᴇнноᴄᴛью ʀᴅɴ ɢʀᴏᴜᴘ.**\n** **\n🇺🇸 - English\n\n**ᴇᴠᴇʀʏᴛʜɪɴɢ ᴛʜᴀᴛ ɪs ʙᴇʏᴏɴᴅ ᴛʜᴇ sᴄᴏᴘᴇ ᴏꜰ ᴛʜᴇ ʙᴏᴛ ɪs ɴᴏᴛ ᴛʜᴇ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ ᴏꜰ ʀᴅɴ ɢʀᴏᴜᴘ.**\n** **", color = discord.Color.from_rgb(77,195,255))
	await ctx.respond(embed = embed)

#@bot.command()
#async def rules(ctx):
#	await ctx.respond(
#        """```ansi
#[2;31m[1;31m[1;47m Bot[0m[1;31m[1;46m[1;45m[1;44m[1;47m [0m[1;31m[1;44m[0m[1;31m[1;45m[0m[1;31m[1;46m[0m[1;31m[1;42m[1;41m[1;37m Rules [0m[1;31m[1;41m[0m[1;31m[1;42m[0m[1;31m[1;46m[0m[1;31m[0m[2;31m[0m```
#	
#	🇷🇺 - Русский
#
#	**ʙᴄᴇ чᴛо нᴀходиᴛᴄя зᴀ ᴦᴩᴀнью боᴛᴀ, нᴇ яʙᴧяᴇᴛᴄя оᴛʙᴇᴛᴄᴛʙᴇнноᴄᴛью "your company name".**
#	** **
#
#	🇺🇸 - English
#
#	**ᴇᴠᴇʀʏᴛʜɪɴɢ ᴛʜᴀᴛ ɪs ʙᴇʏᴏɴᴅ ᴛʜᴇ sᴄᴏᴘᴇ ᴏꜰ ᴛʜᴇ ʙᴏᴛ ɪs ɴᴏᴛ ᴛʜᴇ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ ᴏꜰ "your company name".**
#	** **
#	""")
    
@bot.command(description="This command allows you to apply to rnonday.")
async def request(ctx,name,age,rulesaccept):
	if cursor.execute(f"SELECT id FROM users WHERE id = {ctx.author.id}").fetchone() == None:
		cursor.execute(f"INSERT INTO users VALUES({ctx.author.id},'{ctx.author.name}', '{name}', '{age}', '{rulesaccept}')")
		connection.commit()
		await ctx.respond("""Thank for your application!""")
	else:
		await ctx.respond("""You have already submitted an application and/or you cannot submit an application!""")

connection = sqlite3.connect('database.sql',check_same_thread=False)
cursor = connection.cursor()

bot.run(" Your Discord Bot Token")