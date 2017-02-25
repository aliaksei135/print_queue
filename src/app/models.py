import uuid

from django.db import models

from profiles.models import Profile


class PrintJob(models.Model):
    print_id = models.UUIDField(default=uuid.uuid4, editable=False, blank=True, primary_key=True, unique=True)
    print_name = models.CharField(max_length=20, verbose_name="Print Name", blank=False)
    requester = models.ForeignKey(Profile, on_delete=models.CASCADE, editable=False, auto_created=True)
    notes = models.TextField(verbose_name='Notes', blank=True)
    file = models.FileField(verbose_name="CAD File", upload_to='cad_files', blank=False)

    datetime_submitted = models.DateTimeField(editable=False, auto_now_add=True)
    datetime_actioned = models.DateTimeField(editable=False, blank=True, verbose_name="Job last actioned")

    job_status = models.CharField(max_length=40, editable=False, blank=True, verbose_name="Job Status")

    def __str__(self):
        return format(self.name)

    class Meta:
        ordering = ['-datetime_submitted', '-datetime_actioned']
        verbose_name = 'Print Job'
        verbose_name_plural = 'Print Jobs'
