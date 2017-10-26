from django.conf.urls import url

from . import views

urlpatterns = [
    # e.g.: /
    url(r'^$', views.index, name='index'),
    # e.g.: /characters/3/
    url(
        regex=r'^(?P<character_id>[0-9]+)/$',
        view=views.CharacterDetailView.as_view(),
        name='detail'
    ),
]
