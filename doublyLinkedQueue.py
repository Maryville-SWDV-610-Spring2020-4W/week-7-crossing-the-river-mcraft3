# doublyLinkedQueue.py

# ------------------------------------------------
"""Provides a doubly linked list queue.

   Provides a First In / First Out FIFO Queue.
   Includes use of a class Node. Elements are
   added at the rear/last of the queue and
   elements are deleted or accessed from the front
   /head of the queue. Provides for the dynamic
   allocation of data to avoid queue overflow
   error issues associated with when the size of
   the queue is restricted and the size of the
   queue exceeds the maximum size, throwing an
   error."""   
#-------------- class Node -----------------------
class Node: 
    
    #--------- Node constructor ------------------
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 
        self.prev = None # Initialize prev as null 
           
#---------------- class Queue --------------------          
# Queue class contains a Node object 
class Queue: 
    """FIFO Queue implementation using a doubly
       linked list for storage."""
   
    #--------- Queue constructor -----------------
    def __init__(self): 
        self.head = None
        self.last=None
           
    #--------- Queue public accessors ------------
    # Function to return head element in the queue  
    def get_first(self): 
   
        return self.head.data 
   
    # Function to return the size of the queue 
    def size(self): 
   
        temp=self.head
        count=0
        if temp == None:
            return 0
        while temp is not None: 
            count=count+1
            temp=temp.next
        return count 
       
    # Function to check if queue is empty or not       
    def is_empty(self): 
   
        if self.head is None: 
            return True
        else: 
            return False
               
    #------------ Queue methods ------------------        
    # Function to add an element data in the Queue 
    def enqueue(self, data): 
        if self.last is None: 
            self.head =Node(data) 
            self.last =self.head 
        else: 
            self.last.next = Node(data) # switch to simultaneous assignment
            self.last.next.prev=self.last 
            self.last = self.last.next
            
    # Function to remove first element and
    # return the element from the queue  
    def dequeue(self): 
   
        if self.head is None: 
            return None
        else: 
            temp= self.head.data 
            self.head = self.head.next
            self.prev=None
            return temp 
   
    # Function to print the queue  
    def print_queue(self): 
           
        print("Players are: ", end='') 
        temp=self.head
        if temp == None:
            print("None")        
        while temp is not None: 
            print(temp.data,end="->") 
            temp=temp.next
       
# ------------------------------------------------
