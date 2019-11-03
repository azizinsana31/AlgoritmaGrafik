print("=============")
print("Algoritma DDA")
print("=============")

x1 = 3 
y1 = 6
x2 = 14
y2 = 10

Dx = x2 - x1
Dy = y2 - y1
r = 0

if(Dx > Dy):
    r = Dx  
else:
    r = Dy

Xr = Dx / r
Yr = Dy / r
str = "Dx : {0} \nDy : {1} \nr  : {2} \nXr : {3} \nYr : {4}"
print(str.format(Dx, Dy, r, Xr, Yr))

x = x1 + Xr
y = y1 + Yr
str2 = "\nx : {0:.3f} | y : {1:.3f} \n"
print(str2.format(x, y))

while(True):
    x = x + Xr
    y = y + Yr
    x_round = int(round(x))
    y_round = int(round(y))

    str2 = "x : {0:.3f} | y : {1:.3f} | x_round : {2} | y_round : {3}"
    print(str2.format(x, y, x_round, y_round))
    if(x_round == x2 and y_round == y2):
      break



    
