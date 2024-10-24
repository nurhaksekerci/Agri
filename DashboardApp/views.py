from django.shortcuts import render

# base.html şablonunu yükleyen view
def home(request):
    return render(request, 'main/base.html')
# Calender
def apps_calendar(request):
    return render(request, 'calender/apps-calendar.html')


# Contacts
def apps_contacts_grid(request):
    return render(request, 'contact/apps-contacts-grid.html')

def apps_contacts_profile(request):
    return render(request, 'contact/apps-contacts-profile.html')


# Tasks
def tasks_create(request):
    return render(request, 'tasks/tasks-create.html')

def tasks_kanban(request):
    return render(request, 'tasks/tasks-kanban.html')

def tasks_list(request):
    return render(request, 'tasks/tasks-list.html')

# Ekstralar

def apex(request):
    return render(request, "ekstralar/charts-apex.html")

def echart(request):
    return render(request, "ekstralar/charts-echart.html")

def knob(request):
    return render(request, "ekstralar/charts-knob.html")

def datatable(request):
    return render(request, "ekstralar/tables-datatable.html")

def editable(request):
    return render(request, "ekstralar/tables-editable.html")

def responsiv(request):
    return render(request, "ekstralar/tables-responsive.html")


# Müşteri Sayfaları

def gübre(request):
    return render(request, 'müşterisayfaları/ilac-gübre.html')

def ipm(request):
    return render(request, 'müşterisayfaları/ipm.html')

def tohumcular(request):
    return render(request, 'müşterisayfaları/tohumcular.html')
