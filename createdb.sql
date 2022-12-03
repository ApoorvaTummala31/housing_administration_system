use housing_admin_system; 

create table community(com_id int primary key, name varchar(10) not null, contact varchar(10) not null, no_of_apartments int);
create table office(off_id int primary key,add_street varchar(10), add_door varchar(5), phone varchar(10));

create table employee(emp_id int primary key, name varchar(30) not null, DOB varchar(12) not null, dept varchar(20), works_in int,foreign key(works_in) references office(off_id) on delete cascade on update cascade);
create table apartment(apt_id int primary key, a_type varchar(10) not null, no_of_residents int, street_name varchar(10),com_id int not null, foreign key(com_id) references community(com_id) on delete cascade on update cascade);

create table resident(res_id int,name varchar(10) not null, DOB varchar(12) not null,apt_num int not null, gender varchar(10) not null, primary key(res_id), foreign key(apt_num) references apartment(apt_id) on delete cascade on update cascade);
create table payment_account(p_id int primary key, method varchar(10) not null, p_date varchar(12) not null,amount int not null, invoice varchar(100),res_id int,foreign key(res_id) references resident(res_id) on delete cascade);

create table activity(activity_id int primary key, type varchar(20) not null, maintained_by int not null, foreign key(maintained_by) references employee(emp_id) on delete cascade on update cascade);
create table complaints(res_id int, c_type varchar(20), c_desc varchar(40), c_date date, status varchar(10), resolved_by int,foreign key(resolved_by) references employee(emp_id) on delete cascade on update cascade  );

create table rents(apt_id int, lease_by int,lease_on varchar(10),primary key(apt_id,lease_on,lease_by),foreign key(apt_id) references apartment(apt_id) on delete cascade on update cascade,foreign key(lease_by) references resident(res_id) on delete cascade on update cascade);
create table opts_for(res_id int NOT NULL, activity_id int NOT NULL, Primary Key(res_id,activity_id),foreign key(activity_id) references activity(activity_id) on delete cascade on update cascade,foreign key(res_id) references resident(res_id) on delete cascade on update cascade);

create table works_in(emp_id int not null, off_id int not null, primary key(emp_id,off_id),foreign key(emp_id) references employee(emp_id) on delete cascade on update cascade,foreign key(off_id) references office(off_id) on delete cascade on update cascade);
create table has(off_id int not null,com_id int not null,primary key(off_id,com_id),foreign key(off_id) references office(off_id) on delete cascade on update cascade,foreign key(com_id) references community(com_id) on delete cascade on update cascade);


