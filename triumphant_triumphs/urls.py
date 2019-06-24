"""triumphant_triumphs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  path(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from about import urls as about_urls
from accounts import urls as accounts_urls
from accounts.views import index
from cart import urls as cart_urls
from charts import urls as charts_urls
from checkout import urls as checkout_urls
from products import urls as products_urls
from contact import urls as contact_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about/', include(about_urls)),
    path('accounts/', include(accounts_urls)),
    path('cart/', include(cart_urls)),
    path('charts/', include(charts_urls)),
    path('checkout/', include(checkout_urls)),
    path('contact/', include(contact_urls)),
    path('products/', include(products_urls)),
]

# this setting recommended in Django docs for development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
