DELIMITER //
CREATE PROCEDURE GetSensorReport(IN sensor_id_in INT)
BEGIN
    -- Última lectura de cada sensor
    IF sensor_id_in = '0' THEN
        SELECT s.sensor_id, s.topic, h.value AS last_value, h.time_ts AS last_reading_date,
               (SELECT MAX(value) FROM humidity_reads WHERE sensor_id = s.sensor_id AND time_ts >= NOW() - INTERVAL 1 HOUR) AS max_hour,
               (SELECT MAX(value) FROM humidity_reads WHERE sensor_id = s.sensor_id AND time_ts >= NOW() - INTERVAL 1 DAY) AS max_day,
               s.description
        FROM sensor s
        LEFT JOIN humidity_reads h ON s.sensor_id = h.sensor_id
        WHERE h.time_ts = (SELECT MAX(time_ts) FROM humidity_reads WHERE sensor_id = s.sensor_id)
        ORDER BY s.sensor_id;
    ELSE
        SELECT s.sensor_id, s.topic, h.value AS last_value, h.time_ts AS last_reading_date,
               (SELECT MAX(value) FROM humidity_reads WHERE sensor_id = s.sensor_id AND time_ts >= NOW() - INTERVAL 1 HOUR) AS max_hour,
               (SELECT MAX(value) FROM humidity_reads WHERE sensor_id = s.sensor_id AND time_ts >= NOW() - INTERVAL 1 DAY) AS max_day,
               s.description
        FROM sensor s
        LEFT JOIN humidity_reads h ON s.sensor_id = h.sensor_id
        WHERE
            s.sensor_id = sensor_id_in AND
            h.time_ts = (SELECT MAX(time_ts) FROM humidity_reads WHERE sensor_id = s.sensor_id)
        ORDER BY s.sensor_id;
    END IF;
END //
DELIMITER ;


DELIMITER //

CREATE PROCEDURE GetLastSensorDataByTopic(IN topic_in VARCHAR(255), IN hr_id_in INT)
BEGIN
    SELECT hr.*
    FROM (
        SELECT *
        FROM humidity_reads
        WHERE hr_id > hr_id_in
        ORDER BY time_ts DESC
        LIMIT 100
    ) hr
    INNER JOIN sensor s ON hr.sensor_id = s.sensor_id
    WHERE s.topic = topic_in
    ORDER BY hr.time_ts ASC;
END //

DELIMITER ;



DELIMITER //

CREATE PROCEDURE InsertSensorReading(IN topic_in VARCHAR(255), IN value_in Float, IN payload_in JSON)
BEGIN
    DECLARE sensor_id_var INT;
    
    -- Obtener el sensor_id asociado al topic
    SELECT sensor_id INTO sensor_id_var
    FROM sensor
    WHERE topic = topic_in;
    
    -- Insertar la nueva lectura
    INSERT INTO humidity_reads (sensor_id, value, payload)
    VALUES (sensor_id_var, value_in, payload_in);
    

END //

DELIMITER ;

