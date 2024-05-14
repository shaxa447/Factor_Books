from os import getenv

from dotenv import load_dotenv
from redis_dict import RedisDict

database = RedisDict('factor_book')
load_dotenv('.env')
TOKEN = getenv("BOT_TOKEN")
ADMIN_LIST = 1259522139,
# 1259522136
