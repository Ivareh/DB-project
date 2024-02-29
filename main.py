from fastapi import FastAPI
import uvicorn
import schemas
import models
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)


@app.get("/")
async def root():
    return {"message": "Welcome to TDT4145 Project! Created by Ivar Haugland"}


@app.post("/theaterhalls")
async def create_theaterhall(theaterhall: schemas.TheaterHallIn_Pydantic):
    theaterhall_obj = await models.TheaterHall.create(
        **theaterhall.model_dump(exclude_unset=True)
    )
    return await schemas.TheaterHall_Pydantic.from_tortoise_orm(theaterhall_obj)


@app.get("/theaterhalls/{theaterhall_id}")
async def get_theaterhall(hall_id: int):
    return await schemas.TheaterHall_Pydantic.from_queryset_single(
        models.TheaterHall.get(hallId=hall_id)
    )


@app.get("/theaterhalls")
async def get_all_theaterhalls():
    return await schemas.TheaterHall_Pydantic.from_queryset(models.TheaterHall.all())


@app.delete("/theaterhalls/{theaterhall_id}")
async def delete_theaterhall(hall_id: int):
    theaterhall = await models.TheaterHall.get(hallId=hall_id)
    await theaterhall.delete()
    return {"message": f"TheaterHall with id {hall_id} deleted successfully!"}


@app.put("/theaterhalls/{theaterhall_id}")
async def update_theaterhall(hall_id: int, theaterhall: schemas.TheaterHallIn_Pydantic):
    await models.TheaterHall.filter(hallId=hall_id).update(
        **theaterhall.model_dump(exclude_unset=True)
    )
    return await schemas.TheaterHall_Pydantic.from_queryset_single(
        models.TheaterHall.get(hallId=hall_id)
    )


@app.post("/seasons")
async def create_season(season: schemas.SeasonIn_Pydantic):
    season_obj = await models.Season.create(**season.model_dump(exclude_unset=True))
    return await schemas.Season_Pydantic.from_tortoise_orm(season_obj)


@app.get("/seasons/{season_id}")
async def get_season(season_id: int):
    return await schemas.Season_Pydantic.from_queryset_single(
        models.Season.get(seasonId=season_id)
    )


@app.get("/seasons")
async def get_all_seasons():
    return await schemas.Season_Pydantic.from_queryset(models.Season.all())


@app.delete("/seasons/{season_id}")
async def delete_season(season_id: int):
    season = await models.Season.get(seasonId=season_id)
    await season.delete()
    return {"message": f"Season with id {season_id} deleted successfully!"}


@app.put("/seasons/{season_id}")
async def update_season(season_id: int, season: schemas.SeasonIn_Pydantic):
    await models.Season.filter(seasonId=season_id).update(
        **season.model_dump(exclude_unset=True)
    )
    return await schemas.Season_Pydantic.from_queryset_single(
        models.Season.get(seasonId=season_id)
    )


@app.post("/plays")
async def create_play(play: schemas.PlayIn_Pydantic):
    play_obj = await models.Play.create(**play.model_dump(exclude_unset=True))
    return await schemas.Play_Pydantic.from_tortoise_orm(play_obj)


@app.get("/plays/{play_id}")
async def get_play(play_id: int):
    return await schemas.Play_Pydantic.from_queryset_single(
        models.Play.get(playId=play_id)
    )


@app.get("/plays")
async def get_all_plays():
    return await schemas.Play_Pydantic.from_queryset(models.Play.all())


@app.delete("/plays/{play_id}")
async def delete_play(play_id: int):
    play = await models.Play.get(playId=play_id)
    await play.delete()
    return {"message": f"Play with id {play_id} deleted successfully!"}


@app.put("/plays/{play_id}")
async def update_play(play_id: int, play: schemas.PlayIn_Pydantic):
    await models.Play.filter(playId=play_id).update(
        **play.model_dump(exclude_unset=True)
    )
    return await schemas.Play_Pydantic.from_queryset_single(
        models.Play.get(playId=play_id)
    )


@app.post("/performances")
async def create_performance(performance: schemas.PerformanceIn_Pydantic):
    performance_obj = await models.Performance.create(
        **performance.model_dump(exclude_unset=True)
    )
    return await schemas.Performance_Pydantic.from_tortoise_orm(performance_obj)


