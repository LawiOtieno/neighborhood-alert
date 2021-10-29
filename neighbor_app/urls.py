from django.contrib import admin
from django.urls import path

# from . import views as app_views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', app_views.index, name="home",
    # path('api-token-auth/', obtain_auth_token)

]