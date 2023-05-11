from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    """Отрисовываем список пользователей, находящихся в хранилище"""
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)

    for visit in visits:
        non_closed_visits += [
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': visit.format_duration,
            }
        ]

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
