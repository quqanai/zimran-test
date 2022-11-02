from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from code import handlers
from code.config import TORTOISE_CONFIG

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.add_api_route('/news', handlers.get_news)
app.add_api_route('/news/{news_id}', handlers.get_news_by_id)
app.add_api_route('/news/company/{symbol}', handlers.get_news_by_symbol)

register_tortoise(app, config=TORTOISE_CONFIG)
