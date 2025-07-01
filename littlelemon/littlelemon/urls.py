"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 
# Import the router from DRF
from rest_framework.routers import DefaultRouter
# Import views from your restaurant app
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token



# Create a router instance
router = DefaultRouter()

# Register the ViewSet with the router
# This single line creates all the necessary URLs for your BookingViewSet:
# - /tables/ (for GET list and POST create)
# - /tables/{id}/ (for GET retrieve, PUT update, DELETE destroy)
router.register(r'booking', views.BookingViewSet, basename='booking')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('', include(router.urls)),
    
    # --- ADD DJOSER URLS ---
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('django.contrib.auth.urls')),
    path('api-token-auth/', obtain_auth_token)
]
