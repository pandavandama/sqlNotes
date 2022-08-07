# sqlNotes

### Create statement
CREATE TABLE Persons (
    PersonID int auto_increment primary key,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

### Number of rows
select count(*) from Persons

### Joins
