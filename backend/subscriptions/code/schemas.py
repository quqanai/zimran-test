from pydantic import BaseModel, constr, EmailStr


class CreateSubscriptionSchema(BaseModel):
    email: EmailStr
    symbol: constr(min_length=2, max_length=4)
