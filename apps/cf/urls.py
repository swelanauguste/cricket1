from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('star/admins/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('inventory', include('inventory.urls', namespace='inventory')),
    path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
