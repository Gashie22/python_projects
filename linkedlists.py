from collections import deque
#Linked lists emplementatio using a module

class Node :
    def __init__(self,data):
        self.data=data
        self.next= None
        self.prev=None
class Link :
    def __init__(self):
        self.head=None

    def push (self,newval): #this function allows us to add an element to the head of the linked list
        new_node=Node(newval) #create a variable which stores the Node with that new value
        new_node.next=self.head #allows the execution of other elements not inside this function
        self.head=new_node #making the new node the head

    def show (self):
        node=self.head #first node will bw the head
        while node is not None:
            print(node.data)
            node=node.next #assigning the node to the next node

linked_list=Link()
element1=Node('Monday')
linked_list.head=element1 #linking t point to the next element(element 1 now the haed)
element2=Node('Wednesday')
element3=Node('Tuesday')
el4=Node('Thursday')
linked_list.head.next=element3 #(assigning element3 to be the 2nd element)
element3.next=element2 #(linking element 2 to follow elemnt 3)
element2.next=el4
linked_list.push("Friday")
linked_list.show()
