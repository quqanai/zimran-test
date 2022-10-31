from fastapi import HTTPException, status

from code.exceptions import SubscriptionAlreadyExists
from code.schemas import CreateSubscriptionSchema
from code.services import SubscriptionCreateService


async def create_subscription(data: CreateSubscriptionSchema):
    service = SubscriptionCreateService(data.email, data.symbol)

    try:
        return await service.do()
    except SubscriptionAlreadyExists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
