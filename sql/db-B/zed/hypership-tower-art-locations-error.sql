-- Zed
-- Do we have hidden artwork?

USE zed_prod;

SELECT
    location_local, k
FROM
    content_locations
WHERE
    location_global = "B00001001" -- Hypership tower
    AND k NOT IN (1, 2, 3)        -- Expected positions
ORDER BY location_local, k ASC;
