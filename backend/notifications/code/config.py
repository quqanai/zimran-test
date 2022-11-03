from pydantic import AmqpDsn, BaseSettings, EmailStr


class Settings(BaseSettings):
    rabbitmq_url: AmqpDsn
    email_host: str
    email_port: int
    email_username: EmailStr
    email_password: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
