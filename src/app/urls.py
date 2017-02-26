from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^jobs/new/$', views.NewJobPage.as_view(), name='new_job'),
    url(r'^jobs/$', views.JobsPage.as_view(), name='jobs'),
    url(r'^jobs/(?P<print_id>[^/]+)/$', views.JobPage.as_view(), name='job'),
]
