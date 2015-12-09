drop table if exists data;
    create table data(
      id integer primary key autoincrement,
      date_created text not null,
      name text not null,
      email text not null
);      	   
