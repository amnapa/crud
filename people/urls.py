from django.urls import path
from . import views

urlpatterns = [
    path('person/view/<int:id>', views.view_person),
    path('person/list/', views.list_person),
    path('person/add/', views.add_person),
    path('person/update/<int:id>', views.update_person),
    path('person/delete/<int:id>', views.delete_person),
    path('person/type/', views.person_type),
]