CREATE TABLE PRIZETHIRTY
       (
       DAY VARCHAR(4),
       MONTH VARCHAR(15),
       YEAR VARCHAR(5),
       
       FIRSTPRIZE VARCHAR(8),
       TWOUP VARCHAR(3),
       TWODOWN VARCHAR(3),
       THREEUP VARCHAR(4),
       THREEFRONT1 VARCHAR(4),
       THREEFRONT2 VARCHAR(4),
       THREEDOWN1 VARCHAR(4),
       THREEDOWN2 VARCHAR(4),
       
       PRIMARY KEY (DAY, MONTH, YEAR)
       );


-- select * from "PRIZETHIRTY" order by YEAR DESC, MONTH DESC, DAY DESC;

SELECT TWOUP, COUNT(TWOUP) AS SUM from "PRIZETHIRTY" 
WHERE (DAY = "1" OR DAY = "31" OR DAY = "30" OR DAY = "2") 
	AND (MONTH = "12") AND (CAST("YEAR" AS INTEGER) >= 2550) 
GROUP BY "TWOUP"
HAVING COUNT("TWOUP") > 1
order by COUNT("TWOUP") DESC;