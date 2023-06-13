sql_last_values = """
SELECT * FROM (
    SELECT date,value FROM `humidity_reads` 
    ORDER BY `date` DESC LIMIT 100 
) Q1 ORDER BY `date` ASC;
"""

sql_last_values_from ="""
SELECT * FROM ( 
    SELECT date,value FROM `humidity_reads` 
    WHERE date > FROM_UNIXTIME(%s) 
    ORDER BY `date` DESC LIMIT 20 
) Q1 ORDER BY `date` ASC;
"""