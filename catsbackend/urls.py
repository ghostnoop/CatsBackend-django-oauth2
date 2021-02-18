from django.urls import path, include
from django.contrib.auth.models import User, Group
from django.contrib import admin

admin.autodiscover()
from catsbackend.generics import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += [
    path('', include('catsapi.urls'))
]