@app.get("/performances/{performance_id}")
async def get_performance(performance_id: int):
    return await schemas.Performance_Pydantic.from_queryset_single(
        models.Performance.get(performanceId=performance_id)
    )


@app.get("/performances")
async def get_all_performances():
    return await schemas.Performance_Pydantic.from_queryset(models.Performance.all())


@app.delete("/performances/{performance_id}")
async def delete_performance(performance_id: int):
    performance = await models.Performance.get(performanceId=performance_id)
    await performance.delete()
    return {"message": f"Performance with id {performance_id} deleted successfully!"}


@app.put("/performances/{performance_id}")
async def update_performance(
    performance_id: int, performance: schemas.PerformanceIn_Pydantic
):
    await models.Performance.filter(performanceId=performance_id).update(
        **performance.model_dump(exclude_unset=True)
    )
    return await schemas.Performance_Pydantic.from_queryset_single(
        models.Performance.get(performanceId=performance_id)
    )


@app.post("/areas")
async def create_area(area: schemas.AreaIn_Pydantic):
    area_obj = await models.Area.create(**area.model_dump(exclude_unset=True))
    return await schemas.Area_Pydantic.from_tortoise_orm(area_obj)


@app.get("/areas/{area_id}")
async def get_area(area_id: int):
    return await schemas.Area_Pydantic.from_queryset_single(
        models.Area.get(areaId=area_id)
    )


@app.get("/areas")
async def get_all_areas():
    return await schemas.Area_Pydantic.from_queryset(models.Area.all())


@app.delete("/areas/{area_id}")
async def delete_area(area_id: int):
    area = await models.Area.get(areaId=area_id)
    await area.delete()
    return {"message": f"Area with id {area_id} deleted successfully!"}


@app.put("/areas/{area_id}")
async def update_area(area_id: int, area: schemas.AreaIn_Pydantic):
    await models.Area.filter(areaId=area_id).update(
        **area.model_dump(exclude_unset=True)
    )
    return await schemas.Area_Pydantic.from_queryset_single(
        models.Area.get(areaId=area_id)
    )


@app.post("/chairs")
async def create_chair(chair: schemas.ChairIn_Pydantic):
    chair_obj = await models.Chair.create(**chair.model_dump(exclude_unset=True))
    return await schemas.Chair_Pydantic.from_tortoise_orm(chair_obj)


@app.get("/chairs/{chair_id}")
async def get_chair(chair_id: int):
    return await schemas.Chair_Pydantic.from_queryset_single(
        models.Chair.get(chairId=chair_id)
    )


@app.get("/chairs")
async def get_all_chairs():
    return await schemas.Chair_Pydantic.from_queryset(models.Chair.all())


@app.delete("/chairs/{chair_id}")
async def delete_chair(chair_id: int):
    chair = await models.Chair.get(chairId=chair_id)
    await chair.delete()
    return {"message": f"Chair with id {chair_id} deleted successfully!"}


@app.put("/chairs/{chair_id}")
async def update_chair(chair_id: int, chair: schemas.ChairIn_Pydantic):
    await models.Chair.filter(chairId=chair_id).update(
        **chair.model_dump(exclude_unset=True)
    )
    return await schemas.Chair_Pydantic.from_queryset_single(
        models.Chair.get(chairId=chair_id)
    )


@app.post("/customerprofiles")
async def create_customerprofile(customerprofile: schemas.CustomerProfileIn_Pydantic):
    customerprofile_obj = await models.CustomerProfile.create(
        **customerprofile.model_dump(exclude_unset=True)
    )
    return await schemas.CustomerProfile_Pydantic.from_tortoise_orm(customerprofile_obj)


@app.get("/customerprofiles/{customerprofile_id}")
async def get_customerprofile(customerprofile_id: int):
    return await schemas.CustomerProfile_Pydantic.from_queryset_single(
        models.CustomerProfile.get(customerId=customerprofile_id)
    )


@app.get("/customerprofiles")
async def get_all_customerprofiles():
    return await schemas.CustomerProfile_Pydantic.from_queryset(
        models.CustomerProfile.all()
    )


@app.delete("/customerprofiles/{customerprofile_id}")
async def delete_customerprofile(customerprofile_id: int):
    customerprofile = await models.CustomerProfile.get(customerId=customerprofile_id)
    await customerprofile.delete()
    return {
        "message": f"CustomerProfile with id {customerprofile_id} deleted successfully!"
    }


