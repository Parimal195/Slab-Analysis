
import numpy as np                                                          #importing library
l1 = float (input("Enter the length end-to-end(in m)->"))                   #taking data from user
l2 = float (input("Enter second length end-to-end(in m)->"))
lm = max (l1 , l2)
ln = min (l1 , l2)
d = float (input("Enter the Depth of slab(in m)->"))
w = float (input("Enter the width of beam(in m)->"))
l = float (input("Enter the U.D.Live Load(in kN/m^2)->"))
print("\nEnter the conditions available from the given data \n\n 1.Interior Panel \n 2.One short Edge continuous \n 3.One Long Edge Discontinuous \n 4.Two Adjacent edges Discontinuous \n 5.Two short Edges Discontinuous \n 6.Two long Edges Discontinuous \n 7.Three edges Discontinuous(One long Edge Discontinuous) \n 8.Three edges discontinuous(One short Edge Continuous) \n 9.Four edges discontinuous \n")
l3 = int(input("Enter the Condition->"))

if l3 == 1:                                                                 #different conditions for effective length
    ly = lm - w
    lx = ln - w
elif l3 == 2:
    ly = lm - w
    lx = ln - (0.5*w+w)
elif l3 == 3:
    ly = lm - 1.5*w
    lx = ln-w
elif l3 == 4:
    ly = lm - 1.5*w
    lx = ln - 1.5*w
elif l3 == 5:
    ly = lm-w
    lx = ln-w
elif l3 == 6:
    ly = lm-w
    lx = ln-w
elif l3 == 7:
    ly = lm-1.5*w
    lx = ln-w
elif l3 == 8:
    ly = lm-w
    lx = ln-1.5*w
elif l3 == 9:
    ly = lm-w
    lx = ln-w

print("Effective length(ly)= ", ly)                                        #printing the value of effective length
print("Effective length(lx)= ", lx)

ratio = ly/lx                                                             #calculating the ratio for alpha value or type of slab
volume = lm*ln*d                                                           #calculating volume
dead_load = 2.5*volume                                                     #calculating dead load
total_load = dead_load+l                                                   #total load
w = 1.5*total_load

print("W is ",w)                                                           #Weight of the slab

with open("ffs.txt") as f:                                                 #open file where the value of alpha is stored
    a = f.readlines()

b = []
for line in a:
    array = [float(x) for x in line[:-1].split(" ")]                       #add data to matrix
    b.append(array)
b = np.asarray(b)

r=len(b)
c=len(b[0])
ans=-1

for i in range(0,c):
        if b[0][i] >= ratio:
            ans=i                                                          #getting the value of condition
            break;

rn = 2*l3-1
rp = 2*l3

if ans==-1:
    print("One way slab i.e. ratio is greater than 2.0")
else:
    if b[0][ans]==ratio:
        alphaxn = b[rn][ans]
        #print(alphaxn)
        alphaxp = b[rp][ans]
    else:
        alphaxn2=b[rn][ans]
        alphaxn1=b[rn][ans-1]                                               #getting the value of alpha
        alphaxp2=b[rp][ans]
        alphaxp1=b[rp][ans-1]
        alphaxn=alphaxn1 + (alphaxn2-alphaxn1)*(ratio-b[0][ans-1])/(b[0][ans]-b[0][ans-1])                  #interpolating the value of alpha
        alphaxp=alphaxp1 + (alphaxp2-alphaxp1)*(ratio-b[0][ans-1])/(b[0][ans]-b[0][ans-1])

    Mxn = round(alphaxn*w*lx*lx, 2)                                          #calculating moment for alpha x
    Mxp = round(alphaxp*w*lx*lx, 2)

    print("\nAlpha x(-) = "+str(alphaxn))
    print("Alpha x(+) = "+str(alphaxp))

    if Mxn == 0:
        print("Mx(-) condition doesnot exist")                              #Special conditions of moment
    else:
        print("Mx(-) =", Mxn)
    if Mxp == 0:
        print("Mx(+) condition doesnot exist")
    else:
        print("Mx(+) =", Mxp)
ansy=c-1
alphayn = b[rn][ansy]
alphayp = b[rp][ansy]

Myn = round(alphayn*w*lx*lx, 2)                                             #calculating moment for apha y
Myp = round(alphayp*w*lx*lx, 2)

if Myn == 0:
    print("My(-) condition doesnot exist")
else:
    print("My(-) =", Myn)
if Myp == 0:
    print("My(+) condition doesnot exist")                                  #printing the value of moment
else:
    print("My(+) =", Myp)
if ratio <=2:
    print("It's a two way slab")
else:
    print("One way slab")

print("Ratio is =",ratio)

lx1 = 100*ln                                                                #defining the pixles of graph
ly1 = 100*lm

from tkinter import Tk, Canvas, Frame, BOTH, W                              #importing library for graph
class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
      
        self.master.title("Colours")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(20, lx1+20, ly1+20, 20,                     #drawing the slab
            outline="#fb0", fill="#fb0")
        canvas.create_text(0, 10, anchor=W, font="Purisa",
            text="(0,"+str(ln)+")")
        canvas.create_text(0, 30+lx1, anchor=W, font="Purisa",
            text="(0,0)")
        canvas.create_text(ly1, 10, anchor=W, font="Purisa",
            text="("+str(lm)+","+str(ln)+")")
        canvas.create_text(ly1, 30+lx1, anchor=W, font="Purisa",
            text="("+str(lm)+",0)")
        canvas.create_line(ly1/2+10, lx1/2+20, ly1/2+30, lx1/2+20)
        canvas.create_line( ly1/2+20,lx1/2 + 10, ly1/2+20, lx1/2+30)
        canvas.create_text(ly1/2+30, lx1/2+20, anchor=W, font="Purisa",
            text="My+ =("+str(Myp)+")")
        #canvas.create_text(ly1/2+70, lx1/2+20, anchor=W, font="Purisa",
            #text="("+str(Mxp)+")")
        canvas.create_text(ly1+30, lx1/2+20, anchor=W, font="Purisa",      #printing the values of moment
            text="My- =("+str(Myn)+")")
        canvas.create_text(ly1/2+10, lx1/2, anchor=W, font="Purisa",
            text="Mx+ =("+str(Mxp)+")")
        canvas.create_text(ly1/2, lx1+40, anchor=W, font="Purisa",
            text="Mx- =("+str(Mxn)+")")          
        canvas.pack(fill=BOTH, expand=1)


def main():
  
    root = Tk()
    ex = Example()
    root.geometry("400x100+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()
