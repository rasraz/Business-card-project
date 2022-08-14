from django.contrib import admin
from .models import Portfolio,PortfolioCategory,ProfessionCategory,Bio,MyInfo,Pricing,ContactUs

admin.site.register(ProfessionCategory)
admin.site.register(Portfolio)
admin.site.register(PortfolioCategory)
admin.site.register(Bio)
admin.site.register(MyInfo)
admin.site.register(Pricing)
admin.site.register(ContactUs)