@app.put("/customerprofiles/{customerprofile_id}")
async def update_customerprofile(
    customerprofile_id: int, customerprofile: schemas.CustomerProfileIn_Pydantic
):
    await models.CustomerProfile.filter(customerId=customerprofile_id).update(
        **customerprofile.model_dump(exclude_unset=True)
    )
    return await schemas.CustomerProfile_Pydantic.from_queryset_single(
        models.CustomerProfile.get(customerId=customerprofile_id)
    )


@app.post("/customergroups")
async def create_customergroup(customergroup: schemas.CustomerGroupIn_Pydantic):
    customergroup_obj = await models.CustomerGroup.create(
        **customergroup.model_dump(exclude_unset=True)
    )
    return await schemas.CustomerGroup_Pydantic.from_tortoise_orm(customergroup_obj)


@app.get("/customergroups/{customergroup_id}")
async def get_customergroup(customergroup_id: int):
    return await schemas.CustomerGroup_Pydantic.from_queryset_single(
        models.CustomerGroup.get(groupId=customergroup_id)
    )


@app.get("/customergroups")
async def get_all_customergroups():
    return await schemas.CustomerGroup_Pydantic.from_queryset(
        models.CustomerGroup.all()
    )


@app.delete("/customergroups/{customergroup_id}")
async def delete_customergroup(customergroup_id: int):
    customergroup = await models.CustomerGroup.get(groupId=customergroup_id)
    await customergroup.delete()
    return {
        "message": f"CustomerGroup with id {customergroup_id} deleted successfully!"
    }


@app.put("/customergroups/{customergroup_id}")
async def update_customergroup(
    customergroup_id: int, customergroup: schemas.CustomerGroupIn_Pydantic
):
    await models.CustomerGroup.filter(groupId=customergroup_id).update(
        **customergroup.model_dump(exclude_unset=True)
    )
    return await schemas.CustomerGroup_Pydantic.from_queryset_single(
        models.CustomerGroup.get(groupId=customergroup_id)
    )


@app.post("/ticketpurchases")
async def create_ticketpurchase(ticketpurchase: schemas.TicketPurchaseIn_Pydantic):
    ticketpurchase_obj = await models.TicketPurchase.create(
        **ticketpurchase.model_dump(exclude_unset=True)
    )
    return await schemas.TicketPurchase_Pydantic.from_tortoise_orm(ticketpurchase_obj)


@app.get("/ticketpurchases/{ticketpurchase_id}")
async def get_ticketpurchase(ticketpurchase_id: int):
    return await schemas.TicketPurchase_Pydantic.from_queryset_single(
        models.TicketPurchase.get(purchaseId=ticketpurchase_id)
    )


@app.get("/ticketpurchases")
async def get_all_ticketpurchases():
    return await schemas.TicketPurchase_Pydantic.from_queryset(
        models.TicketPurchase.all()
    )


@app.delete("/ticketpurchases/{ticketpurchase_id}")
async def delete_ticketpurchase(ticketpurchase_id: int):
    ticketpurchase = await models.TicketPurchase.get(purchaseId=ticketpurchase_id)
    await ticketpurchase.delete()
    return {
        "message": f"TicketPurchase with id {ticketpurchase_id} deleted successfully!"
    }


@app.put("/ticketpurchases/{ticketpurchase_id}")
async def update_ticketpurchase(
    ticketpurchase_id: int, ticketpurchase: schemas.TicketPurchaseIn_Pydantic
):
    await models.TicketPurchase.filter(purchaseId=ticketpurchase_id).update(
        **ticketpurchase.model_dump(exclude_unset=True)
    )
    return await schemas.TicketPurchase_Pydantic.from_queryset_single(
        models.TicketPurchase.get(purchaseId=ticketpurchase_id)
    )


@app.post("/tickets")
async def create_ticket(ticket: schemas.TicketIn_Pydantic):
    ticket_obj = await models.Ticket.create(**ticket.model_dump(exclude_unset=True))
    return await schemas.Ticket_Pydantic.from_tortoise_orm(ticket_obj)


