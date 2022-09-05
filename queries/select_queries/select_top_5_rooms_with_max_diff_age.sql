SELECT rooms.name FROM rooms
INNER JOIN students ON rooms.id = students.room
GROUP BY rooms.name
ORDER BY EXTRACT(EPOCH FROM MAX(birthday)-MIN(birthday))/3600 DESC
LIMIT 5;
