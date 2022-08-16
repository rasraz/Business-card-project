from django.contrib import admin
from .models import Portfolio,Bio,MyInfo,Pricing,ContactUsModel,Services,Features

admin.site.register(Portfolio)
admin.site.register(Bio)
admin.site.register(Features)
admin.site.register(MyInfo)
admin.site.register(Pricing)
admin.site.register(ContactUsModel)
admin.site.register(Services)

