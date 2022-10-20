from django.db import models

CLEAN = (
    ('T', 'Teeth'),
    ('H', 'Hair'),
    ('N', 'Nails')
)

# Create your models here.
class Capybara(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    image = models.TextField(max_length=500)

class Cleaning(models.Model):
    date = models.DateField('cleaning date')
    clean = models.CharField(max_length=1, choices=CLEAN, default=CLEAN[0][0])

    capybara = models.ForeignKey(Capybara, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_clean_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']