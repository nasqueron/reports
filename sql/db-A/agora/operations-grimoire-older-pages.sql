-- Agora
-- What Operations Grimoire pages are older than 6 months?

USE nasqueron_wiki;

SELECT
    -- page_link example: [Operations grimoire/Kubernetes|Kubernetes]]
    REPLACE(CONCAT("[[", page_title, "|", SUBSTRING(page_title, 21), "]]"), "_", " ") as page_link,

    -- age in days (1 day = 86400 seconds)
    FLOOR((UNIX_TIMESTAMP() - UNIX_TIMESTAMP(page_touched)) / 86400) as age
FROM
    page
WHERE
    LEFT(page_title, 20) = "Operations_grimoire/"
    AND LEFT(page_title, 29) != "Operations_grimoire/Incidents"
HAVING age > 180
ORDER BY page_touched DESC;
