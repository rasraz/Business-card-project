from django.db import models


class MyInfo(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="home_MyInfo")
    title=models.CharField(max_length=100)
    caption=models.TextField()
    about_use=models.TextField()
    features=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Services(models.Model):
    graphic_design=models.TextField()
    web_design=models.TextField()
    html_css=models.TextField()
    ui_ux_design=models.TextField()
    SEO_optimization=models.TextField()
    business_development=models.TextField()


class ProfessionCategory(models.Model):
    professions=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.professions}'


class Bio(models.Model):
    header=models.CharField(max_length=100)
    details=models.TextField()
    start_year=models.DateField()
    end_year=models.DateField()
    profession_category=models.ForeignKey(ProfessionCategory,on_delete=models.CASCADE,null=True,blank=True,related_name='bio')
 
    def __str__(self):
        return f'{self.header}'


class PortfolioCategory(models.Model):
    category=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.category}'


class Portfolio(models.Model):
    project_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='home_portfolio')
    portfolio_category=models.ForeignKey(PortfolioCategory,on_delete=models.SET_NULL,null=True,blank=True,related_name='protfolio')

    def __str__(self):
        return f'{self.project_name}'


class Pricing(models.Model):
    CHOICE_PLAN=(
    ('B','Basic'),
    ('S','Standard'),
    ('P','Premium'),)
    plan=models.CharField(choices=CHOICE_PLAN,max_length=1)
    price=models.IntegerField()
    graphic_design=models.BooleanField(default=False)
    web_design=models.BooleanField(default=False)
    html_css=models.BooleanField(default=False)
    ui_ux_design=models.BooleanField(default=False)
    SEO_optimization=models.BooleanField(default=False)
    business_development=models.BooleanField(default=False)


class ContactUs(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    estimated_budget=models.CharField(max_length=50)
    enter_your_message=models.TextField()
