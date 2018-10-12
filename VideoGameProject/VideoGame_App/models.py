from django.db import models


class Game_Model(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.title + ' is the genre of ' + self.genre