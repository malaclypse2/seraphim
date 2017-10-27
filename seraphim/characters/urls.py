from django.conf.urls import url

from . import views

urlpatterns = [
    # e.g.: /
    #url(r'^$', views.index, name='index'),
    url(
        regex=r'^$',
        view=views.CharacterList.as_view(),
        name='character_list'
    ),
    # e.g.: /characters/3/
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.CharacterDetail.as_view(),
        name='character_detail'
    ),
    # e.g.: /characters/create/
    url(
        regex=r'^create$',
        view=views.CharacterCreate.as_view(),
        name='character_create'
    ),
    # e.g.: /characters/update/3/
    url(
        regex=r'^update/(?P<pk>[0-9]+)/$',
        view=views.CharacterUpdate.as_view(),
        name='character_update'
    ),
    # e.g.: /characters/delete/3/
    url(
        regex=r'^delete/(?P<pk>[0-9]+)/$',
        view=views.CharacterDelete.as_view(),
        name='character_delete'
    ),
]
