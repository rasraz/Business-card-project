from django.shortcuts import render, redirect 
from .models import Portfolio,Bio,MyInfo,Pricing,Services,ContactUsModel
from .form import ContactUsForm

def index(request):
    E_bio=Bio.objects.filter(profession_category='E')
    W_bio=Bio.objects.filter(profession_category='W')
    P_bio=Bio.objects.filter(profession_category='P')
    D_bio=Bio.objects.filter(profession_category='D')
    S_bio=Bio.objects.filter(profession_category='S')
    I_portfolio=Portfolio.objects.filter(portfolio_category="I")
    AN_portfolio=Portfolio.objects.filter(portfolio_category="AN")
    AP_portfolio=Portfolio.objects.filter(portfolio_category="AP")
    W_portfolio=Portfolio.objects.filter(portfolio_category="W")
    S_portfolio=Portfolio.objects.filter(portfolio_category="S")
    P_portfolio=Portfolio.objects.filter(portfolio_category="P")
    B_pricing=Pricing.objects.filter(plan="B")
    S_pricing=Pricing.objects.filter(plan="S")
    P_pricing=Pricing.objects.filter(plan="P")
    
    form=ContactUsForm()
    
    if request.method == "POST":
        form=ContactUsForm(request.POST)
        if form.is_valid():
            ContactUsModel.objects.create(**form.cleaned_data)

    return render(request,'home/index.html',{
        "portfolio":{
            'ALL':Portfolio.objects.all(),
            "I":I_portfolio,
            "AN":AN_portfolio,
            "AP":AP_portfolio,
            "W":W_portfolio,
            "S":S_portfolio,
            "P":P_portfolio},
        "resume":{
            "E":E_bio,
            "W":W_bio,
            "P":P_bio,
            "D":D_bio,
            "S":S_bio},
        "pricing":{
            "B":B_pricing,
            "S":S_pricing,
            "P":P_pricing,
        },
        "services":Services.objects.all(),
        "info":MyInfo.objects.all(),
        "contact_form":form,
    })
