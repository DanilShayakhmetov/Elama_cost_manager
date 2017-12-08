from django.conf.urls import url,include
from syslogin import views
urlpatterns = [

    url(r'^login/', views.Login),
    url(r'^logout/', views.Logout),
    url(r'^registration/', views.Registered)

    # url(r'^register/$', views.RegisterFormView.as_view())
]
