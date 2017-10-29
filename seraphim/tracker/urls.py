from django.conf.urls import url

from . import views

urlpatterns = [
    # e.g.: /tracker/
    #url(r'^$', views.index, name='index'),
    url(
        regex=r'^$',
        view=views.index,
        name='index'
    ),
]
