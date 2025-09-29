from django.urls import path
from .views import home, spacing, sizing

urlpatterns = [
    path('', home, name='home'),
    path(route="tailwind/spacing/", view=spacing, name="spacing"),
    path(route="tailwind/sizing/", view=sizing, name="sizing"),
]
