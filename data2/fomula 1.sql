use  fomula1;

-- 바레인 그랑프리
SELECT 
	B.year,
    B.raceId,
    B.name,
    C.name,
	D.surname,
    A.q3
FROM
    qualifying A
LEFT JOIN
    races B ON A.raceId = B.raceId
left join 
	constructors C on A.constructorId = C.constructorId
left join 
	drivers D on A.driverId = D.driverId
WHERE 
    B.circuitId = 3;

-- 사우디 그랑프리
SELECT 
	B.year,
    B.raceId,
    B.name,
    C.name,
	D.surname,
    A.q3
FROM
    qualifying A
LEFT JOIN
    races B ON A.raceId = B.raceId
left join 
	constructors C on A.constructorId = C.constructorId
left join 
	drivers D on A.driverId = D.driverId
WHERE 
    B.circuitId = 77;

-- 오스트리아 그랑프리

SELECT 
	B.year,
    B.raceId,
    B.name,
    C.name,
	D.surname,
    A.q3
FROM
    qualifying A
LEFT JOIN
    races B ON A.raceId = B.raceId
left join 
	constructors C on A.constructorId = C.constructorId
left join 
	drivers D on A.driverId = D.driverId
WHERE 
    B.circuitId = 1;
    

-- 일본 그랑프리
SELECT 
	B.year,
    B.raceId,
    B.name,
    C.name,
	D.surname,
    A.q3
FROM
    qualifying A
LEFT JOIN
    races B ON A.raceId = B.raceId
left join 
	constructors C on A.constructorId = C.constructorId
left join 
	drivers D on A.driverId = D.driverId
WHERE 
    B.circuitId = 22;
    
-- 중국 그랑프리
SELECT 
	B.year,
    B.raceId,
    B.name,
    C.name,
	D.surname,
    A.q3
FROM
    qualifying A
LEFT JOIN
    races B ON A.raceId = B.raceId
left join 
	constructors C on A.constructorId = C.constructorId
left join 
	drivers D on A.driverId = D.driverId
WHERE 
    B.circuitId = 17;
    
-- 마이애미 그랑프리
SELECT 
	B.year,
    B.raceId,
    B.name,
    C.name,
	D.surname,
    A.q3
FROM
    qualifying A
LEFT JOIN
    races B ON A.raceId = B.raceId
left join 
	constructors C on A.constructorId = C.constructorId
left join 
	drivers D on A.driverId = D.driverId
WHERE 
    B.circuitId = 79;
    
    
-- 모나코 그랑프리
SELECT 
	B.year,
    B.raceId,
    B.name,
    C.name,
    D.surname,
    A.q3
FROM
    qualifying A
LEFT JOIN
    races B ON A.raceId = B.raceId
left join 
	constructors C on A.constructorId = C.constructorId
left join 
	drivers D on A.driverId = D.driverId
WHERE 
    B.circuitId = 6;