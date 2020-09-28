from config import settings
from discord.ext import commands
import w2g


bot = commands.Bot(command_prefix='!')


@bot.command()
async def helper(context):

    help_info = '!watch <video_url> - creates a room with current video set on'
    await context.send(help_info)


@bot.command()
async def watch(context, video_url: str):
    room_url = w2g.create_room(video_url)
    await context.send(f'Room created, {room_url}')


if __name__ == '__main__':
    bot.run(settings['token'])
