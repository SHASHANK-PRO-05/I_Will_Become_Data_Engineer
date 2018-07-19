# If table is of form


| Sid  | SKey  | Svalue   |
|:---:|:---:|:---:|
| 1 |firstName |Shashank|
| 2 |lastName |Kapoor|


 ```sql
# SET GLOBAL group_concat_max_len = 10000; //Optional if you have a lot of columns
#SET SESSION group_concat_max_len = 10000; //Optional if you have a lot of columnss 
set @SQL = null;
select GROUP_CONCAT(distinct 'group_concat(if(skey=''', skey, "'", ', svalue, NULL)) as ''', skey, "'")
into @SQL
from SourceOutput;

SET @SQL = CONCAT(' SELECT sid, ', @SQL, '
                    FROM SourceOutput
                    GROUP BY sid ');

PREPARE stmt FROM @SQL;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

## How this is working?

1. First we created a SQL statement which helped us in evading hard coding. You don't want to do that.
1. Next we prepared and SQL statement and inserted what we want.
1. Run it. 