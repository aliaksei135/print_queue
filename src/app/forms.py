from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Button
from django import forms

from app.models import PrintJob


class JobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Field('print_name', autocomplete='off',
                  placeholder='Something to remember this job by. '
                              'Don\'t include your name, that\'s automatically added!'),
            Field('file', accept=".sldprt,.sldasm,.stl", ),
            Field('notes', placeholder='Any additional information goes here'),
            FormActions(
                Submit('submit', "Submit", css_class="btn btn-success"),
                Button('cancel', "Cancel", css_class="btn", onclick="window.history.back()")
            )
        )

    class Meta:
        model = PrintJob
        fields = ['print_name', 'file', 'notes']


class ManageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ManageForm, self).__init__(*args, **kwargs)
        JOB_STATUS_CHOICES = ['Submitted', 'Queued', 'Next for printing', 'Printing', 'Completed']
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Field('job_status', choices=JOB_STATUS_CHOICES),
            FormActions(
                Submit('submit', "Submit", css_class="btn btn-success"),
                Button('cancel', "Cancel", css_class="btn", onclick="window.history.back()")
            )
        )

    class Meta:
        model = PrintJob
        fields = ['job_status']
