create table hola(
    id_user int primary key,
    username varchar(30)
)

create table hola2(
    id_gen int primary key,
    username2 varchar(40)
)

create table related(
    id_Reg int primary key,
    username4 varchar(40),
    id_user int
)