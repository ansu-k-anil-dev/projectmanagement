from django.db import models

from auth_module.models import Coridinator, Student


class StudentGroup(models.Model):
    cordinator = models.ForeignKey(to=Coridinator, on_delete=models.DO_NOTHING)
    student = models.ManyToManyField(to=Student)
    added_on = models.DateTimeField(auto_now=True)
    topic_submission_date = models.DateField()
    presentation_submission_date = models.DateField()
    record_submission_date = models.DateField()
    project_submission_date = models.DateField(null=True)
    is_topic_submitted = models.BooleanField(default=False)
    is_presentation_submitted = models.BooleanField(default=False)
    is_record_submitted = models.BooleanField(default=False)
    is_project_submitted = models.BooleanField(default=False)
    assigned_faculty_id = models.IntegerField(null=True)
    marks_obtained = models.IntegerField(null=True)

    def __str__(self):
        return self.cordinator.admin.first_name
    
class Evaluation(models.Model):
    cordinator = models.ForeignKey(to=Coridinator, on_delete=models.DO_NOTHING)
    student_group = models.ForeignKey(to=StudentGroup, on_delete=models.DO_NOTHING)
    project_title = models.CharField(max_length=100)
    viva_mark = models.IntegerField(null=True)
    demo_mark = models.IntegerField(null=True)
    presentation_mark = models.IntegerField(null=True)
    internal_mark = models.IntegerField()
    internal_grade = models.CharField(max_length=50)
    remark = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.project_title
    
    
