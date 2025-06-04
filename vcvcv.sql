create database practice;
use practice;
create table studnet(
   roll_no int primary key,
   name varchar(150) not null,
   course_name varchar(100) not null
);
create table details(
   roll_no int,
   address text,
   phone_no varchar(100) not null,
   FOREIGN KEY (roll_no) REFERENCES studnet(roll_no)
);
insert into studnet(roll_no,name,course_name) values
(1,"a","AI"),
(2,"b","CSE"),
(3,"c","ECE"),
(4,"d","AI"),
(5,"e","EEE"); 
select * from studnet;
alter table studnet drop column phone_no;
insert into details(roll_no,address,phone_no) value(1,null,"12345678");
insert into details(roll_no,address,phone_no) value(5,"hyd","12376878");
insert into details(roll_no,address,phone_no) value(3,"delhi","13245678");
insert into details(roll_no,address,phone_no) value(4,"null","12976898");
insert into details(roll_no,address,phone_no) value(2,"chennai","13977898");
select * from details;


select *
from studnet
join details
on studnet.roll_no=details.roll_no;

select s.roll_no,s.name,s.course_name,d.phone_no
from studnet s
left join details d
on s.roll_no=d.roll_no

insert into studnet value(10,"HELLO","ECE");
select * from studnet;
select *
from studnet
left join details
on studnet.roll_no=details.roll_no;

select * from studnet;
select *
from details
left join studnet
on studnet.roll_no=details.roll_no;

select
 * from studnet
right join details
on studnet.roll_no=details.roll_no;

