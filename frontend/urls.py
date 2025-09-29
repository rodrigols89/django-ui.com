from django.urls import path
from .views import home, spacing

urlpatterns = [
    path('', home, name='home'),
    path(route="tailwind/spacing/", view=spacing, name="spacing"),
]
