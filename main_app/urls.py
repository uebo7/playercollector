from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('players/', views.players_index, name='players_index'),
    path('player/<int:player_id>/', views.player_detail, name='player_detail'),
    #crud path
    path('players/create/', views.PlayerCreate.as_view(), name='player_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='player_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player_delete'),
    #alt model route
    path('players/<int:player_id>/add_win/', views.add_win, name='add_win'),
    # character routes
    path('characters/', views.CharacterIndex.as_view(), name='character_index'),
    path('characters/create/', views.CharacterCreate.as_view(), name='character_create'),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name='character_detail'),
    path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name='character_update'),
    path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='character_delete'),
    # M:M
    path('players/<int:player_id>/assoc_character/<int:character_id>/', views.assoc_character, name='assoc_character'),        
    path('players/<int:player_id>/unassoc_character/<int:character_id>/', views.unassoc_character, name='unassoc_character'),
    path('accounts/signup/', views.signup, name='signup'),
]