-- Zed
-- Where do we have artwork?

USE zed_prod;

SELECT
    DISTINCT location_local
FROM
    content_locations
WHERE
    location_global = "B00001001" -- Hypership tower
ORDER BY location_local ASC;
