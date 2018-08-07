from django.conf.urls import url
from complain_app import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^complain$',views.ComplainListView.as_view(),name='complain_list'),
    url(r'^complain/new/$',views.CreateComplainView.as_view(),name='create'),
    ]
