-- write an SQL script that ranks country origins of bands
-- ordered by the nuymber of (non-unique) fans in each country

SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
