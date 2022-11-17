from django.contrib import admin
from first_app.models import Accounts,Articles,Articles_Details,Comments

# Register your models here.
admin.site.register(Accounts)
admin.site.register(Articles)
admin.site.register(Articles_Details)
admin.site.register(Comments)