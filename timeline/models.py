from django.db import models
from competition.models import Event


class TimelineEventType(models.Model):
    class Meta:
        verbose_name = 'Typ udalosti na časovej osi'
        verbose_name_plural = 'Typy udalostí na časovej osi'
        ordering = ['series', 'order', ]
    name = models.CharField(
        max_length=50,
        verbose_name='názov'
    )
    icon = models.ImageField(verbose_name='ikona')
    default_text = models.TextField(verbose_name='vzor textu')


class TimelineEvent(models.Model):
    class Meta:
        verbose_name = 'Udalosť na časovej osi'
        verbose_name_plural = 'Udalosti na časovej osi'
        ordering = ['series', 'order', ]

    event = models.ForeignKey(
        Event, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(TimelineEventType, verbose_name='typ udalosti')
    show_after = models.DateTimeField(verbose_name='dátum a čas zverejnenia')
    additional_info = models.TextField(verbose_name='doplňujúci text')
