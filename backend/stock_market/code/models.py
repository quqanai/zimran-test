from tortoise import fields, Model


class Company(Model):
    symbol = fields.CharField(max_length=10, pk=True)
    name = fields.CharField(max_length=100)
    logo_url = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'companies'


class News(Model):
    id = fields.IntField(pk=True)  # noqa: A003
    company = fields.ForeignKeyField('models.Company', related_name='news')
    title = fields.CharField(max_length=500)
    content = fields.TextField(null=True)
    image_url = fields.TextField(null=True)
    published_at = fields.DatetimeField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'news'
