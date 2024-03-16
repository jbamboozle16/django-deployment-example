from django.urls import include,path
from basic_app import views

#TEMPLATE TAGGING
# you have to set a global variable called "app_name" named after your app
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
