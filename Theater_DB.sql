CREATE TABLE "TheaterHall" (
    hallId INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    capacity INTEGER NOT NULL
);

CREATE TABLE "Season" (
    seasonId INTEGER PRIMARY KEY,
    season TEXT NOT NULL,
    year INTEGER NOT NULL
);

CREATE TABLE "Play" (
    playId INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    duration INTEGER NOT NULL,
    seasonId INTEGER NOT NULL,
    hallId INTEGER NOT NULL,
    FOREIGN KEY (seasonId) REFERENCES Season(seasonId) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (hallId) REFERENCES TheaterHall(hallId) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE "Performance" (
    performanceId INTEGER PRIMARY KEY,
    duration INTEGER NOT NULL,
    datetime DATETIME NOT NULL,
);

CREATE TABLE "Area" (
    areaId INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    hallId INTEGER NOT NULL,
    FOREIGN KEY (hallId) REFERENCES TheaterHall(hallId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Chair" (
    number INTEGER NOT NULL,
    row INTEGER NOT NULL,
    areaId INTEGER NOT NULL,
    PRIMARY KEY (number, row, areaId),
    FOREIGN KEY (areaId) REFERENCES Area(areaId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "CustomerProfile" (
    customerId INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    phone TEXT NOT NULL
);

CREATE TABLE "CustomerGroup" (
    groupId INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE "TicketPurchase" (
    purchaseId INTEGER PRIMARY KEY,
    datetime DATETIME NOT NULL,
    customerId INTEGER NOT NULL,
    FOREIGN KEY (customerId) REFERENCES CustomerProfile(customerId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Ticket" (
    ticketId INTEGER PRIMARY KEY,
    purchaseId INTEGER,
    performanceId INTEGER NOT NULL,
    number INTEGER NOT NULL,
    row INTEGER NOT NULL,
    areaId INTEGER NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (purchaseId) REFERENCES TicketPurchase(purchaseId) ON DELETE
    SET
        NULL ON UPDATE CASCADE,
        FOREIGN KEY (performanceId) REFERENCES Performance(performanceId) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (number, row, areaId) REFERENCES Chair(number, row, areaId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Act" (
    number INTEGER NOT NULL,
    playId INTEGER NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (number, playId),
    FOREIGN KEY (playId) REFERENCES Play(playId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Role" (
    roleId INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE "Actor" (
    actorId INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    status TEXT NOT NULL
);

CREATE TABLE "Employee" (
    employeeId INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    status TEXT NOT NULL,
    position TEXT NOT NULL
);

CREATE TABLE "ActorRole" (
    actorId INTEGER NOT NULL,
    roleId INTEGER NOT NULL,
    PRIMARY KEY (actorId, roleId),
    FOREIGN KEY (actorId) REFERENCES Actor(actorId) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (roleId) REFERENCES Role(roleId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "ActorPlay" (
    actorId INTEGER NOT NULL,
    playId INTEGER NOT NULL,
    PRIMARY KEY (actorId, playId),
    FOREIGN KEY (actorId) REFERENCES Actor(actorId) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (playId) REFERENCES Play(playId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "EmployeePlay" (
    employeeId INTEGER NOT NULL,
    playId INTEGER NOT NULL,
    PRIMARY KEY (employeeId, playId),
    FOREIGN KEY (employeeId) REFERENCES Employee(employeeId) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (playId) REFERENCES Play(playId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "ActRole" (
    actNumber INTEGER NOT NULL,
    playId INTEGER NOT NULL,
    roleId INTEGER NOT NULL,
    PRIMARY KEY (actNumber, playId, roleId),
    FOREIGN KEY (actNumber, playId) REFERENCES Act(number, playId) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (roleId) REFERENCES Role(roleId) ON DELETE CASCADE ON UPDATE CASCADE
);