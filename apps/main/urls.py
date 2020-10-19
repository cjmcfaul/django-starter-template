from django.urls import path

from . import views

urlpatterns = [
    path(
        route='',
        view=views.IndexView.as_view(),
        name='index',
    ),
    path(
        route='about/',
        view=views.AboutView.as_view(),
        name='about',
    ),
    path(
        route='contact-us/',
        view=views.ContactUsView.as_view(),
        name='contact_us',
    ),
    path(
        route='privacy-policy/',
        view=views.PrivacyPolicyView.as_view(),
        name='privacy_policy',
    ),
    path(
        route='terms-and-conditions/',
        view=views.TermsAndConditionsView.as_view(),
        name='terms_and_conditions',
    ),
]
