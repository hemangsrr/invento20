from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.base import ContextMixin
from .models import Event, Event_register, Ambassador_register
from .forms import EventRegisterForm
class EventDetailView(DetailView):
    model = Event
    template_name = 'pages/event_detail.html'

def departmentview(request):

    if request.path == '/general/':
        template_name = 'pages/general.html'
        events = Event.objects.filter(category='gen')
        return render(request, template_name,
            {'events' : events }
        )

    else:
        if request.path == '/cse/':
            dept = 'cse'
        elif request.path == '/ece/':
            dept = 'ece'
        elif request.path == '/eee/':
            dept = 'eee'
        elif request.path == '/it/':
            dept = 'it'
        elif request.path == '/me/':
            dept = 'me'
        elif request.path == '/saptha/':
            dept = 'sta'

        template_name = 'pages/' + dept + '_dept.html'

        workshops = Event.objects.filter(category=dept, _type='wor')
        competitions = Event.objects.filter(category=dept, _type='com')
        shows = Event.objects.filter(category=dept, _type='sho')
        talks = Event.objects.filter(category=dept, _type='tal')


        return render(request, template_name, {
        'workshops' : workshops,
        'competitions' : competitions,
        'shows' : shows,
        'talks' : talks,
        })

def event_register_view(request):
    # form = EventRegisterForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     return redirect('home')
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        mobile = request.POST["phone"]
        referal_code = request.POST["referal_code"]
        event = request.POST["event"]

        event_register = Event_register(first_name=first_name, last_name=last_name, email=email, phone=mobile, referal_code=referal_code, event=event)
        event_register.save()
        return redirect('home')
    else:
        events = Event.objects.all().order_by('title')
        return render(request, 'pages/event_register.html', {'events': events})

def event_register(request):
    events = Event.objects.all().order_by('title')
    return render(request, 'pages/event_register.html', {'events': events})

def ambassador_register_view(request):
    # form = EventRegisterForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     return redirect('home')
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        mobile = request.POST["phone"]
        college = request.POST["college"]
        department = request.POST["department"]
        referal_code = request.POST["referal_code"]

        ambassador_register = Ambassador_register(first_name=first_name, last_name=last_name, email=email, phone=mobile, college=college, department=department, referal_code=referal_code)
        ambassador_register.save()
        return redirect('home')
    else:
        return render(request, 'pages/ambassador_register.html')

def campus_ambassador(request):
    return render(request, 'pages/ambassador_register.html')
