from distutils.log import debug
from xml.etree.ElementInclude import include
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
# playground/hello
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('_debug_/', include(debug_toolbar.urls)),
]
