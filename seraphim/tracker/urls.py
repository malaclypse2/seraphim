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
    # e.g.: /groups/manage/3/
    url(
        regex=r'^manage/(?P<pk>[0-9]+)/$',
        view=views.manage_combat,
        name='manage'
    ),
]
