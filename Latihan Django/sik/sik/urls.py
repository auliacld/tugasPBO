from django.contrib import admin
from django.urls import path
from sik2020.views import halamanbaru,halamanlainnya
from . import views
urlpatterns = [
	path('', views.halo),
    path('admin/', admin.site.urls),
    path('halamanbaru/', halamanbaru),
    path('halamanlainnya/', halamanlainnya),
]
