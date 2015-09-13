from django.conf.urls import include, url
from django.contrib import admin

from autumnbreeze.views import home_redirect
from autumnbreeze.views import main
from autumnbreeze.views import results


urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^results/', results, name='results'),
    url(r'^home_redirect/', home_redirect, name='home_redirect'),
    url(r'^admin/', include(admin.site.urls)),
]
