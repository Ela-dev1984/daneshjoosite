from django.shortcuts import render, redirect
from .models import Student


def home(request):

    return render(request, "home.html")


def show_student(request):
    all_students = Student.objects.all()
    return render(request, "show.html", {"all_students": all_students})


def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        avg = request.POST.get("average")
        bio = request.POST.get("bio")

        Student.objects.create(name=name, average=avg, bio=bio)
        return redirect("show")
    return render(request, "add.html")


def delete_student(request, id):
    for_delete = Student.objects.get(id=id)
    for_delete.delete()
    return redirect("home")


def sort_student(request):
    min_avg = request.GET.get("min_avg")
    max_avg = request.GET.get("max_avg")

    students = Student.objects.all()

    if min_avg and max_avg:
        students = students.filter(average__gte=min_avg, average__lte=max_avg)

        return render(request, "showfilter.html", {"students": students})
    return render(request, "sort.html", {"students": students})


def profile_student(request, id):
    student = Student.objects.get(id=id)
    return render(request, "profile.html", {"student": student})
