from django.contrib import admin
from . import models as seller_model


admin.site.register(seller_model.Seller)
admin.site.register(seller_model.Seller_company_info)
