from django.db import models

from auth_module.models import Coridinator, Student
from cordinator_module.models import StudentGroup


class TopicSubmission(models.Model):
    student_group = models.ForeignKey(to=StudentGroup, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='media/topic/files', null=True)
    submitted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    remarks = models.TextField(null=True)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class PresentationSubmission(models.Model):
    student_group = models.ForeignKey(to=StudentGroup, on_delete=models.DO_NOTHING)
    project_topic = models.ForeignKey(to=TopicSubmission, on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to='media/presentation/files')
    submitted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    remarks = models.TextField(null=True)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return "Presentation" + ""+ self.project_topic.title

class RecordSubmission(models.Model):
    student_group = models.ForeignKey(to=StudentGroup, on_delete=models.DO_NOTHING)
    project_topic = models.ForeignKey(to=TopicSubmission, on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to='media/record/files')
    submitted_on = models.DateField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    remarks = models.TextField(null=True)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return "Record" + "" + self.project_topic.title

class ProjectSubmission(models.Model):
    student_group = models.ForeignKey(to=StudentGroup, on_delete=models.DO_NOTHING)
    project_topic = models.ForeignKey(to=TopicSubmission, on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to='media/record/files')
    submitted_on = models.DateField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    remarks = models.TextField(null=True)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return "Record" + "" + self.project_topic.title

