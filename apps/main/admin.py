from django.contrib import admin
from django.conf import settings

# Admin Site General Settings
admin.site.site_header = settings.PROJECT_VERBOSE_NAME
admin.site.site_title = settings.PROJECT_VERBOSE_NAME
admin.site.index_title = settings.PROJECT_VERBOSE_NAME
