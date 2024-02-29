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
    duration = fields.IntField(null=False)
    hallId = fields.ForeignKeyField(
        "models.TheaterHall",
        related_name="plays",
        on_delete=fields.RESTRICT,
        on_update=fields.CASCADE,
    )
    seasonId = fields.ForeignKeyField(
        "models.Season",
        related_name="plays",
        on_delete=fields.RESTRICT,
        on_update=fields.CASCADE,
    )


class Performance(Model):
    performanceId = fields.IntField(pk=True)
    duration = fields.IntField(null=False)
    datetime = fields.DatetimeField(null=False)


class Area(Model):
    areaId = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False)
    hallId = fields.ForeignKeyField(
        "models.TheaterHall",
        related_name="areas",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )


class Chair(Model):
    chairId = fields.IntField(pk=True)
    number = fields.IntField(null=False)
    row = fields.IntField(null=False)
    areaId = fields.ForeignKeyField(
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
    customerId = fields.ForeignKeyField(
        "models.CustomerProfile",
        related_name="purchases",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )


class Ticket(Model):
    ticketId = fields.IntField(pk=True)
    purchaseId = fields.ForeignKeyField(
        "models.TicketPurchase",
        related_name="tickets",
        on_delete=fields.SET_NULL,
        on_update=fields.CASCADE,
        null=True,
    )
    performanceId = fields.ForeignKeyField(
        "models.Performance",
        related_name="tickets",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    chairId = fields.ForeignKeyField(
        "models.Chair",
        related_name="tickets",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    areaId = fields.ForeignKeyField(
        "models.Area",
        related_name="tickets",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    price = fields.FloatField(null=False)


class Act(Model):
    actId = fields.IntField(pk=True)
    number = fields.IntField(null=False)
    name = fields.CharField(max_length=255, null=False)
    playId = fields.ForeignKeyField(
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
    actorId = fields.ForeignKeyField(
        "models.Actor",
        related_name="roles",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    roleId = fields.ForeignKeyField(
        "models.Role",
        related_name="actors",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("actorId", "roleId")


class ActorPlay(Model):
    actorPlayId = fields.IntField(pk=True)
    actorId = fields.ForeignKeyField(
        "models.Actor",
        related_name="plays",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    playId = fields.ForeignKeyField(
        "models.Play",
        related_name="actors",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("actorId", "playId")


class EmployeePlay(Model):
    employeePlayId = fields.IntField(pk=True)
    employeeId = fields.ForeignKeyField(
        "models.Employee",
        related_name="plays",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    playId = fields.ForeignKeyField(
        "models.Play",
        related_name="employees",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("employeeId", "playId")


class ActRole(Model):
    actRoleId = fields.IntField(pk=True)
    roleId = fields.ForeignKeyField(
        "models.Role",
        related_name="acts",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )
    actId = fields.ForeignKeyField(
        "models.Act",
        related_name="roles",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )

    class Meta:
        unique_together = ("roleId", "actId")
