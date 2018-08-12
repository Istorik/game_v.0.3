from django.contrib import admin
from news.models import News, Category, BaseItems, Inventory, BaseQrCode

# Register your models here.
admin.site.register(News)
admin.site.register(Category)
admin.site.register(BaseItems)
admin.site.register(Inventory)
admin.site.register(BaseQrCode)
