CREATE TABLE IF NOT EXISTS aollog ( userid String, query String,
time DATE, rank INT, clickurl String)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;


LOAD DATA LOCAL INPATH '/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL1.txt'
OVERWRITE INTO TABLE aollog;



INSERT OVERWRITE TABLE t1
select userid from aollog;

select count(*) from t1;

CREATE TABLE aollogs(userid text, query text, qtime DATETIME(), rank int, clickurl text);
CREATE TABLE aollogs(userid varchar(255), query varchar(255), qtime DATETIME, rank int NOT NULL DEFAULT -1, clickurl varchar(255));
CREATE TABLE aollogs(userid text, query text, qtime DATETIME, rank text, clickurl text);

load data infile '/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL1.txt' into table aollogs;
load data infile '/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL2.txt' into table aollogs;
load data infile '/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL3.txt' into table aollogs;

CREATE TABLE entity(entity text, info text);
CREATE TABLE queryentity(query text, entity text, info text);
load data infile '/Users/rishabhmehrotra/dev/UCL/projects/entity/queryentity.txt' into table entity;
load data infile '/Users/rishabhmehrotra/dev/UCL/projects/entity/queryentity.txt' into table queryentity;

CREATE TABLE uqe(userid text, query text, entity text);
insert into uqe select aollogs.userid, aollogs.query, queryentity.entity from aollogs left outer join queryentity ON aollogs.query = queryentity.query;

CREATE TABLE qe(query text, entity text);
alter table queryentity modify entity VARCHAR(255);
alter table queryentity modify query VARCHAR(255);
alter table queryentity ADD INDEX (entity);
alter table aollogs modify userid VARCHAR(255);
alter table aollogs modify query VARCHAR(255);

CREATE TABLE aollogs(userid VARCHAR(255), query VARCHAR(255), qtime DATETIME, rank VARCHAR(255), clickurl VARCHAR(255));
load data infile '/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL1.txt' into table aollogs IGNORE 1 LINES;

alter table uqe modify userid VARCHAR(255);
alter table uqe modify entity VARCHAR(255);
alter table uqe modify query VARCHAR(255);

CREATE TABLE qe(query VARCHAR(255), entity VARCHAR(255), info text);
load data infile '/Users/rishabhmehrotra/dev/UCL/projects/entity/queryentity.txt' into table qe;
Query OK, 13617693 rows affected, 261 warnings (2 min 2.77 sec)
Records: 13617693  Deleted: 0  Skipped: 0  Warnings: 261

alter table qe ADD INDEX (entity);
Query OK, 0 rows affected (30.38 sec)
Records: 0  Duplicates: 0  Warnings: 0

alter table qe ADD INDEX (query);
Query OK, 0 rows affected (40.25 sec)
Records: 0  Duplicates: 0  Warnings: 0

alter table aollogs ADD INDEX (userid);
alter table aollogs ADD INDEX (query);
SET sql_mode = '';
load data infile '/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL1.txt' into table aollogs IGNORE 1 LINES;
alter table uqe ADD INDEX (userid);
alter table uqe ADD INDEX (query);
alter table uqe ADD INDEX (entity);

insert into uqe select aollogs.userid, aollogs.query, qe.entity from aollogs left outer join qe ON aollogs.query = qe.query;
Query OK, 4571271 rows affected (9 min 1.76 sec)
Records: 4571271  Duplicates: 0  Warnings: 0


SELECT table_schema                                        "DB Name", 
   Round(Sum(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB" 
FROM   information_schema.tables 
GROUP  BY table_schema;


mysql> describe aollogs;
+----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| userid   | varchar(255) | YES  | MUL | NULL    |       |
| query    | varchar(255) | YES  | MUL | NULL    |       |
| qtime    | datetime     | YES  |     | NULL    |       |
| rank     | varchar(255) | YES  |     | NULL    |       |
| clickurl | varchar(255) | YES  |     | NULL    |       |
+----------+--------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

mysql> describe qe
    -> ;
+--------+--------------+------+-----+---------+-------+
| Field  | Type         | Null | Key | Default | Extra |
+--------+--------------+------+-----+---------+-------+
| query  | varchar(255) | YES  | MUL | NULL    |       |
| entity | varchar(255) | YES  | MUL | NULL    |       |
| info   | text         | YES  |     | NULL    |       |
+--------+--------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

mysql> describe uqe;
+--------+--------------+------+-----+---------+-------+
| Field  | Type         | Null | Key | Default | Extra |
+--------+--------------+------+-----+---------+-------+
| userid | varchar(255) | YES  | MUL | NULL    |       |
| query  | varchar(255) | YES  | MUL | NULL    |       |
| entity | varchar(255) | YES  | MUL | NULL    |       |
+--------+--------------+------+-----+---------+-------+




