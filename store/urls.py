from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from products.views import ProductListView
from store import views

urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('usuarios/login', views.login_view, name='login_view'),
    path('usuarios/logout', views.logout_view, name='logout_view'),
    path('usuarios/registro', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('productos/', include('products.urls')),
    path('carrito/', include('carts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
