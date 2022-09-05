CREATE TABLE students
(
    id          BIGINT          PRIMARY KEY,
    name        VARCHAR(255)    NOT NULL,
    room        BIGINT          NOT NULL,
    sex         VARCHAR(1)      NOT NULL,
    birthday    DATE            NOT NULL,

    FOREIGN KEY (room) REFERENCES rooms (id)
);