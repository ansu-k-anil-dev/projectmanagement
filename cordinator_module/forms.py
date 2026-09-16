# forms.py
from django import forms
from .models import StudentGroup, Evaluation

class StudentGroupForm(forms.ModelForm):
    class Meta:
        model = StudentGroup
        fields = ['topic_submission_date',
                  'presentation_submission_date',
                  'record_submission_date',
                  'project_submission_date']
        widgets = {
            'topic_submission_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'presentation_submission_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'record_submission_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'project_submission_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = [
            'viva_mark',
            'demo_mark',
            'presentation_mark',
            'internal_mark',
            'internal_grade',
            'remark'
        ]
        widgets = {
            'viva_mark': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter viva marks'
            }),
            'demo_mark': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter demo marks'
            }),
            'presentation_mark': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter presentation marks'
            }),
            'internal_mark': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter internal marks'
            }),
            'internal_grade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter internal grade'
            }),
            'remark': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter remarks',
                'rows': 3
            })
        }