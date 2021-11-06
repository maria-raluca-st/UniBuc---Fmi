--Tema 1 - Stanescu Maria Raluca
--Lab 0
--1.ex 9.De câte ori a împrumutat un membru(nume și prenume)fiecare film(titlu)?
select m.last_name as "Last Name", m.first_name as "First Name", t.title as "Title", count(t.title_id) as "Number of rentals"
from member m
join rental r on (r.member_id = m.member_id)
join title_copy c on (c.copy_id=r.copy_id and c.title_id=r.title_id)
join title t on (t.title_id=c.title_id)
group by t.title_id, t.title, m.last_name, m.first_name;
--order by m.last_name, m.first_name; 
--order by este optional , daca vrem sa afisam dupa numele si prenumele clientilor

--2.ex 10.De câte ori a împrumutat un membru(nume și prenume)fiecare exemplar(cod)al unui film(titlu)?
select m.last_name as "Last Name", m.first_name as "First Name", t.title as "Title", r.copy_id as "Copy of Movie" ,count(t.title_id) as "Number of rentals"
from member m
join rental r on (r.member_id = m.member_id)
join title_copy c on (c.copy_id=r.copy_id and c.title_id=r.title_id)
join title t on (t.title_id=c.title_id)
group by t.title_id, t.title, m.last_name, m.first_name, r.copy_id;
--order by m.last_name, m.first_name;

--3.ex 11.Obțineți statusul celui mai des împrumutat exemplar al fiecărui film(titlu).

select title as "Title", tc.status as "Status" 
from title_copy tc join title t on (t.title_id=tc.title_id)
where tc.copy_id = ( select copy_id 
                     from  (select tc.copy_id 
                            from rental r join title_copy tc on (r.copy_id=tc.copy_id)
                            group by tc.copy_id 
                            order by count(tc.copy_id) desc)
                            where rownum = 1);
--4.ex 12.Pentru anumite zile specificate din luna curentă,obțineți numărul de împrumuturi efectuate.
--a.Se iau în considerare doar primele 2 zile din lună.
SELECT d as "Date" , (
    select count(*) 
    from rental r where 
    extract(day from book_date) = extract(day from d)
    and extract(month from book_date) = extract(month from d))  as "Rentals"
     FROM(SELECT TRUNC (last_day(add_months(SYSDATE, -1)) + ROWNUM) d
     FROM DUAL CONNECT BY ROWNUM <= 2
     )


--b.Se iau în considerare doar zilele din lună în care au fost efectuate împrumuturi.
select extract( day from book_date) as "Days", count(*) as "Rentals"
from rental 
where extract(month from book_date) = 9
--pt sept.(pt ca in oct. nu s-au efectuat imprumuturi)
--where extract(month from book_date) = extract(month from SYSDATE)
--varianta corecta pt luna curenta, care nu afiseaza nimic.
group by book_date 
order by book_date asc;

--c.Se iau în considerare toate zilele din lună, incluzând în rezultat și zilele în care nu au fost efectuate împrumuturi.
    SELECT d as "Date" , (
    select count(*) 
    from rental r where 
    extract(day from book_date) = extract(day from d)
    and extract(month from book_date) = extract(month from d))  as "Rentals"
    FROM(SELECT TRUNC (last_day(add_months(SYSDATE, -1)) + ROWNUM) d
    FROM DUAL CONNECT BY ROWNUM <= extract(day from last_day(sysdate))
     )
