from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from auth_module.models import Coridinator, Student
from cordinator_module.models import StudentGroup, Evaluation
from .models import TopicSubmission,PresentationSubmission,RecordSubmission, ProjectSubmission
from .forms import TopicSubmissionForm, PresentationSubmissionForm, RecordSubmissionForm, ProjectSubmissionForm


@login_required(login_url='login_page')
def view_group(request):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    student = Student.objects.filter(admin=request.user).first()
    student_groups = student.studentgroup_set.all()
    
    # Get evaluation data for each group
    evaluations = {}
    for group in student_groups:
        eval_data = Evaluation.objects.filter(student_group=group).first()
        if eval_data:
            evaluations[group.id] = eval_data

    context = {
        'student_groups': student_groups,
        'evaluations': evaluations
    }
    return render(request,'Student/view_group.html', context)


@login_required(login_url='login_page')
def add_topic(request, group_id):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    group_id = group_id
    student_group =StudentGroup.objects.get(id=group_id)
    submission_date = student_group.topic_submission_date
    current_time = timezone.now().date()
    if current_time > submission_date:
        messages.error(request, f'Sorry You Cannot Add Topics After Submission Time!')
        return redirect('view_group')
    if request.method == "POST":
        topic_form = TopicSubmissionForm(request.POST)
        if topic_form.is_valid():
            topic_instance = topic_form.save(commit=False)
            topic_instance.student_group_id = group_id
            topic_instance.status='Added'
            topic_instance.save()
            student_group.is_topic_submitted = True
            student_group.save()
            messages.success(request, f'Topic Details has been Added Successfully!')
            return redirect('view_topic')
        else:
            messages.success(request, f'Some Error Occured, Please Try Again!')
            return redirect('view_group')
    else:
        topic_form = TopicSubmissionForm()
        context = {
            'topic_form': topic_form,
            'group_id': group_id
        } 
        return render(request,'Student/add_topic.html', context)


@login_required(login_url='login_page')
def view_topic(request):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    student = Student.objects.filter(admin=request.user).first()
    student_groups = student.studentgroup_set.all()
    topic_data = TopicSubmission.objects.filter(student_group__in = student_groups).first()
    topic_form =  TopicSubmissionForm(instance = topic_data)
    context = {
        'topic_data': topic_data,
        'topic_form': topic_form
    }
    
    return render(request,'Student/view_topic.html', context)


@login_required(login_url='login_page')
def edit_topic(request):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    student = Student.objects.filter(admin=request.user).first()
    student_groups = student.studentgroup_set.all()
    topic_data = TopicSubmission.objects.filter(student_group__in = student_groups).first()
    if request.method == "POST":
        topic_form =  TopicSubmissionForm(request.POST, request.FILES, instance = topic_data)
        if topic_form.is_valid():
            topic_form.save()
            messages.success(request, f'Topic Details has been Added Successfully!')
            return redirect('view_topic')
        else:
            messages.success(request, f'Some Error Occured, Please Try Again!')
            return redirect('view_topic')


@login_required(login_url='login_page')
def delete_topic(request, topic_id):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    topic_data = TopicSubmission.objects.get(id=topic_id)
    student_group = topic_data.student_group
    student_group.is_topic_submitted = False 
    student_group.save()
    topic_data.delete()
    messages.success(request, f'Topic Details has been Deleted Successfully!')
    return redirect('view_topic')
    

