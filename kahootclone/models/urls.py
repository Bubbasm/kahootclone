from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
]
