drop table steptwo;
drop table stepfour;
drop table stepthree;
drop table tfidf;

create table steptwo(docid STRING, term_count INT) row format delimited fields terminated by '\t';
load data inpath '/user/training/data-output/doc-length/part-00000' into table steptwo;

create table stepthree(docid STRING, term STRING, term_count INT) row format delimited fields terminated by '\t';
load data inpath '/user/training/data-output/split-doc-term/part-00000'into table stepthree;

create table stepfour(term STRING, unique_id INT) row format delimited fields terminated by '\t';
load data inpath '/user/training/data-output/doc-freq/part-00000' into table stepfour;

CREATE TABLE tfidf ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/user/training/data-output/tfidf' AS SELECT stepthree.docid, stepthree.term, stepthree.term_count/steptwo.term_count/stepfour.unique_id FROM stepthree LEFT JOIN steptwo ON stepthree.docid = steptwo.docid LEFT JOIN stepfour ON stepthree.term = stepfour.term ORDER BY docid; 