@app.get("/tickets/{ticket_id}")
async def get_ticket(ticket_id: int):
    return await schemas.Ticket_Pydantic.from_queryset_single(
        models.Ticket.get(ticketId=ticket_id)
    )


@app.get("/tickets")
async def get_all_tickets():
    return await schemas.Ticket_Pydantic.from_queryset(models.Ticket.all())


@app.delete("/tickets/{ticket_id}")
async def delete_ticket(ticket_id: int):
    ticket = await models.Ticket.get(ticketId=ticket_id)
    await ticket.delete()
    return {"message": f"Ticket with id {ticket_id} deleted successfully!"}


@app.put("/tickets/{ticket_id}")
async def update_ticket(ticket_id: int, ticket: schemas.TicketIn_Pydantic):
    await models.Ticket.filter(ticketId=ticket_id).update(
        **ticket.model_dump(exclude_unset=True)
    )
    return await schemas.Ticket_Pydantic.from_queryset_single(
        models.Ticket.get(ticketId=ticket_id)
    )


@app.post("/ticketprices")
async def create_ticketprice(ticketprice: schemas.TicketPriceIn_Pydantic):
    ticketprice_obj = await models.TicketPrice.create(
        **ticketprice.model_dump(exclude_unset=True)
    )
    return await schemas.TicketPrice_Pydantic.from_tortoise_orm(ticketprice_obj)


@app.get("/ticketprices/{ticketprice_id}")
async def get_ticketprice(ticketprice_id: int):
    return await schemas.TicketPrice_Pydantic.from_queryset_single(
        models.TicketPrice.get(ticketPriceId=ticketprice_id)
    )


@app.get("/ticketprices")
async def get_all_ticketprices():
    return await schemas.TicketPrice_Pydantic.from_queryset(models.TicketPrice.all())


@app.delete("/ticketprices/{ticketprice_id}")
async def delete_ticketprice(ticketprice_id: int):
    ticketprice = await models.TicketPrice.get(ticketPriceId=ticketprice_id)
    await ticketprice.delete()
    return {"message": f"TicketPrice with id {ticketprice_id} deleted successfully!"}


@app.put("/ticketprices/{ticketprice_id}")
async def update_ticketprice(
    ticketprice_id: int, ticketprice: schemas.TicketPriceIn_Pydantic
):
    await models.TicketPrice.filter(ticketPriceId=ticketprice_id).update(
        **ticketprice.model_dump(exclude_unset=True)
    )
    return await schemas.TicketPrice_Pydantic.from_queryset_single(
        models.TicketPrice.get(ticketPriceId=ticketprice_id)
    )


@app.post("/acts")
async def create_act(act: schemas.ActIn_Pydantic):
    act_obj = await models.Act.create(**act.model_dump(exclude_unset=True))
    return await schemas.Act_Pydantic.from_tortoise_orm(act_obj)


@app.get("/acts/{act_id}")
async def get_act(act_id: int):
    return await schemas.Act_Pydantic.from_queryset_single(models.Act.get(actId=act_id))


@app.get("/acts")
async def get_all_acts():
    return await schemas.Act_Pydantic.from_queryset(models.Act.all())


@app.delete("/acts/{act_id}")
async def delete_act(act_id: int):
    act = await models.Act.get(actId=act_id)
    await act.delete()
    return {"message": f"Act with id {act_id} deleted successfully!"}


@app.put("/acts/{act_id}")
async def update_act(act_id: int, act: schemas.ActIn_Pydantic):
    await models.Act.filter(actId=act_id).update(**act.model_dump(exclude_unset=True))
    return await schemas.Act_Pydantic.from_queryset_single(models.Act.get(actId=act_id))


@app.post("/roles")
async def create_role(role: schemas.RoleIn_Pydantic):
    role_obj = await models.Role.create(**role.model_dump(exclude_unset=True))
    return await schemas.Role_Pydantic.from_tortoise_orm(role_obj)


@app.get("/roles/{role_id}")
async def get_role(role_id: int):
    return await schemas.Role_Pydantic.from_queryset_single(
        models.Role.get(roleId=role_id)
    )


@app.get("/roles")
async def get_all_roles():
    return await schemas.Role_Pydantic.from_queryset(models.Role.all())


@app.delete("/roles/{role_id}")
async def delete_role(role_id: int):
    role = await models.Role.get(roleId=role_id)
    await role.delete()
    return {"message": f"Role with id {role_id} deleted successfully!"}


