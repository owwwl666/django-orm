from datacenter.models import Passcard, Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    """Отображаем все визиты человека в хранилище."""
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        this_passcard_visits += [
            {
                'entered_at': visit.entered_at,
                'duration': visit.format_duration,
                'is_strange': visit.is_visit_long
            },
        ]

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)
