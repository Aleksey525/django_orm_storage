from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.visits_duration import get_duration
from datacenter.visits_duration import format_duration
from datacenter.visits_duration import is_visits_long
from django.shortcuts import render
from datetime import datetime, timedelta


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        name = visit.passcard.owner_name
        entered = visit.entered_at
        duration = format_duration(get_duration(visit))
        is_strange = is_visits_long(visit, minutes=60)
        fields = dict(who_entered=name, entered_at=entered, duration=duration, is_strange=is_strange)
        non_closed_visits.append(fields)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
