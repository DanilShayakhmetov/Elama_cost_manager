from django.conf.urls import url,include
from cost_manager import views
urlpatterns = [

    url(r'^1/addPost/1', views.form_test),
    url(r'^1/addPost/2', views.TryToSave),
    url(r'^accounts/all/', views.AccountList),
    url(r'^transactions/get/(?P<account_id>\d+)/$', views.Journal),

]
