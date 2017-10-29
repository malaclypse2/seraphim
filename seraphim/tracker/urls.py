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
        view=views.add_wound,
        name='add_wound'
    ),
    # e.g., /tracker/manage/3/12/heal
    url(
        regex=r'^manage/(?P<combat_pk>[0-9]+)/(?P<character_pk>[0-9]+)/heal$',
        view=views.add_heal,
        name='add_heal'
    ),
    # e.g., /tracker/manage/3/12/bandage
    url(
        regex=r'^manage/(?P<combat_pk>[0-9]+)/(?P<character_pk>[0-9]+)/bandage/$',
        view=views.bandage_character,
        name='bandage_character'
    ),
    # e.g. /tracker/combat/create
    url(
        regex=r'^manage/combat/create$',
        view=views.CombatCreate.as_view(),
        name='create_combat'
    ),

]
