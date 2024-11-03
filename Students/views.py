from django.contrib import messages
from django.shortcuts import render, redirect

from .form import StudentForm
from .models import Student


def student_create(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student_data = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "other_names": form.cleaned_data["other_names"],
                "date_of_birth": form.cleaned_data["date_of_birth"],
                "gender": form.cleaned_data["gender"],
                "parent_first_name": form.cleaned_data["parent_first_name"],
                "parent_last_name": form.cleaned_data["parent_last_name"],
                "parent_other_names": form.cleaned_data["parent_other_names"],
                "parent_email": form.cleaned_data["parent_email"],
                "parent_phone_number_1": form.cleaned_data["parent_phone_number_1"],
            }
            if Student.objects.filter(**student_data).exists():
                messages.error(request, "Student already exists")
            else:
                form.save()
                messages.success(request, "Student created successfully")
                return redirect("student_create")
    context = {"form": form}
    return render(request, "Students/student_create.html", context)


def student_list(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "Students/student_list.html", context)


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {"student": student}
    return render(request, "Students/student_detail.html", context)


def student_update(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student_data = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "other_names": form.cleaned_data["other_names"],
                "date_of_birth": form.cleaned_data["date_of_birth"],
                "gender": form.cleaned_data["gender"],
                "parent_first_name": form.cleaned_data["parent_first_name"],
                "parent_last_name": form.cleaned_data["parent_last_name"],
                "parent_other_names": form.cleaned_data["parent_other_names"],
                "parent_email": form.cleaned_data["parent_email"],
                "parent_phone_number_1": form.cleaned_data["parent_phone_number_1"],
            }
            if Student.objects.filter(**student_data).exists():
                messages.error(request, "Student already exists")
            else:
                form.save()
                messages.success(request, "Student updated successfully")
                return redirect("student_list")
    context = {"form": form}
    return render(request, "Students/student_update.html", context)


def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    redirect("student_list")
    messages.success(request, "Student deleted successfully")
