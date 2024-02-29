import models

from tortoise.contrib.pydantic import pydantic_model_creator



TheaterHall_Pydantic = pydantic_model_creator(models.TheaterHall)
TheaterHallIn_Pydantic = pydantic_model_creator(models.TheaterHall, name="TheaterHallIn", exclude_readonly=True)

Season_Pydantic = pydantic_model_creator(models.Season)
SeasonIn_Pydantic = pydantic_model_creator(models.Season, name="SeasonIn", exclude_readonly=True)

Play_Pydantic = pydantic_model_creator(models.Play)
PlayIn_Pydantic = pydantic_model_creator(models.Play, name="PlayIn", exclude_readonly=True)

Performance_Pydantic = pydantic_model_creator(models.Performance)
PerformanceIn_Pydantic = pydantic_model_creator(models.Performance, name="PerformanceIn", exclude_readonly=True)

Area_Pydantic = pydantic_model_creator(models.Area)
AreaIn_Pydantic = pydantic_model_creator(models.Area, name="AreaIn", exclude_readonly=True)

Chair_Pydantic = pydantic_model_creator(models.Chair)
ChairIn_Pydantic = pydantic_model_creator(models.Chair, name="ChairIn", exclude_readonly=True)

CustomerProfile_Pydantic = pydantic_model_creator(models.CustomerProfile)
CustomerProfileIn_Pydantic = pydantic_model_creator(models.CustomerProfile, name="CustomerProfileIn", exclude_readonly=True)

CustomerGroup_Pydantic = pydantic_model_creator(models.CustomerGroup)
CustomerGroupIn_Pydantic = pydantic_model_creator(models.CustomerGroup, name="CustomerGroupIn", exclude_readonly=True)

TicketPurchase_Pydantic = pydantic_model_creator(models.TicketPurchase)
TicketPurchaseIn_Pydantic = pydantic_model_creator(models.TicketPurchase, name="TicketPurchaseIn", exclude_readonly=True)

Ticket_Pydantic = pydantic_model_creator(models.Ticket)
TicketIn_Pydantic = pydantic_model_creator(models.Ticket, name="TicketIn", exclude_readonly=True)

Act_Pydantic = pydantic_model_creator(models.Act)
ActIn_Pydantic = pydantic_model_creator(models.Act, name="ActIn", exclude_readonly=True)

Role_Pydantic = pydantic_model_creator(models.Role)
RoleIn_Pydantic = pydantic_model_creator(models.Role, name="RoleIn", exclude_readonly=True)

Actor_Pydantic = pydantic_model_creator(models.Actor)
ActorIn_Pydantic = pydantic_model_creator(models.Actor, name="ActorIn", exclude_readonly=True)

Employee_Pydantic = pydantic_model_creator(models.Employee)
EmployeeIn_Pydantic = pydantic_model_creator(models.Employee, name="EmployeeIn", exclude_readonly=True)

ActorRole_Pydantic = pydantic_model_creator(models.ActorRole)
ActorRoleIn_Pydantic = pydantic_model_creator(models.ActorRole, name="ActorRoleIn", exclude_readonly=True)

ActorPlay_Pydantic = pydantic_model_creator(models.ActorPlay)
ActorPlayIn_Pydantic = pydantic_model_creator(models.ActorPlay, name="ActorPlayIn", exclude_readonly=True)

EmployeePlay_Pydantic = pydantic_model_creator(models.EmployeePlay)
EmployeePlayIn_Pydantic = pydantic_model_creator(models.EmployeePlay, name="EmployeePlayIn", exclude_readonly=True)

ActRole_Pydantic = pydantic_model_creator(models.ActRole)
ActRoleIn_Pydantic = pydantic_model_creator(models.ActRole, name="ActRoleIn", exclude_readonly=True)




# import pydantic as pydantic
# from typing import Optional
# import datetime as dt


# class _BaseTheaterHall(pydantic.BaseModel):
#     model_config = pydantic.ConfigDict(from_attributes=True)

#     name: str
#     capacity: int


# # Properties to receive on account creation
# class TheaterCreate(_BaseTheaterHall):
#     pass


# # Properties to receive on update
# class TheaterUpdate(_BaseTheaterHall):
#     pass


# # Properties shared by models stored in DB
# class _TheaterInDBBase(_BaseTheaterHall):
#     hallId: int


# # Properties to return to client
# class Theater(_TheaterInDBBase):
#     pass


# # Properties stored in DB
# class TheaterInDb(_TheaterInDBBase):
#     pass


# class _Base