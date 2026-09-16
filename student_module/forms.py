from django import forms
from .models import TopicSubmission, PresentationSubmission, RecordSubmission, ProjectSubmission


class TopicSubmissionForm(forms.ModelForm):
    class Meta:
        model = TopicSubmission
        fields = ['title',
                  'file']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project title'
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-control-file'
            })
        }


class PresentationSubmissionForm(forms.ModelForm):
    class Meta:
        model = PresentationSubmission
        fields = ['file']
        
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control-file'
            })
        }

class RecordSubmissionForm(forms.ModelForm):
    class Meta:
        model = RecordSubmission
        fields = ['file']
        
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control-file'
            })
        }


class ProjectSubmissionForm(forms.ModelForm):
    class Meta:
        model = ProjectSubmission
        fields = ['file']
        
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control-file'
            })
        }
