import sys
path = 'C:/ADNAN/django_learning/first_django'
sys.path.append(path)
import os 
os.environ["DJANGO_SETTINGS_MODULE"]= "first_django.settings"

import django
django.setup() 

from first_app.models  import Articles_Details,Accounts,Articles,Comments
from faker import Faker
import random,datetime
fake=Faker()
def populate(n=5):
   
    for i in range(n):
        acc = Accounts.objects.get_or_create(Full_name=fake.name(),Username=str(fake.first_name()+str(random.randint(10,9999))).lower(),email=fake.email(),passw=fake.password())[0]
        article = Articles.objects.get_or_create(Username=acc,Article_id=fake.ean(prefixes=('0010', '0011')),Article_Content=fake.paragraph(nb_sentences=random.randint(10,30)),Date_Posted=fake.date_this_year())[0]
        cmnts = Comments.objects.get_or_create(Article_id=article,Comment_id = fake.ean(prefixes=('9911', '9910')),Comment_Username=str(fake.first_name()+str(random.randint(10,9999))),Comment=fake.paragraph(nb_sentences=random.randint(5,10)))[0]
        artcl_dtl = Articles_Details.objects.get_or_create(Article_id=article,Likes=random.randint(0,100000),Re_Posts=random.randint(0,1000),Post_Comments=cmnts)[0]


populate(10)