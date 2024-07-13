-- ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin, nb_fans FROM (
	SELECT origin, SUM(nb_fans) AS nb_fans
	FROM metal_bands
	GROUP BY origin
) AS ranked_countries
ORDER BY nb_fans DESC;
