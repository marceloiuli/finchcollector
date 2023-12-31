from django.db import models
from django.urls import reverse
from datetime import date

PLAYTIME = (
    ('S', 'Sing'),
    ('P', 'Pet'),
    ('F', 'Feed')
)


# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('snacks_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    snacks = models.ManyToManyField(Snack)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
    def play_for_today(self):
        return self.playing_set.filter(date=date.today()).count() >= len(PLAYTIME)
    
class Playing(models.Model):
    date = models.DateField('Play date')
    play = models.CharField(
        max_length=1,
        choices=PLAYTIME,
        default=PLAYTIME[0][0]
    )

    finch = models.ForeignKey(
        Finch,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_play_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']