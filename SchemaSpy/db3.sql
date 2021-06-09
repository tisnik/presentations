CREATE TABLE department (
   ID       integer NOT NULL,
   name     varchar(20) NOT NULL,
   location varchar(20) NOT NULL,
   
   PRIMARY KEY (ID)
);

CREATE TABLE employee (
   ID         integer NOT NULL,
   name       varchar(20) NOT NULL,
   job        varchar(20) NOT NULL,
   manager    integer,
   hiredate   date NOT NULL,
   salary     integer NOT NULL,
   comment    integer,
   department integer NOT NULL,
   
   PRIMARY KEY (ID),
   CONSTRAINT fk_manager FOREIGN KEY (manager) REFERENCES employee (ID)
      ON DELETE SET NULL
      ON UPDATE CASCADE,
   CONSTRAINT fk_department FOREIGN KEY (department) REFERENCES department (ID)
      ON DELETE RESTRICT
      ON UPDATE NO ACTION
);

CREATE TABLE project (
   ID        integer NOT NULL,
   employee  integer NOT NULL,
   startdate date NOT NULL,
   enddate   date NOT NULL,
   
   PRIMARY KEY (ID),
   CONSTRAINT fk_project FOREIGN KEY (employee) REFERENCES employee (ID)
      ON DELETE NO ACTION
      ON UPDATE CASCADE
);
