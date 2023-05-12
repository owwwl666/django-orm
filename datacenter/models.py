from django.db import models
from django.utils import timezone

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        """Находим время, которое посетитель провел в хранилище.
           Если он до сих пор там, то возвращаем количество времени, которое он находится в хранилище.
           Переводим время в секунды.
        """
        delta = timezone.localtime(timezone.now()) - self.entered_at if not self.leaved_at \
            else self.leaved_at - self.entered_at
        return delta.total_seconds()

    def format_duration(self):
        """Форматируем в строку, отрбрасывая милисекунды."""
        return f'{self.get_duration():.0f} секунд'

    def is_visit_long(self, minutes=60):
        """Переводим секунды в минуты и сравниваем с заданным параметром"""
        return self.get_duration() / 60 > minutes
