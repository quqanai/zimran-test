from tortoise import fields, Model


class News(Model):
    id = fields.IntField(pk=True)  # noqa: A003
    symbol = fields.CharField(max_length=10)
    title = fields.CharField(max_length=500)
    content = fields.TextField(null=True)
    image_url = fields.TextField(null=True)
    published_at = fields.DatetimeField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'news'
