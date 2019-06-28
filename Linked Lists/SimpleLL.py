class SimpleLL:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'(SimpleLL node data is: {self.data})'

    def get_data(self):

        """ Return the current value of the data i.e self.data"""
        return self.data

    def set_data(self, new_data):
        """set the data of the node to the passed data in the element new_data"""
        self.data = new_data

    def get_next(self):
        """Return the value of the next node in the instance self.next"""
        return self.next

    def set_next(self, new_next):
        """Sets the value of next node"""
        self.next = new_next


class ssl:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return f'the data of the node is: {self.head}'

    def is_empty(self):
        if self.head is None:
            return 'Linked list is empty'
        else:
            return f'Linked list have this element on head{self.head}'

    def add_front(self, new_head):
        temp = SimpleLL(new_head) #add a new node in front
        temp.set_next(self.head) #setting the next of newly added node
        self.head = temp #assigning the new value to head

    def size(self):

        """returns an interger value of the number of nodes in a linked list

        time complexity is O(n)


        """
        size = 0

        if self.head == None: # LL is empty
            return 'LinkedList head is none'

        current = self.head  #to iterate through the LL

        while current != None: #till the end of LL
            size += 1
            current = current.get_next() #to move to next node

        return size


    def search(self, data):
        
        if self.head is None:
            return 'LL is empty to search'

        current = self.head

        while current is not None:

            if current.get_data() == data: # or if current.get_data() == key:
                return f'The value found matches the data {data}'

            else:
                current = current.get_next()
        
        return 'Key not found'


    def remove(self, data):
        if self.head is None:
            return 'LL is empty so nothing to remove'

        current = self.head
        previous = None
        found = False

        while not found: #loop to find the data on head as well as until the end of the LL. 
                        #If not found on head then the traversal moves forward by setting previous to current and moving current to next.
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return 'The data to remove is not found'

                else:
                    previous = current
                    current = current.get_next()
        # by now we've found the node to remove
        if previous is None: #if found data to remove is on head
            self.head = current.get_next()

        else:
            previous.set_next(current.get_next()) #setting the in-between nodes to point to next

#creating ssl class instance
node1 = ssl()

print(node1.remove(12))

print(node1.is_empty())
print(node1.size())

#assigning value to class instance of ssl
node2 = SimpleLL(69)
node1.head = node2
print(node1.is_empty())
print(node1.head)

#checking functions of ssl class
(node1.add_front('Ankit Sigroha'))
print(node1.head)
print(node1.size())

(node1.add_front('Sunny'))
(node1.add_front('is'))
(node1.add_front('Champ'))
print(node1.size())

print(node1.search('Sunny'))
print(node1.search('Himanshu'))

print(node1.remove('Cat'))
print(node1.size())
(node1.remove('is'))

print(node1.size())
print(node1.search('is'))
print(node1.head)














