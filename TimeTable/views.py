from django.shortcuts import *
from django.http import *
from .models import *
from django.core import *
from rest_framework.views import *
from rest_framework.response import *
from .serializers import *

# Create your views here.
def index(request):
	list_of_events = Event.objects.all()
	context = {'list_of_events': list_of_events}
	return render(request, 'TimeTable/index.html', context)

# def detail(request, event_id):
# 	event = get_object_or_404(Event, pk=event_id)
# 	event_serialized = model_to_dict(event)
#     return JsonResponse(json.dumps(event_serialized))

# def all_element(request):
#     events = Event.objects.all()
#     events_serialized = serializers.serialize('json', events)
#     return JsonResponse(events_serialized, safe=False)
class EventView(APIView):
	def get(self, request):
		event = Event.objects.all()
		serializer = EventSerializer(event, many=True)
		return Response(serializer.data)