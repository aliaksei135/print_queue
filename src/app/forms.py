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
            Field('file', accept=".sldprt,.sldasm,.stl"),
            Field('notes', placeholder='Any additional information goes here'),
            FormActions(
                Submit('submit', "Submit", css_class="btn-success"),
                Button('cancel', "Cancel", css_class="btn")
            )
        )

    class Meta:
        model = PrintJob
        fields = ['print_name', 'file', 'notes']
