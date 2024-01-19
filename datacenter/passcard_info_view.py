from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.visits_duration import get_duration
from datacenter.visits_duration import format_duration
from datacenter.visits_duration import is_visits_long
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        entered = visit.entered_at
        duration = format_duration(get_duration(visit))
        is_strange = is_visits_long(visit, minutes=60)
        fields = dict(entered_at=entered, duration=duration, is_strange=is_strange)
        this_passcard_visits.append(fields)


    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
