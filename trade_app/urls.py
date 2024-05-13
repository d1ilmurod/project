from django.urls import path
from .views import (
    index_page_view,
    about_page_view,
    service_page_view,
    team_page_view,
    why_page_view
)

urlpatterns = [
    path('', index_page_view, name='home'),
    path('about/', about_page_view, name='about'),
    path('service/', service_page_view, name='service'),
    path('team/', team_page_view, name='team'),
    path('why/', why_page_view, name='why'),
]
