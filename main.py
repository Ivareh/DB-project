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


@app.post("/customer_profiles")
async def create_customer_profile(customer_profile: schemas.CustomerProfileIn_Pydantic):
    customer_profile_obj = await models.CustomerProfile.create(
        **customer_profile.model_dump(exclude_unset=True)
    )
    return await schemas.CustomerProfile_Pydantic.from_tortoise_orm(
        customer_profile_obj
    )


@app.get("/customer_profiles/{customer_id}")
async def get_customer_profile(customer_id: int):
    return await schemas.CustomerProfile_Pydantic.from_queryset_single(
        models.CustomerProfile.get(customerId=customer_id)
    )


@app.get("/customer_profiles")
async def get_all_customer_profiles():
    return await schemas.CustomerProfile_Pydantic.from_queryset(
        models.CustomerProfile.all()
    )


@app.delete("/customer_profiles/{customer_id}")
async def delete_customer_profile(customer_id: int):
    customer_profile = await models.CustomerProfile.get(customerId=customer_id)
    await customer_profile.delete()
    return {"message": f"CustomerProfile with id {customer_id} deleted successfully!"}


@app.put("/customer_profiles/{customer_id}")
async def update_customer_profile(
    customer_id: int, customer_profile: schemas.CustomerProfileIn_Pydantic
):
    await models.CustomerProfile.filter(customerId=customer_id).update(
        **customer_profile.model_dump(exclude_unset=True)
    )
    return await schemas.CustomerProfile_Pydantic.from_queryset_single(
        models.CustomerProfile.get(customerId=customer_id)
    )


@app.post("/customer_groups")
async def create_customer_group(customer_group: schemas.CustomerGroupIn_Pydantic):
    customer_group_obj = await models.CustomerGroup.create(
        **customer_group.model_dump(exclude_unset=True)
    )
    return await schemas.CustomerGroup_Pydantic.from_tortoise_orm(customer_group_obj)


@app.get("/customer_groups/{group_id}")
async def get_customer_group(group_id: int):
    return await schemas.CustomerGroup_Pydantic.from_queryset_single(
        models.CustomerGroup.get(groupId=group_id)
    )


@app.get("/customer_groups")
async def get_all_customer_groups():
    return await schemas.CustomerGroup_Pydantic.from_queryset(
        models.CustomerGroup.all()
    )


@app.delete("/customer_groups/{group_id}")
async def delete_customer_group(group_id: int):
    customer_group = await models.CustomerGroup.get(groupId=group_id)
    await customer_group.delete()
    return {"message": f"CustomerGroup with id {group_id} deleted successfully!"}


@app.put("/customer_groups/{group_id}")
async def update_customer_group(
    group_id: int, customer_group: schemas.CustomerGroupIn_Pydantic
):
    await models.CustomerGroup.filter(groupId=group_id).update(
        **customer_group.model_dump(exclude_unset=True)
    )
    return await schemas.CustomerGroup_Pydantic.from_queryset_single(
        models.CustomerGroup.get(groupId=group_id)
    )


@app.post("/ticket_purchases")
async def create_ticket_purchase(ticket_purchase: schemas.TicketPurchaseIn_Pydantic):
    ticket_purchase_obj = await models.TicketPurchase.create(
        **ticket_purchase.model_dump(exclude_unset=True)
    )
    return await schemas.TicketPurchase_Pydantic.from_tortoise_orm(ticket_purchase_obj)


@app.get("/ticket_purchases/{purchase_id}")
async def get_ticket_purchase(purchase_id: int):
    return await schemas.TicketPurchase_Pydantic.from_queryset_single(
        models.TicketPurchase.get(purchaseId=purchase_id)
    )


@app.get("/ticket_purchases")
async def get_all_ticket_purchases():
    return await schemas.TicketPurchase_Pydantic.from_queryset(
        models.TicketPurchase.all()
    )


@app.delete("/ticket_purchases/{purchase_id}")
async def delete_ticket_purchase(purchase_id: int):
    ticket_purchase = await models.TicketPurchase.get(purchaseId=purchase_id)
    await ticket_purchase.delete()
    return {"message": f"TicketPurchase with id {purchase_id} deleted successfully!"}


@app.put("/ticket_purchases/{purchase_id}")
async def update_ticket_purchase(
    purchase_id: int, ticket_purchase: schemas.TicketPurchaseIn_Pydantic
):
    await models.TicketPurchase.filter(purchaseId=purchase_id).update(
        **ticket_purchase.model_dump(exclude_unset=True)
    )
    return await schemas.TicketPurchase_Pydantic.from_queryset_single(
        models.TicketPurchase.get(purchaseId=purchase_id)
    )


@app.post("/ticket_prices")
async def create_ticket_price(ticket_price: schemas.TicketPriceIn_Pydantic):
    ticket_price_obj = await models.TicketPrice.create(
        **ticket_price.model_dump(exclude_unset=True)
    )
    return await schemas.TicketPrice_Pydantic.from_tortoise_orm(ticket_price_obj)


@app.get("/ticket_prices/{price_id}")
async def get_ticket_price(price_id: int):
    return await schemas.TicketPrice_Pydantic.from_queryset_single(
        models.TicketPrice.get(priceId=price_id)
    )


@app.get("/ticket_prices")
async def get_all_ticket_prices():
    return await schemas.TicketPrice_Pydantic.from_queryset(models.TicketPrice.all())


@app.delete("/ticket_prices/{price_id}")
async def delete_ticket_price(price_id: int):
    ticket_price = await models.TicketPrice.get(priceId=price_id)
    await ticket_price.delete()
    return {"message": f"TicketPrice with id {price_id} deleted successfully!"}


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


