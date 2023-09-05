from django.db import models

from accounts.models import Listener
from songs.models import Song


class Like(models.Model):
    user = models.ForeignKey(Listener, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} liked "{self.song}"'


class Comment(models.Model):
    user = models.ForeignKey(
        Listener, on_delete=models.CASCADE, related_name="user_comments"
    )
    song = models.ForeignKey(
        Song, on_delete=models.CASCADE, related_name="song_comments"
    )
    reply = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="reply_comments",
        blank=True,
        null=True,
    )
    is_reply = models.BooleanField(default=False)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.user}: {self.content[:30]}"


class Playlist(models.Model):
    owner = models.ForeignKey(Listener, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.owner}"
