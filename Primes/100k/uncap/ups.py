t_0 = 51056.75
times = [
	51056.75,
	50856.25,
	55.00,
]

e_0 = 1247.31
energies = [
	1247.31,
	1217.62,
	0.91,
]

speed_up = []
for t in times:
	speed_up.append(t_0/t)

green_up = []
for e in energies:
	green_up.append(e_0/e)

power_up = []
for i in range(0,len(speed_up)):
	power_up.append(speed_up[i]/green_up[i])

print('Powerup | Speedup | Greenup')
print(27*'-')
for i in range(0,len(power_up)):
	print(f'{power_up[i]:.2f}    |   {speed_up[i]:.2f}  |   {green_up[i]:.2f}')
