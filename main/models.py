from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    year = models.IntegerField()
    genre = models.CharField(max_length=100, choices=[('фантастика', 'fantasy'), ('боевик', 'thriller'), ('детектив', 'detective'), ('комедия', 'comedy'), ('мелодрама', 'melodrama'), ('научный', 'science'), ('приключения', 'adventures'), ('ужасы', 'horror'), ('спорт', 'sport'), ('мультфильм', 'cartoon'), ('документальный', 'documentary')])
    producer = models.CharField(max_length=100)
    actors = models.TextField()
    duration = models.CharField(max_length=100)
    image = models.ImageField(upload_to='films', null=True)
    video = models.TextField()

    def __str__(self) -> str:
        return self.title


    @property
    def average_rating(self):
        ratings = self.ratings.all()
        values = []
        for rating in ratings :
            values.append(rating.value)
        if values:
            return sum(values) / len(values)
        return 0

    class Meta:
        ordering = ['id']