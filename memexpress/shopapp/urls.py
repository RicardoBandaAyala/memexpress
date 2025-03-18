from django.contrib import admin
from django.urls import path
from shopapp.views import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
]