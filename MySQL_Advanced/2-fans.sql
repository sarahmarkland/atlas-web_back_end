-- write an SQL script that ranks country origins of bands
-- ordered by the nuymber of (non-unique) fans in each country

SELECT origin, SUM(nb_fans) AS nb_fans
FROM (
    SELECT
        CASE
            WHEN origin LIKE '%,%' THEN origin
            ELSE origin
        END AS origin,
        nb_fans
    FROM metal_bands
) AS band_countries
GROUP BY origin
ORDER BY nb_fans DESC;
