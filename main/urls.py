from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^products/$', views.products, name='products'),
	url(r'^versions/(?P<product_id>\d+)/$', views.versions, name='versions'),
	url(r'^functions/$', views.functions, name='functions'),
	url(r'^feedback/$', views.feedback, name='feedback'),
	url(r'^message/$', views.message, name='message'),
	url(r'^about/$', views.about, name='about'),
]