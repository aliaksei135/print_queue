from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from app import forms
from app import models
from app.models import PrintJob


class NewJobPage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/new_job.html'
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "job_form" not in kwargs:
            kwargs["job_form"] = forms.JobForm()
        return super(NewJobPage, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        job_form = forms.JobForm(request.POST, request.FILES, )
        if not job_form.is_valid():
            messages.error(request, "There was a problem with the form. Check your inputs.")
            job_form = forms.JobForm()
            return super(NewJobPage, self).get(request, job_form=job_form)
        else:
            job = job_form.save(commit=False)
            job.requester = user.profile_user
            job.save()
            messages.success(request, 'Your job has been added!')
            return redirect('app:jobs')


class JobsPage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/jobs.html'
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            jobs = PrintJob.objects.filter(requester=user.profile_user)
            return super(JobsPage, self).get(request, jobs=jobs)
        else:
            jobs = PrintJob.objects.all()
            return super(JobsPage, self).get(request, jobs=jobs)


class JobPage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/job.html'
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        print_id = self.kwargs.get('print_id')
        job = get_object_or_404(models.PrintJob, print_id=print_id)
        if user is not job.requester:
            return HttpResponseForbidden("You can\'t access other peoples print jobs!")
        else:
            return super(JobPage, self).get(request, job=job)
