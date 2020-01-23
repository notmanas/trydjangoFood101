from django.conf.urls import url

from .views import (
    RestaurantListView,
    RestaurantCreateView,
    RestaurantUpdateView
)

urlpatterns = [
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name="detail"),
    url(r'$', RestaurantListView.as_view(), name='list'),

]
