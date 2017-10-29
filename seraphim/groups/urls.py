from django.conf.urls import url

from . import views

urlpatterns = [
    # e.g.: /
    #url(r'^$', views.index, name='index'),
    url(
        regex=r'^$',
        view=views.GroupList.as_view(),
        name='list'
    ),
    # e.g.: /groups/3/
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.GroupDetail.as_view(),
        name='detail'
    ),
    # e.g.: /groups/create/
    url(
        regex=r'^create$',
        view=views.GroupCreate.as_view(),
        name='create'
    ),
    # e.g.: /groups/update/3/
    url(
        regex=r'^update/(?P<pk>[0-9]+)/$',
        view=views.GroupUpdate.as_view(),
        name='update'
    ),
    # e.g.: /groups/delete/3/
    url(
        regex=r'^delete/(?P<pk>[0-9]+)/$',
        view=views.GroupDelete.as_view(),
        name='delete'
    ),
]