@app.put("/roles/{role_id}")
async def update_role(role_id: int, role: schemas.RoleIn_Pydantic):
    await models.Role.filter(roleId=role_id).update(
        **role.model_dump(exclude_unset=True)
    )
    return await schemas.Role_Pydantic.from_queryset_single(
        models.Role.get(roleId=role_id)
    )


@app.post("/actors")
async def create_actor(actor: schemas.ActorIn_Pydantic):
    actor_obj = await models.Actor.create(**actor.model_dump(exclude_unset=True))
    return await schemas.Actor_Pydantic.from_tortoise_orm(actor_obj)


@app.get("/actors/{actor_id}")
async def get_actor(actor_id: int):
    return await schemas.Actor_Pydantic.from_queryset_single(
        models.Actor.get(actorId=actor_id)
    )


@app.get("/actors")
async def get_all_actors():
    return await schemas.Actor_Pydantic.from_queryset(models.Actor.all())


@app.delete("/actors/{actor_id}")
async def delete_actor(actor_id: int):
    actor = await models.Actor.get(actorId=actor_id)
    await actor.delete()
    return {"message": f"Actor with id {actor_id} deleted successfully!"}


@app.put("/actors/{actor_id}")
async def update_actor(actor_id: int, actor: schemas.ActorIn_Pydantic):
    await models.Actor.filter(actorId=actor_id).update(
        **actor.model_dump(exclude_unset=True)
    )
    return await schemas.Actor_Pydantic.from_queryset_single(
        models.Actor.get(actorId=actor_id)
    )


@app.post("/employees")
async def create_employee(employee: schemas.EmployeeIn_Pydantic):
    employee_obj = await models.Employee.create(
        **employee.model_dump(exclude_unset=True)
    )
    return await schemas.Employee_Pydantic.from_tortoise_orm(employee_obj)


@app.get("/employees/{employee_id}")
async def get_employee(employee_id: int):
    return await schemas.Employee_Pydantic.from_queryset_single(
        models.Employee.get(employeeId=employee_id)
    )


@app.get("/employees")
async def get_all_employees():
    return await schemas.Employee_Pydantic.from_queryset(models.Employee.all())


@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    employee = await models.Employee.get(employeeId=employee_id)
    await employee.delete()
    return {"message": f"Employee with id {employee_id} deleted successfully!"}


@app.put("/employees/{employee_id}")
async def update_employee(employee_id: int, employee: schemas.EmployeeIn_Pydantic):
    await models.Employee.filter(employeeId=employee_id).update(
        **employee.model_dump(exclude_unset=True)
    )
    return await schemas.Employee_Pydantic.from_queryset_single(
        models.Employee.get(employeeId=employee_id)
    )


@app.post("/actorroles")
async def create_actorrole(actorrole: schemas.ActorRoleIn_Pydantic):
    actorrole_obj = await models.ActorRole.create(
        **actorrole.model_dump(exclude_unset=True)
    )
    return await schemas.ActorRole_Pydantic.from_tortoise_orm(actorrole_obj)


@app.get("/actorroles/{actorrole_id}")
async def get_actorrole(actorrole_id: int):
    return await schemas.ActorRole_Pydantic.from_queryset_single(
        models.ActorRole.get(actorRoleId=actorrole_id)
    )


@app.get("/actorroles")
async def get_all_actorroles():
    return await schemas.ActorRole_Pydantic.from_queryset(models.ActorRole.all())


@app.delete("/actorroles/{actorrole_id}")
async def delete_actorrole(actorrole_id: int):
    actorrole = await models.ActorRole.get(actorRoleId=actorrole_id)
    await actorrole.delete()
    return {"message": f"ActorRole with id {actorrole_id} deleted successfully!"}


@app.put("/actorroles/{actorrole_id}")
async def update_actorrole(actorrole_id: int, actorrole: schemas.ActorRoleIn_Pydantic):
    await models.ActorRole.filter(actorRoleId=actorrole_id).update(
        **actorrole.model_dump(exclude_unset=True)
    )
    return await schemas.ActorRole_Pydantic.from_queryset_single(
        models.ActorRole.get(actorRoleId=actorrole_id)
    )


