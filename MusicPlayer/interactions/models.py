from django.db import models

from accounts.models import Listener
from songs.models import Song


class Like(models.Model):
    user = models.ForeignKey(Listener, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} liked "{self.song}"'

