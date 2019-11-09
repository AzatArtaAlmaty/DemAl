from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('test/', EventView.as_view()),
    # path('<int:event_id>/', views.detail, name='detail'),
    # path('AllElements/', views.all_element, name='all_element'),
    # path('/<str:field_name>', views.all_element, name='all_element'),
]