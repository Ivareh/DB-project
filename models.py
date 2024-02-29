from tortoise.models import Model
from tortoise import fields


class TheaterHall(Model):
    hallId = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)
    capasity = fields.IntField(null=False)


class Season(Model):
    seasonId = fields.IntField(pk=True)
    season = fields.CharField(max_length=255, null=False)
    year = fields.IntField(null=False)


class Play(Model):
    playId = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, null=False)
    author = fields.CharField(max_length=255, null=False)
    duration = fields.CharField(max_length=255, null=False)
    hall = fields.relational.ForeignKeyField(
        "models.TheaterHall",
        related_name="plays",
        on_delete=fields.RESTRICT,
        on_update=fields.CASCADE,
    )
    season = fields.relational.ForeignKeyField(
        "models.Season",
        related_name="plays",
        on_delete=fields.RESTRICT,
        on_update=fields.CASCADE,
    )


class Performance(Model):
    performanceId = fields.IntField(pk=True)
    datetime = fields.DatetimeField(null=False)
    hall = fields.relational.ForeignKeyField(
        "models.TheaterHall",
        related_name="performances",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    play = fields.relational.ForeignKeyField(
        "models.Play",
        related_name="performances",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )


class Area(Model):
    areaId = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)
    hallId = fields.relational.ForeignKeyField(
        "models.TheaterHall",
        related_name="areas",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )


class Chair(Model):
    chairId = fields.IntField(pk=True)
    number = fields.IntField(null=False)
    row = fields.IntField(null=False)
    areaId = fields.relational.ForeignKeyField(
        "models.Area",
        related_name="chairs",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("number", "row", "areaId")


class CustomerProfile(Model):
    customerId = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)
    address = fields.CharField(max_length=255, null=False)
    phone = fields.CharField(max_length=255, null=False)


class CustomerGroup(Model):
    groupId = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)


class TicketPurchase(Model):
    purchaseId = fields.IntField(pk=True)
    datetime = fields.DatetimeField(null=False)
    customerId = fields.relational.ForeignKeyField(
        "models.CustomerProfile",
        related_name="purchases",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )


class Ticket(Model):
    ticketId = fields.IntField(pk=True)
    purchaseId = fields.relational.ForeignKeyField(
        "models.TicketPurchase",
        related_name="tickets",
        on_delete=fields.SET_NULL,
        on_update=fields.CASCADE,
        null=True,
    )
    performanceId = fields.relational.ForeignKeyField(
        "models.Performance",
        related_name="tickets",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    chairId = fields.relational.ForeignKeyField(
        "models.Chair",
        related_name="tickets",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    areaId = fields.relational.ForeignKeyField(
        "models.Area",
        related_name="tickets",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    customerGroupId = fields.relational.ForeignKeyField(
        "models.CustomerGroup",
        related_name="tickets",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    playId = fields.relational.ForeignKeyField(
        "models.Play",
        related_name="tickets",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )


class TicketPrice(Model):
    ticketPriceId = fields.IntField(pk=True)
    price = fields.FloatField(null=False)
    playId = fields.relational.ForeignKeyField(
        "models.Play",
        related_name="ticketPrices",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    groupId = fields.relational.ForeignKeyField(
        "models.CustomerGroup",
        related_name="ticketPrices",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    ticketId = fields.relational.ForeignKeyField(
        "models.Ticket",
        related_name="ticketPrices",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("playId", "groupId", "ticketId")


class Act(Model):
    actId = fields.IntField(pk=True)
    number = fields.IntField(null=False)
    name = fields.CharField(max_length=255, null=False)
    playId = fields.relational.ForeignKeyField(
        "models.Play",
        related_name="acts",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("number", "playId")


class Role(Model):
    roleId = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)


class Actor(Model):
    actorId = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)
    email = fields.CharField(max_length=255, null=False)
    status = fields.BooleanField(null=False)


class Employee(Model):
    employeeId = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)
    email = fields.CharField(max_length=255, null=False)
    status = fields.BooleanField(null=False)


class ActorRole(Model):
    actorRoleId = fields.IntField(pk=True)
    actorId = fields.relational.ForeignKeyField(
        "models.Actor",
        related_name="roles",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    roleId = fields.relational.ForeignKeyField(
        "models.Role",
        related_name="actors",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("actorId", "roleId")


class ActorPlay(Model):
    actorPlayId = fields.IntField(pk=True)
    actorId = fields.relational.ForeignKeyField(
        "models.Actor",
        related_name="plays",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    playId = fields.relational.ForeignKeyField(
        "models.Play",
        related_name="actors",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("actorId", "playId")


class EmployeePlay(Model):
    employeePlayId = fields.IntField(pk=True)
    employeeId = fields.relational.ForeignKeyField(
        "models.Employee",
        related_name="plays",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    playId = fields.relational.ForeignKeyField(
        "models.Play",
        related_name="employees",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("employeeId", "playId")


class ActRole(Model):
    actRoleId = fields.IntField(pk=True)
    roleId = fields.relational.ForeignKeyField(
        "models.Role",
        related_name="acts",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    actId = fields.relational.ForeignKeyField(
        "models.Act",
        related_name="roles",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("roleId", "actId")
