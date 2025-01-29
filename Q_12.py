x, y = 3, 4
cx, cy = 0, 0
radius = 5

distance_sq = (x - cx) ** 2 + (y - cy) ** 2
radius_sq = radius ** 2

if distance_sq < radius_sq:
    position = "Inside"
elif distance_sq == radius_sq:
    position = "On"
else:
    position = "Outside"

