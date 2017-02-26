from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^jobs/create/$', views.NewJobPage.as_view(), name='new_job'),
    url(r'^jobs/$', views.JobsPage.as_view(), name='jobs'),
    url(r'^jobs/view/(?P<print_id>[^/]+)/$', views.JobPage.as_view(), name='view_job'),
    url(r'^jobs/manage/(?P<print_id>[^/]+)/$', views.ManageJobPage.as_view(), name='manage_job'),
    url(r'^jobs/edit/(?P<print_id>[^/]+)/$', views.EditJobPage.as_view(), name='edit_job'),
]
