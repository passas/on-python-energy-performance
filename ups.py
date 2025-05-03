t_0 = 74127.62
times = [
	74127.62,
	48568.75,
	53765.00,
	25517.12,
	26286.38,
	25207.62,
	25268.62,
	29059.25,
	29357.50,
]

e_0 = 1729.51
energies = [
	1729.51,
	1036.47,
	1153.91,
	531.16,
	550.93,
	536.45,
	536.49,
	572.52,
	591.31,
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
