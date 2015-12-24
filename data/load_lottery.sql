begin;

create table temp(
  city varchar,
  population varchar,
  aid_given varchar,
  gross_lottery_sales varchar,
  spare varchar
);

create table lottery(
  city varchar,
  population integer,
  aid_given numeric,
  gross_lottery_sales numeric
);

\copy temp from '/Users/benkaufman/Desktop/lottery_sales/Data-Table 1.csv' with csv header;

insert into lottery(city, population, aid_given, gross_lottery_sales)
select
  city,
  replace(population, ',', '')::integer,
  replace(replace(aid_given, '$', ''),',','')::numeric,
  replace(replace(gross_lottery_sales, '$', ''),',','')::numeric
from temp;

insert 

commit;
