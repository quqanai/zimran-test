from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from code import handlers
from code.config import TORTOISE_CONFIG

app = FastAPI()
app.add_api_route('/news/{symbol}', handlers.get_company_news)

register_tortoise(app, config=TORTOISE_CONFIG)
