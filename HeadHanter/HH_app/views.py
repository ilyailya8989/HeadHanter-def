from django.shortcuts import render, get_object_or_404, redirect
from .models import Vacancy, Resume
from .forms import VacancyForm, ResumeForm
from django.contrib.auth.decorators import login_required

# Вакансии
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'HH_app/vacancy_list.html', {'vacancies': vacancies})

def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'HH_app/vacancy_detail.html', {'vacancy': vacancy})

@login_required
def vacancy_create(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm()
    return render(request, 'HH_app/vacancy_form.html', {'form': form})

@login_required
def vacancy_update(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm(instance=vacancy)
    return render(request, 'HH_app/vacancy_form.html', {'form': form})

@login_required
def vacancy_delete(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == 'POST':
        vacancy.delete()
        return redirect('vacancy_list')
    return render(request, 'HH_app/vacancy_confirm_delete.html', {'vacancy': vacancy})

# Резюме
def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'HH_app/resume_list.html', {'resumes': resumes})

def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'HH_app/resume_detail.html', {'resume': resume})

@login_required
def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'HH_app/resume_form.html', {'form': form})

@login_required
def resume_update(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'HH_app/resume_form.html', {'form': form})

@login_required
def resume_delete(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == 'POST':
        resume.delete()
        return redirect('resume_list')
    return render(request, 'HH_app/resume_confirm_delete.html', {'resume': resume})
