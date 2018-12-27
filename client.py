from discord.ext import commands;
Client = commands.Bot(command_prefix="c.")

@Client.command()
async def test(ctx):
      ctx.send("Hello!")

Client.run("token")
