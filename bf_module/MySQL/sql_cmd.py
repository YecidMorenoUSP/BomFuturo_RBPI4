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

sql_get_sensors = """
SELECT s.sensor_id, s.type, s.topic, s.description, hr.date, hr.value as last_value
FROM sensor s
    INNER JOIN humidity_reads hr ON s.sensor_id = hr.sensor_id
    INNER JOIN (
        SELECT sensor_id, MAX(date) AS max_date
        FROM humidity_reads
        GROUP BY sensor_id
    ) t ON hr.sensor_id = t.sensor_id AND hr.date = t.max_date
ORDER by sensor_id DESC
"""