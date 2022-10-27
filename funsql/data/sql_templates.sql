--> sample10
-- sample 10 rows
SELECT * FROM {tbl} LIMIT 10;


--> drop
-- drop a table
DROP TABLE IF EXISTS ess_enc.e085206_{tbl_name};


--> columns
-- show list of columns in the table
SELECT *
  FROM information_schema.columns
 WHERE table_schema = '{your_schema}'
   AND table_name   = '{your_table}'
     ;