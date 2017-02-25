from django.contrib import messages
from django.views import generic

from app import forms


class NewJobPage(generic.TemplateView):
    template_name = 'app/new_job.html'
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "job_form" not in kwargs:
            kwargs["user_form"] = forms.JobForm(instance=user)
        return super(NewJobPage, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        job_form = forms.JobForm(request.POST, request.FILES, instance=user)
        if not job_form.is_valid():
            messages.error(request, "There was a problem with the form. Check your inputs.")
            job_form = forms.JobForm(instance=user)
            return super(NewJobPage, self).get(request, job_form=job_form)
