from django.urls import path, include
from django.views.generic import TemplateView
from .views import greeting_page

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('greeting/', greeting_page, name='greeting'),
]
