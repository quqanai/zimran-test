from fastapi import FastAPI
from fastapi_pagination import add_pagination, Page
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from code import handlers
from code.config import TORTOISE_CONFIG
from code.schemas import NewsSchema

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.add_api_route('/news', handlers.get_news, response_model=Page[NewsSchema])
app.add_api_route('/news/{news_id}', handlers.get_news_by_id)
app.add_api_route(
    '/companies/{symbol}/news', handlers.get_news_by_symbol, response_model=Page[NewsSchema],
)

register_tortoise(app, config=TORTOISE_CONFIG)
add_pagination(app)
