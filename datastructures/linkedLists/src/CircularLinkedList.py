                                 
"""Linked List"""
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    '''def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail'''
    
    def add(self,data):
        new_node=Node(data)
        if self.__head==None:
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
        
    
    def display(self):
        temp=self.__head
        while temp is not None:
            print(temp.get_data())
            temp=temp.get_next()
    
    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            else:
                temp=temp.get_next()
        return temp
        
    def delete(self,data):
        node=self.find_node(data)
        if node is None:
            print("Node not found!!!")
        else:
            if node == self.__head:
                self.__head=node.get_next()
            else:
                temp=self.__head
                while temp.get_next() != node:
                    temp=temp.get_next()
                temp.set_next(node.get_next())
                if node.get_next is None:
                    self.__tail=node
    
    def insert(self,data,data_before):
        if self.find_node(data_before) is None:
            print(data_before,"not found!!")
            return
        new_node=Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head=new_node
        else:
            temp=self.__head
            while temp.get_data()!= data_before:
                temp=temp.get_next()
            new_node.set_next(temp.get_next())
            temp.set_next(new_node)
            if new_node.get_next()==None:
                self.__tail=new_node
    
    def count_nodes(self):
        count=0
        temp=self.__head
        while(temp is not None):
            count+=1
            temp=temp.get_next()
        return count
                
    def insert_atPos(self,data,pos):
        if pos<0:
            print("Enter a position starting from 0")
            return
        if pos>self.count_nodes():
            print("Position outside range of list")
            return
        new_node=Node(data)
        if pos==0:
            new_node.set_next(self.__head)
            self.__head=new_node
        else:
            temp=self.__head
            for i in range(pos,1,-1):
                temp=temp.get_next()
            new_node.set_next(temp.get_next())
            temp.set_next(new_node)
            if new_node.get_next()==None:
                self.__tail=new_node

list1=LinkedList()
#Add all the required element(s)
list1.add("Kit Kat")
list1.add("Gems")
list1.add("Dairy Milk")
list1.add("Five Star")
list1.add("Snickers")
#Search for the required node
node=list1.find_node("Five Star")
#node=list1.find_node("Bar One")
if(node!=None):
    print("Node found")
else:
    print("Node not found") 
list1.delete("Snickers")
#list1.insert("Dark chocolate","Five Star")
#list1.insert("Dark chocolate",None)
#list1.insert("Dark chocolate","Marbles")
#list1.insert("Dark chocolate","Gems")
list1.insert_atPos("Dark chocolate",4)
list1.display()
