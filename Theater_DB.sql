CREATE TABLE "TheaterHall" (
    hall_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    capacity INTEGER NOT NULL
);

CREATE TABLE "Season" (
    season_id INTEGER PRIMARY KEY,
    season TEXT NOT NULL,
    year INTEGER NOT NULL
);

CREATE TABLE "Play" (
    play_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    description TEXT,
    season_id INTEGER NOT NULL,
    hall_id INTEGER NOT NULL,
    FOREIGN KEY (season_id) REFERENCES Season(season_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (hall_id) REFERENCES TheaterHall(hall_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE "Performance" (
    performance_id INTEGER PRIMARY KEY,
    datetime DATETIME NOT NULL,
    play_id INTEGER NOT NULL,
    hall_id INTEGER NOT NULL,
    FOREIGN KEY (play_id) REFERENCES Play(play_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (hall_id) REFERENCES TheaterHall(hall_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE "Area" (
    area_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    hall_id INTEGER NOT NULL,
    FOREIGN KEY (hall_id) REFERENCES TheaterHall(hall_id) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (name, hall_id)
);

CREATE TABLE "Chair" (
    chair_id INTEGER PRIMARY KEY,
    number INTEGER NOT NULL,
    row INTEGER NOT NULL,
    area_id INTEGER NOT NULL,
    hall_id INTEGER NOT NULL,
    FOREIGN KEY (area_id) REFERENCES Area(area_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (hall_id) REFERENCES TheaterHall(hall_id) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (number, row, area_id, hall_id)
);

CREATE TABLE "CustomerProfile" (
    customer_id INTEGER PRIMARY KEY,
    userName TEXT NOT NULL,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    phone TEXT NOT NULL,
    UNIQUE (userName)
);

CREATE TABLE "CustomerGroup" (
    group_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE "TicketPurchase" (
    purchase_id INTEGER PRIMARY KEY,
    datetime DATETIME NOT NULL,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES CustomerProfile(customer_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "TicketPrice" (
    ticketPrice_id INTEGER PRIMARY KEY,
    price REAL NOT NULL,
    group_id INTEGER NOT NULL,
    play_id INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES CustomerGroup(group_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (play_id) REFERENCES Play(play_id) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (group_id, play_id)
);

CREATE TABLE "Ticket" (
    ticket_id INTEGER PRIMARY KEY,
    purchase_id INTEGER,
    performance_id INTEGER NOT NULL,
    chair_id INTEGER NOT NULL,
    area_id INTEGER NOT NULL,
    ticketPrice_id INTEGER NOT NULL,
    FOREIGN KEY (purchase_id) REFERENCES TicketPurchase(purchase_id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (performance_id) REFERENCES Performance(performance_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (chair_id) REFERENCES Chair(chair_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (area_id) REFERENCES Area(area_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ticketPrice_id) REFERENCES TicketPrice(ticketPrice_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Act" (
    act_id INTEGER PRIMARY KEY,
    number INTEGER NOT NULL,
    name TEXT,
    play_id INTEGER NOT NULL,
    FOREIGN KEY (play_id) REFERENCES Play(play_id) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (number, play_id)
);

CREATE TABLE "Role" (
    role_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    play_id INTEGER NOT NULL,
    FOREIGN KEY (play_id) REFERENCES Play(play_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Actor" (
    actor_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    status TEXT NOT NULL,
    description TEXT
);

CREATE TABLE "Employee" (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    status TEXT NOT NULL,
    description TEXT,
    task TEXT NOT NULL
);

CREATE TABLE "ActorRole" (
    actorRole_id INTEGER PRIMARY KEY,
    actor_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (actor_id) REFERENCES Actor(actor_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (role_id) REFERENCES Role(role_id) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (actor_id, role_id)
);

CREATE TABLE "ActorPlay" (
    actorPlay_id INTEGER PRIMARY KEY,
    actor_id INTEGER NOT NULL,
    play_id INTEGER NOT NULL,
    FOREIGN KEY (actor_id) REFERENCES Actor(actor_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (play_id) REFERENCES Play(play_id) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (actor_id, play_id)
);

CREATE TABLE "EmployeePlay" (
    employeePlay_id INTEGER PRIMARY KEY,
    employee_id INTEGER NOT NULL,
    play_id INTEGER NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (play_id) REFERENCES Play(play_id) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (employee_id, play_id)
);

CREATE TABLE "ActRole" (
    actRole_id INTEGER PRIMARY KEY,
    act_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (act_id) REFERENCES Act(act_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (role_id) REFERENCES Role(role_id) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (act_id, role_id)
);