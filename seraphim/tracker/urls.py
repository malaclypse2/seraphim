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
    # e.g.: /tracker/manage/3/
    url(
        regex=r'^manage/(?P<pk>[0-9]+)/$',
        view=views.manage_combat,
        name='manage'
    ),
    # e.g., /tracker/manage/3/12/
    url(
        regex=r'^manage/(?P<combat_pk>[0-9]+)/(?P<character_pk>[0-9]+)/$',
        view=views.character_detail,
        name='manage_character'
    ),
    # e.g., /tracker/manage/3/12/wound
    url(
        regex=r'^manage/(?P<combat_pk>[0-9]+)/(?P<character_pk>[0-9]+)/wound$',
        view=views.manage_wound,
        name='manage_wound'
    ),
]
