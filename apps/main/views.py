from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class IndexView(TemplateView):
    template_name = 'main/index.html'


class AboutView(TemplateView):
    template_name = 'main/about.html'


class ContactUsView(TemplateView):
    template_name = 'main/contact-us.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'main/privacy-policy.html'


class TermsAndConditionsView(TemplateView):
    template_name = 'main/terms-and-conditions.html'


def handler400(request, exception):
    response = render(
        request,
        "main/error-page.html",
        context={
            'error_number': '400',
            'error_message': _("There's something wrong with this page!")
        }
    )
    response.status_code = 400
    return response


def handler403(request, exception):
    response = render(
        request,
        "main/error-page.html",
        context={
            'error_number': '403',
            'error_message': _("You're not supposed to be here!")
        }
    )
    response.status_code = 403
    return response


def handler404(request, exception):
    response = render(
        request,
        "main/error-page.html",
        context={
            'error_number': '404',
            'error_message': _("We can't find the page you're looking for.")
        }
    )
    response.status_code = 404
    return response


def handler500(request):
    response = render(
        request,
        "main/error-page.html",
        context={
            'error_number': '500',
            'error_message': _("That wasn't supposed to happen... We'll get to work on fixing this error.")
        }
    )
    response.status_code = 500
    return response

