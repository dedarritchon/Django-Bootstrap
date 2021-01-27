from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from upload.views import image_upload
from main.views import welcome, register, login, logout, about, pricing


urlpatterns = [
    url(r'^$', welcome, name='welcome'),
    url(r'^register/?$', register, name='register'),
    url(r'^login/?$', login, name='login'),
    url(r'^logout/?$', logout, name='logout'),
    url(r'^about/?$', about, name='about'),
    url(r'^pricing/?$', pricing, name='pricing'),
    url(r'^upload/?$', image_upload, name='upload'),
    url(r'^admin/', admin.site.urls),
]


if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
