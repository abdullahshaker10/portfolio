from django.shortcuts import render
from .models import Job
# Create your views here.


def homepage(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})


def details(request, job_id):
    job = Job.objects.get(id=job_id)

    return render(request, 'jobs/details.html', {'job': job})
