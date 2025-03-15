import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.serializers.json import DjangoJSONEncoder
from .models import UserLocation
from .forms import UserLocationForm

def user_create(request):
    if request.method == 'POST':
        form = UserLocationForm(request.POST)
        if form.is_valid():
            user_location = form.save()
            # Prepare context for the homepage.
            users = list(UserLocation.objects.values())
            users_json = json.dumps(users, cls=DjangoJSONEncoder)
            context = {
                'users_json': users_json,
                'current_user_id': user_location.id,
            }
            html = render_to_string('index.html', context, request=request)
            response = HttpResponse(html)
            response['HX-Push'] = '/?current_user_id=' + str(user_location.id)
            return response
    else:
        form = UserLocationForm()
    return render(request, 'user_form.html', {'form': form})

def map_view(request):
    users = list(UserLocation.objects.values())
    users_json = json.dumps(users, cls=DjangoJSONEncoder)
    current_user_id = request.GET.get('current_user_id', None)
    return render(request, 'index.html', {
        'users_json': users_json,
        'current_user_id': current_user_id,
    })
