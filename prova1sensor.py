s = "Sensor"
print(s[1:4])

temp = 25.678 
print(f"{temp:.1f}")

temp = 95

if temp >= 70:
    status = "Atenção"
elif temp >=90:
    status= "CRÍTICO"
else:
    status = "NORMAL"


print(status)

i = 0
while i < 3:
    i += 1
print(i)