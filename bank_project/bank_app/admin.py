from django.contrib import admin
from .models import District, Branch, AccountType, Material

# Register your models here.
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(AccountType)
admin.site.register(Material)
