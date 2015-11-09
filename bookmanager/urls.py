from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<book_ISBN>[0-9-]+)/$', views.detail, name='detail'),
    url(r'^delete/$',views.delete,name='delete'),
    url(r'^update/$',views.update,name='update'),
    url(r'^addbook/$',views.addbook,name='addbook'),
    url(r'^addauthor/$',views.addauthor,name='addauthor'),
]