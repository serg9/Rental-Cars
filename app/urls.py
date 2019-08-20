from django.contrib import admin
from django.urls import path, include
#from rest_framework import routers
from crawler import views

#router = routers.DefaultRouter()
#router.register(r'crawler', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_data, name='get_data'),
]