@app.post("/actor_roles")
async def create_actor_role(actor_role: schemas.ActorRoleIn_Pydantic):
    actor_role_obj = await models.ActorRole.create(
        **actor_role.model_dump(exclude_unset=True)
    )
    return await schemas.ActorRole_Pydantic.from_tortoise_orm(actor_role_obj)


@app.get("/actor_roles/{actorRole_id}")
async def get_actor_role(actorRole_id: int):
    return await schemas.ActorRole_Pydantic.from_queryset_single(
        models.ActorRole.get(actorRoleId=actorRole_id)
    )


@app.get("/actor_roles")
async def get_all_actor_roles():
    return await schemas.ActorRole_Pydantic.from_queryset(models.ActorRole.all())


@app.delete("/actor_roles/{actorRole_id}")
async def delete_actor_role(actorRole_id: int):
    actor_role = await models.ActorRole.get(actorRoleId=actorRole_id)
    await actor_role.delete()
    return {"message": f"ActorRole with id {actorRole_id} deleted successfully!"}


@app.put("/actor_roles/{actorRole_id}")
async def update_actor_role(
    actorRole_id: int, actor_role: schemas.ActorRoleIn_Pydantic
):
    await models.ActorRole.filter(actorRoleId=actorRole_id).update(
        **actor_role.model_dump(exclude_unset=True)
    )
    return await schemas.ActorRole_Pydantic.from_queryset_single(
        models.ActorRole.get(actorRoleId=actorRole_id)
    )


@app.post("/actor_plays")
async def create_actor_play(actor_play: schemas.ActorPlayIn_Pydantic):
    actor_play_obj = await models.ActorPlay.create(
        **actor_play.model_dump(exclude_unset=True)
    )
    return await schemas.ActorPlay_Pydantic.from_tortoise_orm(actor_play_obj)


@app.get("/actor_plays/{actorPlay_id}")
async def get_actor_play(actorPlay_id: int):
    return await schemas.ActorPlay_Pydantic.from_queryset_single(
        models.ActorPlay.get(actorPlayId=actorPlay_id)
    )


@app.get("/actor_plays")
async def get_all_actor_plays():
    return await schemas.ActorPlay_Pydantic.from_queryset(models.ActorPlay.all())


@app.delete("/actor_plays/{actorPlay_id}")
async def delete_actor_play(actorPlay_id: int):
    actor_play = await models.ActorPlay.get(actorPlayId=actorPlay_id)
    await actor_play.delete()


@app.put("/actor_plays/{actorPlay_id}")
async def update_actor_play(
    actorPlay_id: int, actor_play: schemas.ActorPlayIn_Pydantic
):
    await models.ActorPlay.filter(actorPlayId=actorPlay_id).update(
        **actor_play.model_dump(exclude_unset=True)
    )
    return await schemas.ActorPlay_Pydantic.from_queryset_single(
        models.ActorPlay.get(actorPlayId=actorPlay_id)
    )


@app.post("/employee_plays")
async def create_employee_play(employee_play: schemas.EmployeePlayIn_Pydantic):
    employee_play_obj = await models.EmployeePlay.create(
        **employee_play.model_dump(exclude_unset=True)
    )
    return await schemas.EmployeePlay_Pydantic.from_tortoise_orm(employee_play_obj)


@app.get("/employee_plays/{employeePlay_id}")
async def get_employee_play(employeePlay_id: int):
    return await schemas.EmployeePlay_Pydantic.from_queryset_single(
        models.EmployeePlay.get(employeePlayId=employeePlay_id)
    )


@app.get("/employee_plays")
async def get_all_employee_plays():
    return await schemas.EmployeePlay_Pydantic.from_queryset(models.EmployeePlay.all())


@app.delete("/employee_plays/{employeePlay_id}")
async def delete_employee_play(employeePlay_id: int):
    employee_play = await models.EmployeePlay.get(employeePlayId=employeePlay_id)
    await employee_play.delete()
    return {"message": f"EmployeePlay with id {employeePlay_id} deleted successfully!"}


@app.put("/employee_plays/{employeePlay_id}")
async def update_employee_play(
    employeePlay_id: int, employee_play: schemas.EmployeePlayIn_Pydantic
):
    await models.EmployeePlay.filter(employeePlayId=employeePlay_id).update(
        **employee_play.model_dump(exclude_unset=True)
    )
    return await schemas.EmployeePlay_Pydantic.from_queryset_single(
        models.EmployeePlay.get(employeePlayId=employeePlay_id)
    )


@app.post("/act_roles")
async def create_act_role(act_role: schemas.ActRoleIn_Pydantic):
    act_role_obj = await models.ActRole.create(
        **act_role.model_dump(exclude_unset=True)
    )
    return await schemas.ActRole_Pydantic.from_tortoise_orm(act_role_obj)


@app.get("/act_roles/{actRole_id}")
async def get_act_role(actRole_id: int):
    return await schemas.ActRole_Pydantic.from_queryset_single(
        models.ActRole.get(actRoleId=actRole_id)
    )


@app.get("/act_roles")
async def get_all_act_roles():
    return await schemas.ActRole_Pydantic.from_queryset(models.ActRole.all())


@app.delete("/act_roles/{actRole_id}")
async def delete_act_role(actRole_id: int):
    act_role = await models.ActRole.get(actRoleId=actRole_id)
    await act_role.delete()
    return {"message": f"ActRole with id {actRole_id} deleted successfully!"}


@app.put("/act_roles/{actRole_id}")
async def update_act_role(actRole_id: int, act_role: schemas.ActRoleIn_Pydantic):
    await models.ActRole.filter(actRoleId=actRole_id).update(
        **act_role.model_dump(exclude_unset=True)
    )
    return await schemas.ActRole_Pydantic.from_queryset_single(
        models.ActRole.get(actRoleId=actRole_id)
    )
