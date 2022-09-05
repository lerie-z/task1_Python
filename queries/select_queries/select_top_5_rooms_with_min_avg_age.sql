SELECT rooms.name FROM rooms
INNER JOIN students ON rooms.id = students.room
GROUP BY rooms.name
ORDER BY AVG((EXTRACT(EPOCH FROM current_timestamp - birthday)/3600))
LIMIT 5;