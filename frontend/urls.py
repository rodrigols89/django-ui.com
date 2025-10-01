from django.urls import path
from .views import home, spacing, sizing, layout, typography, borders

urlpatterns = [
    path('', home, name='home'),
    path(route="tailwind/spacing/", view=spacing, name="spacing"),
    path(route="tailwind/sizing/", view=sizing, name="sizing"),
    path(route="tailwind/layout/", view=layout, name="layout"),
    path(route="tailwind/typography/", view=typography, name="typography"),
    path(route="tailwind/borders/", view=borders, name="borders"),
]
