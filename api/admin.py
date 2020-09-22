from django.contrib import admin
from .models import Provider,Etf,Component,Price

admin.site.register(Provider)
admin.site.register(Etf)
admin.site.register(Component)
admin.site.register(Price)
