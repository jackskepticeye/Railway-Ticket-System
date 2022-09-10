create database Registration_Details;

use Registration_Details;

create table Reg_Details (F_Name varchar(20), 
                          L_Name  varchar(20), 
                          CONTACT varchar(20),
                          EMAIL varchar(50),
                          Security_Q varchar(100), 
                          Security_A varchar(100), 
                          PASSWORD_1 varchar(100), 
                          primary key (EMAIL));

select * from Reg_Details;