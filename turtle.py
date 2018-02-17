from turtle import *
color('red','yellow')
bgcolor('black')
begin_fill()
while True:
	left(170)
	forward(200)
	if abs(pos())<1:
		break
end_fill()
done()
ht()