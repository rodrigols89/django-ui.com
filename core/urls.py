from django.contrib import admin
from django.urls import path
from django_distill import distill_path
from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    distill_path('', views.home, name='home', distill_func=lambda: None),

    # Páginas Tailwind
    distill_path('tailwind/core-concepts/', views.core_concepts, name='core-concepts', distill_func=lambda: None),
    distill_path('tailwind/spacing/', views.spacing, name='spacing', distill_func=lambda: None),
    distill_path('tailwind/sizing/', views.sizing, name='sizing', distill_func=lambda: None),
    distill_path('tailwind/layout/', views.layout, name='layout', distill_func=lambda: None),
    distill_path('tailwind/typography/', views.typography, name='typography', distill_func=lambda: None),
    distill_path('tailwind/borders/', views.borders, name='borders', distill_func=lambda: None),
]
