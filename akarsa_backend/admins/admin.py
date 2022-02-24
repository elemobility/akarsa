from django.contrib import admin
from . import models as admin_model
# from . models import *

admin.site.register(admin_model.Admin)
admin.site.register(admin_model.Cms)
admin.site.register(admin_model.Faq)
admin.site.register(admin_model.Faq_category)
admin.site.register(admin_model.General_settings)
admin.site.register(admin_model.Social_media_settings)
admin.site.register(admin_model.Notification_admin)
# admin.site.register(Faq)
