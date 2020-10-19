from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    # Users URLs
    path('users/<uuid:user_uuid>/', views.UserDetail.as_view()),
    # Django REST Framework Auth URLs
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
