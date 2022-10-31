from tortoise import fields, Model


class Subscription(Model):
    id = fields.IntField(pk=True)  # noqa: A003
    email = fields.CharField(max_length=100)
    symbol = fields.CharField(max_length=10)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'subscriptions'
        unique_together = 'email', 'symbol'
