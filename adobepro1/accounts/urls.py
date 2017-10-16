from django.conf.urls import url
from .views import (
    login_view,
)
from .views import logout_view, register_view, elasticsearch_view

urlpatterns = [
    url(r'^login/$', login_view, name = "login"),
]
urlpatterns += [
    url(r'^logout/$', logout_view, name = "logout"),
]

urlpatterns += [
    url(r"^register/$", register_view, name = "register"),
]

urlpatterns += [
   url(r"^elasticsearch/$", elasticsearch_view, name = "elasticsearch"),
]