from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('wood/', views.wood_list, name='wood_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<int:pk>/', views.wood_detail, name='wood_detail'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)