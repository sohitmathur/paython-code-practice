from django.contrib import admin
from.models import AccountDetails

# Register your models here.

class AccountDetailsAdmin(admin.ModelAdmin):
    list_display= ['id','account_name','bal','acdate','email','mobile']

admin.site.register(AccountDetails,AccountDetailsAdmin)