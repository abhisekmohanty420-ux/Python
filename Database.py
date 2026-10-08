import mysql.connector as mc
db=mc.connect(
     host="localhost",
     user="root",
     password="sonu@abhisek",
     database="student"
     )
curs=db.cursor()
if curs:
    print("database connected")
curs.execute("USE student")
sql='''
create table student(
    id bigint not null primary key auto_increment,
    name varchar(50) not null,
    email varchar(50) unique not null,
    date_of_birth varchar(30) not null
)
'''
curs.execute(sql)
sql='''
INSERT INTO student (name, email, date_of_birth) VALUES
('Abhishek Mohanty', 'abhishek@gmail.com', '2005-01-15'),
('Rahul Sharma', 'rahul@gmail.com', '2004-03-22'),
('Priya Singh', 'priya@gmail.com', '2005-07-10'),
('Aman Kumar', 'aman@gmail.com', '2004-11-05'),
('Sneha Das', 'sneha@gmail.com', '2005-02-18'),
('Rohit Patnaik', 'rohit@gmail.com', '2004-09-12'),
('Ananya Mishra', 'ananya@gmail.com', '2005-06-25'),
('Vivek Sahu', 'vivek@gmail.com', '2004-12-30'),
('Neha Gupta', 'neha@gmail.com', '2005-04-08'),
('Karan Mehta', 'karan@gmail.com', '2004-08-19'),
('Pooja Nair', 'pooja@gmail.com', '2005-10-14'),
('Arjun Das', 'arjun@gmail.com', '2004-01-27'),
('Riya Patel', 'riya@gmail.com', '2005-05-03'),
('Sourav Behera', 'sourav@gmail.com', '2004-06-16'),
('Kavya Reddy', 'kavya@gmail.com', '2005-09-21'),
('Aditya Joshi', 'aditya@gmail.com', '2004-10-11'),
('Simran Kaur', 'simran@gmail.com', '2005-03-07'),
('Nikhil Verma', 'nikhil@gmail.com', '2004-05-29'),
('Ishita Roy', 'ishita@gmail.com', '2005-08-17'),
('Manish Yadav', 'manish@gmail.com', '2004-02-09');
'''
curs.execute(sql)
db.commit()
curs.execute("select * from student")
for i in curs.fetchall():
    print(i)

sql="insert into student (name,email,date_of_birth) values(%s,%s,%s)"
values=[
('Rakesh Kumar', 'rakesh@gmail.com', '2005-11-12'),
('Meera Sharma', 'meera@gmail.com', '2004-07-24'),
('Sanjay Das', 'sanjay@gmail.com', '2005-03-19'),
('Tanvi Patel', 'tanvi@gmail.com', '2004-12-06'),
('Akash Behera', 'akash@gmail.com', '2005-09-28')
]    
curs.executemany(sql,values)
db.commit()
sql='''update student set name="Abhisek Mohanty" where id=21'''
curs.execute(sql)
db.commit()
sql='''delete from student where id=44'''
curs.execute(sql)
db.commit()
curs.execute("select * from student")
for i in curs.fetchall():
    print(i)