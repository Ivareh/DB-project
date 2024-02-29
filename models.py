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
    price = fields.FloatField(null=False)
    
    
class Act(Model):
    actId = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, null=False)
    duration = fields.IntField(null=False)
    playId = fields.ForeignKeyField(
        "models.Play",
        related_name="acts",
        on_delete=fields.CASCADE,
        on_update=fields.CASCADE,
    )