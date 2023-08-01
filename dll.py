class DLLNode(object):
    """Node for Doubly Linked List"""

    def __init__(self, val:int) -> None:
        self.val = val
        self.prev = None
        self.next = None
    
class DLL(object):
    """Doubly Linked List"""

    def __init__(self, val:int=-1) -> None:
        """head always points to a dummy node initialized with value -1"""
        self.head = DLLNode(val)
        self.tail = self.head
    
    def insert_front(self, val:int)-> None:
        """Insert node at the front """
        node = DLLNode(val)

        #Store previous first node
        #this will become the second node
        prev_node = self.head.next

        #Link node after head
        self.head.next = node
        node.prev = self.head

        #Link previous first node after new node
        #to make it the second node
        node.next = prev_node

        #If previous first node is not the tail
        if prev_node:
            prev_node.prev = node 
        else: #update the tail
            self.tail = node
            
    def insert_rear(self, val:int) -> None:
        """Insert node at the end"""
        node = DLLNode(val)

        #Link node after tail
        self.tail.next = node
        node.prev = self.tail

        #Update tail
        self.tail = node
    
    def _search(self, val:int)-> DLLNode:
        """Search for a node with value"""
        node = self.head

        #Traverse until value is found or end of list
        while node and node.val != val:
            node = node.next
        
        return node
    
    def insert_after(self, val:int, new:int):
        """Insert new node after node with val"""
        node = self._search(val)
        if not node:
            print("Value not found in DLL.")
            return
        
        new_node = DLLNode(new)

        #Store previous node.next to be linked after new_node
        node_next = node.next

        #Link new node after node with val
        node.next = new_node
        new_node.prev = node

        #If new node is not the last node, link
        #previous next node with new node.
        if node_next:
            new_node.next = node_next
            node_next.prev = new_node
        else: #update tail
            self.tail = new_node
    
    def _is_empty(self):
        """Return if the list empty"""
        return self.head == self.tail
    
    def delete_front(self) -> int:
        """Delete first node of the list"""

        #If list is empty
        if self._is_empty():
            print("No elements present in the list.")
            return -1
        
        #head always points to a dummy node.
        #So, node to be deleted is head.next

        #Store value of node before deletion.
        val = self.head.next.val

        #head points to next node.
        self.head = self.head.next
        self.head.prev = None

        #Update value of head to make it dummy.
        self.head.val = -1
        return val

    def delete_rear(self) -> int:
        """Delete last node of the list"""

        #If list is empty, return
        if self._is_empty():
            return -1

        #Store value of node before deletion
        val = self.tail.val

        #Update tail to point to the second to last node.
        self.tail = self.tail.prev
        self.tail.next = None
        return val

    def delete(self, val:int):
        """Delete first node with given value"""
        node = self._search(val)
        if not node:
            print("Value not found in DLL.")
            return

        #Store prev and next nodes of node to be deleted
        node_prev, node_next = node.prev, node.next

        #Update pointers to skip nodes.
        node_prev.next = node_next

        #If node being deleted is not the last node.
        if node_next:
            node_next.prev = node_prev
        else: #update tail if node is last node
            self.tail = node_prev
        
        return

    def print(self) -> None:
        """Print list values from head to tail"""

        node = self.head.next
        print("### Head to tail ###")
        while node:
            print(node.val)
            node = node.next

if __name__ == '__main__':
    dll = DLL()

    for val in range(1,5):
        dll.insert_front(val)
    
    print("List after inserting values in the front")
    dll.print()

    for val in range(10,5,-1):
        dll.insert_rear(val)
    
    print("List after inserting values in the rear")
    dll.print()

    dll.insert_after(1, 0)
    print("List after inserting value after a node")
    dll.print()

    for i in range(2):
        print("Deleting ", dll.delete_front())
    print("List after deleting 2 elements from the front.")
    dll.print()

    for i in range(2):
        print("Deleting ", dll.delete_rear())
    print("List after deleting 2 elements from the rear.")
    dll.print()

    dll.delete(0)
    print("List after deleting a node with value 0.")
    dll.print()

    for i in range(5):
        print("Deleting ", dll.delete_front())
    print("List after deleting remaining nodes from the list")
    dll.print()
   
    print("Output after deleting from an empty list:")
    print("Deleting ", dll.delete_front())
   
    
