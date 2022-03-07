class Node:
    def __init__(self, value= None, nextnode=None,prev_elem=None):
        self.value = value
        self.nextnode = nextnode
        self.prev_elem = prev_elem
        

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.amount = 0

    def add_head(self, val):
        tmp = Node(val)
        tmp.nextnode = self.head
        if  self.head is not None:
            self.head.prev_elem = tmp
        if self.amount == 0 :
            self.head = self.tail = tmp
        else:
            self.head = tmp
        self.amount += 1
    
    
    def add_tail(self, val):
        tmp = Node(val)
        tmp.prev_elem = self.tail
        if self.tail is not None:
            self.tail.nextnode = tmp

        if self.amount == 0 :
            self.head = self.tail = tmp
        else:
            self.tail = tmp
        self.amount += 1
        


    def insert_elem(self,val, ind):
        if ind == self.amount:
            self.add_tail(val)
        if ind == 0 :
            self.add_head(val)
            return
        i = 0 
        ins = self.head
        while i <ind:
            ins = ins.nextnode
            i +=1
        prev_ins = ins.prev_elem
        tmp = Node(val)
        if prev_ins is not None and self.amount != 0 :
            prev_ins.nextnode = tmp
        tmp.nextnode = ins
        tmp.prev_elem = prev_ins
        ins.prev_elem = tmp 
        self.amount += 1
        


    
     
    def get_elem(self, ind):
        tmp = self.head
        i = 0
        while i < ind and tmp is not None:
            tmp = tmp.nextnode
            i += 1
        if tmp != None:
            return tmp
              
    
    
    def del_elem(self):
        pass
    
    
    def get_count(self):
        return self.amount
    
    def print_elem(self, ind):
        tmp = self.get_elem(ind)
        print(tmp.value)

    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value, end=" ")
            tmp = tmp.nextnode
        print()
    


    def check_elem(self, number):
        tmp = self.head
        i = 0 
        while i < self.amount and tmp is not None:
            if number == tmp.value:
                return True
            tmp = tmp.nextnode
        return False
            





l = LinkedList()
l.add_head(5)
l.add_head(8)
l.add_head(2)
l.add_tail(3)

print(l.get_count())
print(l.get_elem(3))
print(l.check_elem(8))
print(l.print_elem(2))
print(l.insert_elem(10,2))

l.print_list()
