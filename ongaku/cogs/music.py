# cog that handles the music in voice channels
import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
import wavelink

intents = discord.Intents().all()
client = discord.Client(intents=intents)
owners = [375797651486015488, ]
guilds = [1015609486225965102, ]
bot = discord.Bot(intents=intents, owner_ids = set(owners), guild_ids = set(guilds))

class music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        """Connect to our Lavalink nodes."""
        await self.bot.wait_until_ready()
        await wavelink.NodePool.create_node(bot=self.bot,
                                            host='0.0.0.0',
                                            port=2333,
                                            password='localhost123')

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f'Node: <{node.identifier}> is ready!')

    music = SlashCommandGroup("music", "music related commands")

    @music.command()
    async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):

        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        await vc.play(search)

def setup(bot):
    bot.add_cog(music(bot))