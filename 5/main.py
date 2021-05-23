import turtle as t

f = open("C:/haedal/5/turtle.txt", 'r')
lines = f.readlines()
t.shape('turtle')

for line in lines:
    val = float(line)
    i = lines.index(line)

    if i%2==0 :
        t.forward(val)
    else :
        t.right(val)
f.close()