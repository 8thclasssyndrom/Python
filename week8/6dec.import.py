"""
Тема: Индексы. Импорт и экспорт данных.

Индексы в PostgreSQL - специальные объекты базы данных, предназначенные в основном для ускорения доступа к данным.

Если создать в система индекс по полю id, она сможет находить строки гораздо быстрее.

create index
drope index 

Когда индекс создан, никакие дополнительные действия не требуются.

Типы индексов:
1. В-дерево(бинарного дерево, создается по умолчанию)
2. Хеш
3. GiST
4. SP-GiST
5. GIN
6. BRIN

Индексы можно создавать по нескольким столбцам таблицы.

Индекс замедляет вставку, обновление и удаление записей(INSERT, UPDATE, DELETE)

Индекс требует много места - заполняет память.

psql db_name < input_file.sql

pg_dump db_name > output_file.sql

Индексы - это определенная конструкция, суть которой заключается в упрощении и ускорении поиска нужной строки или строк.



"""


"""
Начало практики

Индексы - ускоряет выборку

CREATE INDEX index_name ON table_name(column);

Бинарное дерево - b3
- иерархическая система данных в виде узла


Экспорт:

pg_dump название_бд > название_файла.sql

SELECT * FROM wordform GROUP BY plaintext HAVING COUNT(*) >= ALL (SELECT COUNT(*) FROM wordfrom GROUP BY plaintext)	
"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""
Tasks
Таски

#1
select plaintext from wordform limit 10;

#2
select plaintext from wordform where plaintext like'a%';

#3
select title, genretype from work where genretype = 'p';

#4
select avg(totalparagraphs) as avg from work where genretype = 't';

#5
select title from work where totalwords > (select avg(totalwords) from work);

#6

select ch.charname,ch.speechcount,w.title from character_work as ch_w inner join character as ch on ch.charid=ch_w.charid 
inner join work as w on w.workid=ch_w.workid;

#7
select (select round(avg(c.speechcount)) as round from character as c  inner join character_work as ch_w on 
c.charid=ch_w.charid inner join work as w on ch_w.workid = w.workid where w.title = 'Romeo and Juliet'), title from work 
where title = 'Romeo and Juliet';

#8
select section, sum(wordcount) as sum from paragraph group by section ;

#9
select charname, speechcount from character where speechcount between 15 and 30;

#10
select title, year from work where year between 1601 and 1699;

#11
select longtitle from work where longtitle like '%the%';

#12
select distinct section from paragraph;

#13
select c.chapterid, c.description, w.title from chapter as c inner join work as w on c.workid=w.workid;

#14
select p.paragraphnum, c.charname, c.speechcount from character as c inner join paragraph as p on c.charid = p.charid;

#15
select p.paragraphnum, w.title, w.year from work as w inner join paragraph as p on w.workid = p.workid;


"""


"""


"""

"""


"""

"""


"""

"""


"""

"""
"""
