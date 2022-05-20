from django.urls import path

from . import views


# urlpatterns = [

# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('card/<int:card_id>',views.card_by_id, name = 'card_by_id' ),
    path('card',views.all_cards,name = 'all_cards'),
    path('probe', views.probe,name = 'probe'),
]

# from django.views.generic import RedirectView
# urlpatterns += [
#     path('', RedirectView.as_view(url='gallery/', permanent=True)),
# ]

