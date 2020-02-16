from django.urls import path

from survey import views

app_name = 'survey'

urlpatterns = [

path('new', views.survey_create, name='survey_create'),
path('fetch', views.fetchData, name='survey_data'),


]