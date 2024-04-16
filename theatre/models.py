import pathlib
import uuid

from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name + " " + self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TheatreHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self):
        return self.name


def play_image_path(instance, filename) -> pathlib.Path:
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}" + (
        pathlib.Path(filename).suffix)
    return pathlib.Path("upload/plays/") / pathlib.Path(filename)


class Play(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=255)
    actors = models.ManyToManyField(Actor, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    image = models.ImageField(null=True, upload_to=play_image_path)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "plays"

    def __str__(self):
        return self.title


class Performance(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    show_time = models.DateTimeField()
    theatre_hall = models.ForeignKey(TheatreHall, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-show_time"]

    def __str__(self):
        return f"{self.play} at {self.show_time} in {self.theatre_hall.name}"


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.created_at)


class Ticket(models.Model):
    performance = models.ForeignKey(
        Performance, on_delete=models.CASCADE, related_name="tickets"
    )
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="tickets"
    )
    row = models.IntegerField()
    seat = models.IntegerField()

    @staticmethod
    def validate_seat(seat: int, num_seats: int, error_to_raise):
        if not (1 <= seat <= num_seats):
            raise error_to_raise(
                {
                    "seat": f"{seat} "
                            f"number must be in range: "
                            f"(1, {num_seats}): "
                            f"but we got {num_seats})"
                }
            )

    def clean(self):
        Ticket.validate_seat(
            self.seat, self.performance.theatre_hall.seats_in_row, ValueError
        )

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        self.full_clean()
        super(Ticket, self).save(
            force_insert, force_update, using, update_fields
        )

    def __str__(self):
        return (
            f"{str(self.performance)} (row: {self.row}, seat: {self.seat})"
        )

    class Meta:
        unique_together = ("performance", "row", "seat")
