from django.conf.urls import url
from . import views

#template urls
#app_name is the name you will use in base (template tags). i.e. app_name:urlname
app_name = 'basic_app'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register/$', views.user_login, name='user_login')
]
