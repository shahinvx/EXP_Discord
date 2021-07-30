from django.urls import path
from .import views

urlpatterns = [
    # include path() of (sub_app) views.py
    path('', views.Discord_Home.as_view(), name='Discord App'),
    path('list/',views.Discord_list.as_view(), name='Discord List'),
    path('model_list/',views.Nlp_list.as_view(), name='Discord List'),
    path('add_discord/',views.Discord_Add.as_view(), name='Discord Add'),
    path('add_nlp/',views.Nlp_Model_Add.as_view(), name='NLP Model Add'),
    path('discord_start/<name>/',views.Discord_App_Start.as_view(),name='Discord App Start'),
    path('discord_alt/<name>/',views.Discord_alt.as_view(),name='Discord App Start'),
]