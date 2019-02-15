from django.contrib import admin

# Register your models here.
from .models import consumer_Db
from .models import role_per
admin.site.register(consumer_Db)
admin.site.register(role_per)