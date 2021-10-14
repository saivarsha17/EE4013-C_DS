Sum=0.0
i=2.0
j=1.0
while(i/j>0.0625):
    j=j+j
    Sum=Sum+i/j
    print(Sum)