@app.post("/actorplays")
async def create_actorplay(actorplay: schemas.ActorPlayIn_Pydantic):
    actorplay_obj = await models.ActorPlay.create(
        **actorplay.model_dump(exclude_unset=True)
    )
    return await schemas.ActorPlay_Pydantic.from_tortoise_orm(actorplay_obj)


@app.get("/actorplays/{actorplay_id}")
async def get_actorplay(actorplay_id: int):
    return await schemas.ActorPlay_Pydantic.from_queryset_single(
        models.ActorPlay.get(actorPlayId=actorplay_id)
    )


@app.get("/actorplays")
async def get_all_actorplays():
    return await schemas.ActorPlay_Pydantic.from_queryset(models.ActorPlay.all())


@app.delete("/actorplays/{actorplay_id}")
async def delete_actorplay(actorplay_id: int):
    actorplay = await models.ActorPlay.get(actorPlayId=actorplay_id)
    await actorplay.delete()


@app.put("/actorplays/{actorplay_id}")
async def update_actorplay(actorplay_id: int, actorplay: schemas.ActorPlayIn_Pydantic):
    await models.ActorPlay.filter(actorPlayId=actorplay_id).update(
        **actorplay.model_dump(exclude_unset=True)
    )
    return await schemas.ActorPlay_Pydantic.from_queryset_single(
        models.ActorPlay.get(actorPlayId=actorplay_id)
    )


@app.post("/employeeplays")
async def create_employeeplay(employeeplay: schemas.EmployeePlayIn_Pydantic):
    employeeplay_obj = await models.EmployeePlay.create(
        **employeeplay.model_dump(exclude_unset=True)
    )
    return await schemas.EmployeePlay_Pydantic.from_tortoise_orm(employeeplay_obj)


@app.get("/employeeplays/{employeeplay_id}")
async def get_employeeplay(employeeplay_id: int):
    return await schemas.EmployeePlay_Pydantic.from_queryset_single(
        models.EmployeePlay.get(employeePlayId=employeeplay_id)
    )


@app.get("/employeeplays")
async def get_all_employeeplays():
    return await schemas.EmployeePlay_Pydantic.from_queryset(models.EmployeePlay.all())


@app.delete("/employeeplays/{employeeplay_id}")
async def delete_employeeplay(employeeplay_id: int):
    employeeplay = await models.EmployeePlay.get(employeePlayId=employeeplay_id)
    await employeeplay.delete()
    return {"message": f"EmployeePlay with id {employeeplay_id} deleted successfully!"}


@app.put("/employeeplays/{employeeplay_id}")
async def update_employeeplay(
    employeeplay_id: int, employeeplay: schemas.EmployeePlayIn_Pydantic
):
    await models.EmployeePlay.filter(employeePlayId=employeeplay_id).update(
        **employeeplay.model_dump(exclude_unset=True)
    )
    return await schemas.EmployeePlay_Pydantic.from_queryset_single(
        models.EmployeePlay.get(employeePlayId=employeeplay_id)
    )


@app.post("/actroles")
async def create_actrole(actrole: schemas.ActRoleIn_Pydantic):
    actrole_obj = await models.ActRole.create(**actrole.model_dump(exclude_unset=True))
    return await schemas.ActRole_Pydantic.from_tortoise_orm(actrole_obj)


@app.get("/actroles/{actrole_id}")
async def get_actrole(actrole_id: int):
    return await schemas.ActRole_Pydantic.from_queryset_single(
        models.ActRole.get(actRoleId=actrole_id)
    )


@app.get("/actroles")
async def get_all_actroles():
    return await schemas.ActRole_Pydantic.from_queryset(models.ActRole.all())


@app.delete("/actroles/{actrole_id}")
async def delete_actrole(actrole_id: int):
    actrole = await models.ActRole.get(actRoleId=actrole_id)
    await actrole.delete()
    return {"message": f"ActRole with id {actrole_id} deleted successfully!"}


@app.put("/actroles/{actrole_id}")
async def update_actrole(actrole_id: int, actrole: schemas.ActRoleIn_Pydantic):
    await models.ActRole.filter(actRoleId=actrole_id).update(
        **actrole.model_dump(exclude_unset=True)
    )
    return await schemas.ActRole_Pydantic.from_queryset_single(
        models.ActRole.get(actRoleId=actrole_id)
    )
