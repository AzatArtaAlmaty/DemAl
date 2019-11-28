from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('eventsList', eventsList, name='eventsList'),
    path('events', events, name='events'),
    path('eventDesc/<int:event_id>', eventDesc, name='eventDesc'),
    path('authorization', authorization, name='authorization'),
    path('test', EventView.as_view()),
    path('order', OrderView.as_view()),
    path('xa', newindex, name='newindex'),
    # path('<int:event_id>/', views.detail, name='detail'),
    # path('AllElements/', views.all_element, name='all_element'),
    # path('/<str:field_name>', views.all_element, name='all_element'),
]