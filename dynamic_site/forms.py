from django import forms
from home.models import Project, TemplateList
from django.conf import settings

template_choices = [(value.id,"{}".format(value.thumbnail.url)) for value in TemplateList.objects.all()]

class ProjectForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Project
        exclude = ['user','slug']
        # fields = ['project_name','template','project_type']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['template'].widget = forms.RadioSelect(choices = template_choices)

    def clean(self):
        cleaned_data = super(ProjectForm, self).clean()
        return cleaned_data