@login_required(login_url='login_page')
def add_presentation(request, group_id):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    group_id = group_id
    student_group = StudentGroup.objects.get(id=group_id)
    submission_date = student_group.presentation_submission_date
    current_time = timezone.now().date()
    if current_time > submission_date:
        messages.error(request, f'Sorry You Cannot Add Presentation After Submission Time!')
        return redirect('view_group')
    if request.method == "POST":
        presentation_form = PresentationSubmissionForm(request.POST, request.FILES)
        topic_obj = TopicSubmission.objects.filter(student_group=student_group).first()

        uploaded_file = request.FILES.get('file')
        ppt_extensions = ('ppt', 'pptx')
        if not uploaded_file or not uploaded_file.name.lower().endswith(ppt_extensions):
            messages.error(request, 'Only PPT or PPTX formats are allowed!')
            return redirect('view_group')
        
        if presentation_form.is_valid():
            presentation_instance = presentation_form.save(commit=False)
            presentation_instance.student_group_id = group_id
            presentation_instance.project_topic_id = topic_obj.id
            presentation_instance.status='Added'
            presentation_instance.save()
            student_group.is_presentation_submitted = True
            student_group.save()
            messages.success(request, f'Presentation Details has been Added Successfully!')
            return redirect('view_presentation')
        else:
            messages.success(request, f'Some Error Occured, Please Try Again!')
            return redirect('view_group')
    else:
        presentation_form = PresentationSubmissionForm()
        context = {
            'presentation_form': presentation_form,
            'group_id': group_id
        } 
        return render(request,'Student/add_presentation.html', context)


@login_required(login_url='login_page')
def view_presentation(request):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    student = Student.objects.filter(admin=request.user).first()
    student_groups = student.studentgroup_set.all()
    data = PresentationSubmission.objects.filter(student_group__in = student_groups).first()
    form =  PresentationSubmissionForm(instance = data)
    context = {
        'data': data,
        'form': form
    }
    
    return render(request,'Student/view_presentation.html', context)


@login_required(login_url='login_page')
def edit_presentation(request):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    student = Student.objects.filter(admin=request.user).first()
    student_groups = student.studentgroup_set.all()
    data = PresentationSubmission.objects.filter(student_group__in = student_groups).first()
    if request.method == "POST":
        form =  PresentationSubmissionForm(request.POST,request.FILES, instance = data)
        if form.is_valid():
            form.save()
            messages.success(request, f'Details has been Added Successfully!')
            return redirect('view_presentation')
        else:
            messages.success(request, f'Some Error Occured, Please Try Again!')
            return redirect('view_presentation')


@login_required(login_url='login_page')
def delete_presentation(request, id):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    data = PresentationSubmission.objects.get(id=id)
    student_group = data.student_group
    student_group.is_presentation_submitted = False 
    student_group.save()
    data.delete()
    messages.success(request, f' Details has been Deleted Successfully!')
    return redirect('view_presentation')


@login_required(login_url='login_page')
def add_record(request, group_id):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    group_id = group_id
    student_group = StudentGroup.objects.get(id=group_id)
    submission_date = student_group.record_submission_date
    current_time = timezone.now().date()
    if current_time > submission_date:
        messages.error(request, f'Sorry You Cannot Add Record After Submission Time!')
        return redirect('view_group')
    if request.method == "POST":
        form = RecordSubmissionForm(request.POST, request.FILES)
        topic_obj = TopicSubmission.objects.filter(student_group=student_group).first()
        
        uploaded_file = request.FILES.get('file')
        if not uploaded_file or not uploaded_file.name.lower().endswith('.pdf'):
            messages.error(request, 'Only PDF formats are allowed!')
            return redirect('view_group')

        if form.is_valid():
            instance = form.save(commit=False)
            instance.student_group_id = group_id
            instance.project_topic_id = topic_obj.id
            instance.status='Added'
            instance.save()
            student_group.is_record_submitted = True
            student_group.save()
            messages.success(request, f'Record Details has been Added Successfully!')
            return redirect('view_record')
        else:
            messages.success(request, f'Some Error Occured, Please Try Again!')
            return redirect('view_group')
    else:
        form = RecordSubmissionForm()
        context = {
            'form': form,
            'group_id': group_id
        } 
        return render(request,'Student/add_record.html', context)


@login_required(login_url='login_page')
def view_record(request):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')
    student = Student.objects.filter(admin=request.user).first()
    student_groups = student.studentgroup_set.all()
    data = RecordSubmission.objects.filter(student_group__in = student_groups).first()
    form =  RecordSubmissionForm(instance = data)
    context = {
        'data': data,
        'form': form
    }
    
    return render(request,'Student/view_record.html', context)


