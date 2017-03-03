import uuid

from django.db import models

from profiles.models import Profile


class PrintJob(models.Model):
    print_id = models.UUIDField(default=uuid.uuid4, editable=False, blank=False, primary_key=True, unique=True,
                                auto_created=True)
    print_name = models.CharField(max_length=20, verbose_name="Print Name", blank=False)
    requester = models.ForeignKey(Profile, on_delete=models.CASCADE, editable=False, auto_created=True)
    notes = models.TextField(verbose_name='Notes', blank=True, null=True)
    file = models.FileField(verbose_name="CAD File", upload_to='cad_files', blank=False)

    datetime_submitted = models.DateTimeField(editable=False, auto_now_add=True, verbose_name='Job submitted')
    datetime_actioned = models.DateTimeField(editable=False, blank=True, null=True, verbose_name="Job last actioned")

    job_status = models.CharField(max_length=40, blank=True, verbose_name="Job Status")

    def __str__(self):
        return format(self.print_name)

    class Meta:
        ordering = ['datetime_actioned', 'datetime_submitted']
        verbose_name = 'Print Job'
        verbose_name_plural = 'Print Jobs'
