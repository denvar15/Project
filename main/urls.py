from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/date/', views.date, name='date'),
    path('<int:question_id>/author/', views.author, name='author'),
    path('details/', views.details, name='details')]