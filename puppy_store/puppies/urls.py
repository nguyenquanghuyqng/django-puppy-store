from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from . import views


schema_view = get_swagger_view(title='Puppy API')

urlpatterns = [
    url(
        r'^api/v1/puppies/(?P<pk>[0-9]+)$',
        views.get_delete_update_puppy,
        name='get_delete_update_puppy'
    ),
    url(
        r'^api/v1/puppies/$',
        views.get_post_puppies,
        name='get_post_puppies'
    ),
    url(r'^$', schema_view)
]
