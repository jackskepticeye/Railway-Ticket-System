create database Train;

use Train;

create table Ticket ( CLASS varchar(10), 
                      GROSS_PRICE varchar (30), 
					  ADULT varchar (100), 
                      CHILD varchar (100), 
                      ORIGIN varchar(50), 
                      DESTINATION varchar(50),
                      NET_PRICE varchar(30),
                      REF_NO varchar(50),
                      TIME_1 varchar(200),
                      DATE_1 varchar(200),
                      ROUTE varchar(30), 
                      primary key(TIME_1) );
                      
select * from Ticket;


                      



