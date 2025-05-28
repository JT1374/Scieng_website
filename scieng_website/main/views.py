# Imports.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Project
from django.contrib.auth.decorators import login_required


# All views functions.
def signup_view(request):
    """
    Handles user registration.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered signup page or a redirect after successful signup.

    Return type:
        HttpResponse
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # automatically log the user in
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})


def login_view(request):
    """
    Handles user login.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered login page or a redirect after successful login.

    Return type:
        HttpResponse
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def logout_view(request):
    """
    Handles user logout.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered logout page or a redirect after logout.

    Return type:
        HttpResponse
    """
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'main/logout.html')


def home(request):
    """
    Renders the home page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.

    Return type:
        HttpResponse
    """
    return render(request, 'main/home.html')


def project_list(request):
    """
    Displays a list of all projects.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered project list page.

    Return type:
        HttpResponse
    """
    projects = Project.objects.all()
    return render(request, 'main/project_list.html', {'projects': projects})


@login_required
def project_detail(request, project_id):
    """
    Displays details for a specific project.

    Parameters:
        request (HttpRequest): The HTTP request object.
        project_id (int): The ID of the project.

    Returns:
        HttpResponse: The rendered project detail page.

    Return type:
        HttpResponse
    """
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'main/project_detail.html', {'project': project})
