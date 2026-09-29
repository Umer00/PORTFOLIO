from django.shortcuts import render, redirect
from .models import Project, Skill, Contact


def home(request):
    projects = Project.objects.all().order_by('-created_at')
    skills = Skill.objects.all()

    return render(request, 'portfolio_app/home.html', {
        'projects': projects,
        'skills': skills,
    })


def projects(request):
    projects = Project.objects.all().order_by('-created_at')

    return render(request, 'portfolio_app/projects.html', {
        'projects': projects,
    })


def skills(request):
    skills = Skill.objects.all()

    return render(request, 'portfolio_app/skills.html', {
        'skills': skills,
    })


def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        return redirect('contact')

    return render(request, 'portfolio_app/contact.html')