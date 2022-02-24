from django.contrib import admin

from . import models as customer_model


admin.site.register(customer_model.Customer)
admin.site.register(customer_model.Brand)
admin.site.register(customer_model.Category)
admin.site.register(customer_model.Sub_category)
admin.site.register(customer_model.Concern)
admin.site.register(customer_model.Sub_concern)
admin.site.register(customer_model.Ingrediant)
admin.site.register(customer_model.Sub_ingrediant)
admin.site.register(customer_model.Type)
admin.site.register(customer_model.Sub_type)
admin.site.register(customer_model.Cart)
admin.site.register(customer_model.Gift)
admin.site.register(customer_model.Offer)
admin.site.register(customer_model.Product)
admin.site.register(customer_model.Shopping_order)
admin.site.register(customer_model.Payment)
admin.site.register(customer_model.Shipping)
admin.site.register(customer_model.Transaction_report)
admin.site.register(customer_model.Feedback)

admin.site.register(customer_model.Product_colors)
admin.site.register(customer_model.Subbrand)

admin.site.register(customer_model.Product_type)

admin.site.register(customer_model.Combo_product)


