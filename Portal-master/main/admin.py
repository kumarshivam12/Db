from django.contrib import admin

# Register your models here.
from .models import consumer
from .models import History
from .models import cabprosessing
admin.site.register(consumer)
admin.site.register(cabprosessing)
admin.site.register(History)