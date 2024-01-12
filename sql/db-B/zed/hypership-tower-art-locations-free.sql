-- Zed
-- Where can we put artwork?

USE zed_prod;

SET @max_tower_floor = 100;

-- Counters T and C for T1C1..T100C6
WITH RECURSIVE counter_tower AS (
  SELECT 1 AS floor_counter, 1 AS corridor
  UNION ALL
  SELECT 
    (CASE
      WHEN corridor < 6 THEN floor_counter
      WHEN corridor = 6 THEN floor_counter + 1
    END) AS floor_counter,
    (CASE
      WHEN corridor < 6 THEN corridor + 1
      WHEN corridor = 6 THEN 1
    END) AS corridor
  FROM counter_tower
  WHERE floor_counter < @max_tower_floor
)

SELECT
    location_local
FROM
    (SELECT CONCAT("T", floor_counter, "C", corridor) as location_local FROM counter_tower) as locations
WHERE
    location_local NOT IN (
        SELECT DISTINCT location_local
        FROM content_locations
        WHERE location_global = "B00001001" -- Hypership tower        
    )
;
