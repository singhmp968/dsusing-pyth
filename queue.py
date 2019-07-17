class queue:
    def __init__(self,size=0):
        self.size=size
        self.list1=[]
    def add(self,data):
        if len(self.list1)>=self.size:
            
            print("stack is full")
            return 
        self.list1.append(data)
    def remove(self,data):
        
        if len(self.list1)==0:
            
            print("stack is empty")
            return
        self.list1.pop(0)
        return data
    def printqueue(self):
        for i in self.list1:
            print(i)
            
'''obj=stack(5)
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
print(obj.list1)
obj.remove()
print(obj.list1)'''
obj=queue(4)
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.printqueue()
