from django.conf import settings
from django.contrib.sites.models import Site


def project_context(request):

    current_site = Site.objects.get_current()

    return {
        'PROJECT_NAME': settings.PROJECT_VERBOSE_NAME,
        'PROJECT_LOGO_URL': settings.PROJECT_LOGO_URL,
        'PROJECT_EMAIL': settings.DEFAULT_FROM_EMAIL,
        'PROJECT_PHONE_NUMBER': settings.PROJECT_PHONE_NUMBER,
        'PROJECT_URL': f'https://www.{ current_site.domain }',
        'SITE_DOMAIN_NAME': current_site.domain,
        'SITE_DISPLAY_NAME': current_site.name,
    }