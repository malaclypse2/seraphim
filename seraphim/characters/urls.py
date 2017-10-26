from django.conf.urls import url

from . import views

urlpatterns = [
    # e.g.: /
    #url(r'^$', views.index, name='index'),
    url(
        regex=r'^$',
        view=views.CharacterListView.as_view(),
        name='list'
    ),
    # e.g.: /characters/3/
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.CharacterDetailView.as_view(),
        name='detail'
    ),
]
