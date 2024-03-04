from tortoise.models import Model
from tortoise import fields


class TheaterHall(Model):
    hall_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)
    capacity = fields.IntField(null=False)


class Season(Model):
    season_id = fields.IntField(pk=True)
    season = fields.CharField(max_length=255, null=False)
    year = fields.IntField(null=False)


class Play(Model):
    play_id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, null=False)
    author = fields.CharField(max_length=255, null=False)
    duration = fields.CharField(max_length=255, null=False)
    hall = fields.ForeignKeyField(
        "models.TheaterHall",
        related_name="plays",
        on_delete=fields.RESTRICT,
        on_update=fields.CASCADE,
    )
    season = fields.ForeignKeyField(
        "models.Season",
        related_name="plays",
        on_delete=fields.RESTRICT,
        on_update=fields.CASCADE,
    )


class Performance(Model):
    performance_id = fields.IntField(pk=True)
    datetime = fields.DatetimeField(null=False)
    hall = fields.ForeignKeyField(
        "models.TheaterHall",
        related_name="performances",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
        db_column="hall_id",
    )
    play = fields.ForeignKeyField(
        "models.Play",
        related_name="performances",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )


class Area(Model):
    area_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)
    hall = fields.ForeignKeyField(
        "models.TheaterHall",
        related_name="areas",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("name", "hall_id")


class Chair(Model):
    chair_id = fields.CharField(pk=True, max_length=255)
    number = fields.IntField(null=False)
    row = fields.IntField(null=False)
    area = fields.ForeignKeyField(
        "models.Area",
        related_name="chairs",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    hall = fields.ForeignKeyField(
        "models.TheaterHall",
        related_name="chairs",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("number", "row", "area_id", "hall_id")


class CustomerProfile(Model):
    customer_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)
    address = fields.CharField(max_length=255, null=False)
    phone = fields.CharField(max_length=255, null=False)


class CustomerGroup(Model):
    group_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)


class TicketPurchase(Model):
    purchase_id = fields.IntField(pk=True)
    datetime = fields.DatetimeField(null=False)
    customer = fields.ForeignKeyField(
        "models.CustomerProfile",
        related_name="purchases",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )


class TicketPrice(Model):
    ticketPrice_id = fields.IntField(pk=True)
    price = fields.FloatField(null=False)
    play = fields.ForeignKeyField(
        "models.Play",
        related_name="prices",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    group = fields.ForeignKeyField(
        "models.CustomerGroup",
        related_name="prices",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("group_id", "play_id")


class Ticket(Model):
    ticket_id = fields.IntField(pk=True)
    ticketPrice = fields.ForeignKeyField(
        "models.TicketPrice",
        related_name="tickets",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    purchase = fields.ForeignKeyField(
        "models.TicketPurchase",
        related_name="tickets",
        on_delete=fields.SET_NULL,
        on_update=fields.CASCADE,
        null=True,
    )
    performance = fields.ForeignKeyField(
        "models.Performance",
        related_name="tickets",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    area = fields.ForeignKeyField(
        "models.Area",
        related_name="tickets",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )


class TicketChair(Model):
    ticketChair_id = fields.IntField(pk=True)
    ticket = fields.ForeignKeyField(
        "models.Ticket",
        related_name="chairs",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    chair = fields.ForeignKeyField(
        "models.Chair",
        related_name="tickets",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("ticket_id", "chair_id")


class Act(Model):
    act_id = fields.IntField(pk=True)
    number = fields.IntField(null=False)
    name = fields.CharField(max_length=255, null=False)
    play = fields.ForeignKeyField(
        "models.Play",
        related_name="acts",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("number", "play_id")


class Role(Model):
    role_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)


class Actor(Model):
    actor_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)
    email = fields.CharField(max_length=255, null=False)
    status = fields.BooleanField(null=False)


class Employee(Model):
    employee_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)
    email = fields.CharField(max_length=255, null=False)
    status = fields.BooleanField(null=False)


class ActorRole(Model):
    actorRole_id = fields.IntField(pk=True)
    actor = fields.ForeignKeyField(
        "models.Actor",
        related_name="roles",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    role = fields.ForeignKeyField(
        "models.Role",
        related_name="actors",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("actor_id", "role_id")


class ActorPlay(Model):
    actorPlay_id = fields.IntField(pk=True)
    actor = fields.ForeignKeyField(
        "models.Actor",
        related_name="plays",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    play = fields.ForeignKeyField(
        "models.Play",
        related_name="actors",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("actor_id", "play_id")


class EmployeePlay(Model):
    employeePlay_id = fields.IntField(pk=True)
    employee = fields.ForeignKeyField(
        "models.Employee",
        related_name="plays",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    play = fields.ForeignKeyField(
        "models.Play",
        related_name="employees",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("employee_id", "play_id")


class ActRole(Model):
    actRole_id = fields.IntField(pk=True)
    role = fields.ForeignKeyField(
        "models.Role",
        related_name="acts",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    act = fields.ForeignKeyField(
        "models.Act",
        related_name="roles",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("role_id", "act_id")
