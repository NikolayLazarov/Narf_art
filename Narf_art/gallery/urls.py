from django.urls import path

from . import views


# urlpatterns = [

# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('card/<int:card_id>',views.card_by_id, name = 'card_by_id' ),
    path('card',views.all_cards,name = 'all_cards'),
    path('probe', views.probe,name = 'probe'),
    path('upload/', views.image_upload_view),
    path('new/', views.addProduct, name = "add-card"),

]

#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# from django.views.generic import RedirectView
# urlpatterns += [
#     path('', RedirectView.as_view(url='gallery/', permanent=True)),
# ]

