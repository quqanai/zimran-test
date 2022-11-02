from datetime import datetime

from pydantic import BaseModel


class NewsSchema(BaseModel):
    id: int  # noqa: A003
    title: str
    content: str = None
    image_url: str = None
    published_at: datetime
