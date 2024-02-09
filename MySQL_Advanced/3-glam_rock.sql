-- write an SQL script that lists all bands with Glam rock as their main
-- style, ranked by their longevity

SELECT band_name,
    (YEAR(SPLIT(lifespan, '-')[2]) - YEAR(SPLIT(lifespan, '-')[1])) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;
