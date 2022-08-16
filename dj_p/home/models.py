from django.db import models


class Features(models.Model):
    feature=models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.feature}'


class MyInfo(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="home_MyInfo")
    title=models.CharField(max_length=100)
    caption=models.TextField()
    about_us=models.TextField()
    features=models.ManyToManyField(Features)

    def __str__(self):
        return f'{self.name}'


class Services(models.Model):
    interface_design=models.TextField()
    web_design=models.TextField()
    web_development=models.TextField()
    ui_ux_design=models.TextField()
    SEO_optimization=models.TextField()
    motion_graphic=models.TextField()


class Bio(models.Model):
    CHOICE_PROFESSION=(
    ('E','Education'),
    ('W','Work History'),
    ('P','Programming Skill'),
    ('D','Designer Skills'),
    ('S','SEO Skills'),)
    header=models.CharField(max_length=100)
    details=models.TextField()
    start_year=models.DateField()
    end_year=models.DateField()
    profession_category=models.CharField(max_length=30,choices=CHOICE_PROFESSION,default='E')
 
    def __str__(self):
        return f'{self.header}'


class Portfolio(models.Model):
    CHOICE_PORTFOLIO=(
    ('I','Illustration'),
    ('AN','Animation'),
    ('AP','App UI'),
    ('W','Web UI'),
    ('S','Social Media'),
    ('P','Print Design'),)
    project_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='home_portfolio')
    portfolio_category=models.CharField(max_length=30,choices=CHOICE_PORTFOLIO,default='A')

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


class ContactUsModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    estimated_budget=models.CharField(max_length=50)
    enter_your_message=models.TextField()

    def __str__(self):
        return f'{self.name}-{self.subject}-{self.estimated_budget}'    

