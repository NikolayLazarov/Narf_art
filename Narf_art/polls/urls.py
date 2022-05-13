
#see what this does
from django.urls import path

from . import views


# urlpatterns = [

# ]

urlpatterns = [
    path('', views.index, name='index'),
]

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

