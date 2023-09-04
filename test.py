import os
import backup

from dotenv import load_dotenv

load_dotenv()

f = os.environ.get('DISCORD_API_KEY')
# print(f)
# backup.backup("jio")