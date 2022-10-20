from django.urls import path
from .views import list, update_delete

urlpatterns = [
    path('', list),
    path("<str:id>/", update_delete)
]
