from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Anasayfa için yönlendirme
    # Calendar
    path('calendar/', views.apps_calendar, name='apps-calendar'),
    

    # Contacts
    path('contacts-grid/', views.apps_contacts_grid, name='apps-contacts-grid'),
    path('contacts-profile/', views.apps_contacts_profile, name='apps-contacts-profile'),

    # Tasks
    path('tasks/create/', views.tasks_create, name='tasks-create'),
    path('tasks/kanban/', views.tasks_kanban, name='tasks-kanban'),
    path('tasks/list/', views.tasks_list, name='tasks-list'),

    # Ekstralar
    path("ekstralar/apex/", views.apex, name="apex"),
    path("ekstralar/echart/", views.echart, name="echart"),
    path("ekstralar/knob/", views.knob, name="knob"),
    path("ekstralar/datatable/", views.datatable, name="datatable"),
    path("ekstralar/editable/", views.editable, name="editable"),
    path("ekstralar/responsiv/", views.responsiv, name="responsiv"),
    
    # Müşteri Sayfaları
    path('gübre/', views.gübre, name='gübre'),
    path('ipm/', views.ipm, name='ipm'),
    path('tohumcular/', views.tohumcular, name='tohumcular'),
]
