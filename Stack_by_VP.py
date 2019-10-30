

import queue as a
def dis(self):                                   #display fn (Not available in Module)
    self.i=self.qsize()-1
    while self.i>=0:
            print(self.queue[self.i])
            self.i-=1
q=a.LifoQueue()
print("MENU:\n1.Push\n2.Pop\n3.LengthOfStack\n4.Check Stack Emptiness\n5.Display Stack\n6.Peek\n7.EXIT")
ch=int(input("Enter Your Choise=  "))
while ch<=6:
    if (ch==1):
        val=int(input("Enter Element To Be Pushed Into  Stack=  "))
        q.put(val)
        print("Value ",val,"  Pushed")
       
        
    elif (ch==2):
          
          
         
          if q.qsize()==0:
              print("Stack Is Empty, Cannot Pop Element  !!! ")
              
          else:
              print("Popped Element=  ",q.get())
             
          
              
            
    elif (ch==3):
        l=q.qsize()
        print("Number Of Elements In The Stack Are =  ",l)
    elif (ch==4):
         if (q.qsize()==0):
            print("Stack Is Empty")
         else:
            print("Stack Is Not Empty")
           
    elif (ch==5):
       dis(q)
       print("End")
    elif (ch==6):
        print("Peek of The Stack is= ",q.queue[q.qsize()-1])
         
           
    
    
            
            
            
    ch=int(input("Enter Your Next Choise=  "))
print("INVALID INPUT ,Execution Stopped\nYOU HAVE TO RUN AGAIN!!!!!!")

