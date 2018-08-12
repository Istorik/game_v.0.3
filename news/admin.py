from django.contrib import admin
from news.models import News, Category, Category_miner, Miner, BaseItems

# Register your models here.
admin.site.register(News)
admin.site.register(Category)
admin.site.register(Category_miner)
admin.site.register(Miner)
admin.site.register(BaseItems)

