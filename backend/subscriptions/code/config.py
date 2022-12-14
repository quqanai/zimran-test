from pydantic import AmqpDsn, BaseSettings, PostgresDsn


class Settings(BaseSettings):
    database_url: PostgresDsn
    rabbitmq_url: AmqpDsn = None
    stock_market_url: str = None

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()

TORTOISE_CONFIG = {
    'connections': {'default': settings.database_url},
    'apps': {
        'models': {
            'models': ['code.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}
