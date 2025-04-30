t_0 = 69336.38
times = [
	69336.38,
	66590.00,
	71201.88,
	54545.75,
	43783.75,
	41770.88,
	42539.12,
	42944.88,
	43752.25
]

e_0 = 1459.70
energies = [
	1459.70,
	1406.83,
	1487.67,
	1145.00,
	913.07,
	882.50,
	899.01,
	898.14,
	908.58
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
