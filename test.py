import os

from dotenv import load_dotenv

load_dotenv()

f = os.environ.get('DISCORD_API_KEY')
print(f)