@login_required(login_url='login_page')
def edit_record(request):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    student = Student.objects.filter(admin=request.user).first()
    student_groups = student.studentgroup_set.all()
    data = RecordSubmission.objects.filter(student_group__in = student_groups).first()
    if request.method == "POST":
        form =  RecordSubmissionForm(request.POST,request.FILES, instance = data)
        if form.is_valid():
            form.save()
            messages.success(request, f'Details has been Added Successfully!')
            return redirect('view_record')
        else:
            messages.success(request, f'Some Error Occured, Please Try Again!')
            return redirect('view_record')


@login_required(login_url='login_page')
def delete_record(request, id):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    data = RecordSubmission.objects.get(id=id)
    student_group = data.student_group
    student_group.is_record_submitted = False 
    student_group.save()
    data.delete()
    messages.success(request, f' Details has been Deleted Successfully!')
    return redirect('view_record')
        

@login_required(login_url='login_page')
def add_project(request, group_id):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    group_id = group_id
    student_group = StudentGroup.objects.get(id=group_id)
    submission_date = student_group.record_submission_date
    current_time = timezone.now().date()
    if current_time > submission_date:
        messages.error(request, f'Sorry You Cannot Add Project After Submission Time!')
        return redirect('view_group')
    if request.method == "POST":
        form = ProjectSubmissionForm(request.POST, request.FILES)
        topic_obj = TopicSubmission.objects.filter(student_group=student_group).first()
        
        uploaded_file = request.FILES.get('file')
        if not uploaded_file or not uploaded_file.name.lower().endswith('.zip'):
            messages.error(request, 'Only ZIP formats are allowed!')
            return redirect('view_group')

        if form.is_valid():
            instance = form.save(commit=False)
            instance.student_group_id = group_id
            instance.project_topic_id = topic_obj.id
            instance.status='Added'
            instance.save()
            student_group.is_project_submitted = True
            student_group.save()
            messages.success(request, f'Project Details has been Added Successfully!')
            return redirect('view_project')
        else:
            messages.success(request, f'Some Error Occured, Please Try Again!')
            return redirect('view_group')
    else:
        form = ProjectSubmissionForm()
        context = {
            'form': form,
            'group_id': group_id
        } 
        return render(request,'Student/add_project.html', context)


@login_required(login_url='login_page')
def view_project(request):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    student = Student.objects.filter(admin=request.user).first()
    student_groups = student.studentgroup_set.all()
    data = ProjectSubmission.objects.filter(student_group__in = student_groups).first()
    form =  ProjectSubmissionForm(instance = data)
    context = {
        'data': data,
        'form': form
    }
    
    return render(request,'Student/view_project.html', context)


@login_required(login_url='login_page')
def edit_project(request):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    student = Student.objects.filter(admin=request.user).first()
    student_groups = student.studentgroup_set.all()
    data = ProjectSubmission.objects.filter(student_group__in = student_groups).first()
    if request.method == "POST":
        uploaded_file = request.FILES.get('file')
        if not uploaded_file or not uploaded_file.name.lower().endswith('.zip'):
            messages.error(request, 'Only ZIP formats are allowed!')
            return redirect('view_project')
        form =  ProjectSubmissionForm(request.POST,request.FILES, instance = data)
        if form.is_valid():
            form.save()
            messages.success(request, f'Details has been Added Successfully!')
            return redirect('view_project')
        else:
            messages.success(request, f'Some Error Occured, Please Try Again!')
            return redirect('view_project')


@login_required(login_url='login_page')
def delete_project(request, id):
    if not request.user.user_type == '3':
        messages.success(request, f'You are not Authorized to Perform this Action!')
        return redirect('doLogout')

    data = ProjectSubmission.objects.get(id=id)
    student_group = data.student_group
    student_group.is_project_submitted = False 
    student_group.save()
    data.delete()
    messages.success(request, f' Details has been Deleted Successfully!')
    return redirect('view_project')