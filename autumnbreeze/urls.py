from django.conf.urls import include, url
from django.contrib import admin

from autumnbreeze.views import main


urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^admin/', include(admin.site.urls)),
]
