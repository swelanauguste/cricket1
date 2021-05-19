from django.db import models
from django.conf import settings
from django.urls import reverse


Users = settings.AUTH_USER_MODEL


class Role(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    pic = models.URLField(blank=True)
    default_pic = models.URLField(
        editable=False,
        default="https://drive.google.com/file/d/1W50JnkJ0V1U0grarMPozNhj-VTxMexTA/preview",
    )
    nickname = models.CharField(max_length=200, blank=True)
    role = models.ManyToManyField(Role)
    matches = models.PositiveIntegerField(default=0)
    batting_innings = models.PositiveIntegerField(default=0)
    fours = models.PositiveIntegerField("4s", default=0)
    sixes = models.PositiveIntegerField("6s", default=0)
    no = models.PositiveIntegerField("not out", default=0)
    batting_runs = models.PositiveIntegerField(default=0)
    hs = models.PositiveIntegerField("highest score", default=0)
    hundreds = models.PositiveIntegerField("100s", default=0)
    fifties = models.PositiveIntegerField("50s", default=0)
    bowling_innings = models.PositiveIntegerField(default=0)
    catches = models.PositiveIntegerField("Ct", default=0)
    stumped = models.PositiveIntegerField("St", default=0)
    balls = models.PositiveIntegerField(default=0)
    bowling_runs = models.PositiveIntegerField(default=0)
    wkts = models.PositiveIntegerField("wickets", default=0)

    def get_absolute_url(self):
        return reverse("users:profile-detail", args=[str(self.id)])

    def get_profile_image(self):
        if self.pic:
            return self.pic
        return self.default_pic

    @property
    def get_overs(self):
        return round(self.balls / 6, 1)

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.user.username

    @property
    def get_batting_average(self):
        if self.batting_runs != 0 or self.batting_innings != 0 or self.no != 0:
            return self.batting_runs / (self.batting_innings - self.no)
        return str("-")

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.user.username
