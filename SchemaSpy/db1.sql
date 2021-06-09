CREATE TABLE department (
   ID       integer NOT NULL,
   name     varchar(20) NOT NULL,
   location varchar(20) NOT NULL
);

CREATE TABLE employee (
   ID         integer NOT NULL,
   name       varchar(20) NOT NULL,
   job        varchar(20) NOT NULL,
   manager    integer,
   hiredate   date NOT NULL,
   salary     integer NOT NULL,
   comment    integer,
   department integer NOT NULL
);

CREATE TABLE project (
   ID        integer NOT NULL,
   employee  integer NOT NULL,
   startdate date NOT NULL,
   enddate   date NOT NULL
);
