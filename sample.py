
import numpy as np 
l1 = float (input("Enter the length(in m)->"))
l2 = float (input("Enter second length(in m)->"))
ly = max (l1 , l2)
lx = min (l1 , l2)
ratio = ly/lx
d = float (input("Enter the Depth(in m)->"))
l = float (input("Enter the U.D.Live Load(in kN)->"))
volume = lx*ly*d
dead_load = 2.5*volume
total_load = dead_load+l
w = 1.5*total_load
with open("ffs.txt") as f:
    a = f.readlines()


b = []
for line in a:
    array = [float(x) for x in line[:-1].split(" ")]
    b.append(array)

b = np.asarray(b)
#print(b)
r=len(b)
c=len(b[0])
ans=-1
for i in range(0,c):
        if b[0][i] >= ratio:
            ans=i               #ratio col no.
            break;
#print(ans)
print("\nEnter the conditions available from the given data \n\n 1.Interior Panel \n 2.One short Edge continuous \n 3.One Long Edge Discontinuous \n 4.Two Adjacent edges Discontinuous \n 5.Two short Edges Discontinuous \n 6.Two long Edges Discontinuous \n 7.Three edges Discontinuous(One long Edge Discontinuous) \n 8.Three edges discontinuous(One short Edge Continuous) \n 9.Four edges discontinuous \n")
l3 = int(input("Enter the Condition->"))
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
        alphaxn1=b[rn][ans-1]
        alphaxp2=b[rp][ans]
        alphaxp1=b[rp][ans-1]
        alphaxn=alphaxn1 + (alphaxn2-alphaxn1)*(ratio-b[0][ans-1])/(b[0][ans]-b[0][ans-1])
        alphaxp=alphaxp1 + (alphaxp2-alphaxp1)*(ratio-b[0][ans-1])/(b[0][ans]-b[0][ans-1])
    Mxn = alphaxn*w*lx*lx
    Mxp = alphaxp*w*lx*lx
    print("\nAlpha x(-) = "+str(alphaxn))
    print("Alpha x(+) = "+str(alphaxp))
    if Mxn == 0:
        print("Mx(-) condition doesnot exist")
    else:
        print("Mx(-) =", Mxn)
    if Mxp == 0:
        print("Mx(+) condition doesnot exist")
    else:
        print("Mx(+) =", Mxp)
ansy=c-1
alphayn = b[rn][ansy]
#print(alphaxn)
alphayp = b[rp][ansy]
Myn = alphayn*w*lx*lx
Myp = alphayp*w*lx*lx
if Myn == 0:
    print("My(-) condition doesnot exist")
else:
    print("My(-) =", Myn)
if Myp == 0:
    print("My(+) condition doesnot exist")
else:
    print("My(+) =", Myp)
if ratio <=2:
    print("It's a two way slab")
else:
    print("One way slab")
print("Ratio is =",ratio)
lx1 = 100*lx
ly1 = 100*ly
from tkinter import Tk, Canvas, Frame, BOTH, W
class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
      
        self.master.title("Colours")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(20, lx1+20, ly1+20, 20, 
            outline="#fb0", fill="#fb0")
        canvas.create_text(0, 10, anchor=W, font="Purisa",
            text="(0,"+str(lx)+")")
        canvas.create_text(0, 30+lx1, anchor=W, font="Purisa",
            text="(0,0)")
        canvas.create_text(ly1, 10, anchor=W, font="Purisa",
            text="("+str(ly)+","+str(lx)+")")
        canvas.create_text(ly1, 30+lx1, anchor=W, font="Purisa",
            text="("+str(ly)+",0)")
        canvas.create_line(ly1/2+10, lx1/2+20, ly1/2+30, lx1/2+20)
        canvas.create_line( ly1/2+20,lx1/2 + 10, ly1/2+20, lx1/2+30)
        canvas.create_text(ly1/2+30, lx1/2+20, anchor=W, font="Purisa",
            text="Mx+")
        canvas.create_text(ly1+30, lx1/2+20, anchor=W, font="Purisa",
            text="Mx-")
        canvas.create_text(ly1/2+10, lx1/2, anchor=W, font="Purisa",
            text="My+")
        canvas.create_text(ly1/2, lx1+40, anchor=W, font="Purisa",
            text="My-")          
        canvas.pack(fill=BOTH, expand=1)


def main():
  
    root = Tk()
    ex = Example()
    root.geometry("400x100+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()