t_0 = 57264.50
times = [
	57264.50,
	53185.88,
	54261.88,
	54555.38,
	56117.38,
	66509.00,
	1541.00
]

e_0 = 1202.77
energies = [
	1202.77,
	1121.72,
	1147.61,
	1138.28,
	1169.45,
	1414.98,
	32.86
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
