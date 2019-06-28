class DoubleLL:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return f'(The node data is: {self.data})'

    def get_data(self):
        """ Return the current value of the data i.e self.data"""
        return self.data

    def set_data(self, new_data):
        """set the data of the node to the passed data in the element new_data"""
        self.data = new_data

    def get_next(self):
        """Return the value of the next node in the instance self.next"""
        return self.next

    def get_prev(self):
        """Return the value of the previous node in the instance self.previous"""

        return self.previous

    def set_previous(self, new_prev):
        """Return the value of the previous node in the instance self.next"""

        self.previous = new_prev

    def set_next(self, new_next):
        """Return the value of the next node in the instance self.next"""
        self.next = new_next


class dll:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return f'The node data of head is: {self.head}'

    def is_empty(self):
        return self.head is None

    def size(self):
        size = 0

        if self.head is None:
            return 'LL is empty'

        current = self.head

        while current != None:
            size += 1
            current = current.get_next()

        return size

    def search(self, data):

        if self.head is None:
            return 'There\'s nothing to search in LL as it\'s empty'

        current = self.head

        while current is not None:

            if current.get_data() == data:
                return f'The data found is matched with : {data}'

            else:
                current = current.get_next()

        return f'The key {data} is not found in LL'

    def add_front(self, new_head):
        temp = DoubleLL(new_head)
        temp.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(temp)
        self.head = temp

    def remove(self, data):
        if self.head is None:
            return 'The LL is empty to remove'

        current = self.head
        found = False

        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return 'Data to remove is not found in LL'
                else:
                    current = current.get_next()


        if current.previous is None:
            self.head = current.get_next()
            # current.set_previous = None as it is already set to None while instantiating
        elif self.size() is 1: # while removing the last element
            print('LinkedList has only one element')

        else:
            current.previous.set_next(current.get_next())  # setting the next of the previous node
            current.next.set_previous(current.get_prev())  # setting the previous of the next node





node1 = dll()
print(node1.size())
node1.add_front('Ankit')
node1.add_front('Sigroha')
node1.add_front('Sunny')
print(node1.size())

print(node1.head)
print(node1.remove('sigroha'))
print(node1.remove('Sigroha'))
print(node1.size())
print(node1.remove('Sunny'))
print(node1.head)

node1.add_front('Sigroha')
node1.add_front('Sunny')
node1.add_front('Champ')

print(node1.remove('Sunny'))
print(node1.remove('Sigroha'))
print(node1.remove('Champ'))
print(node1.size())
print(node1.head)
node1.remove('Ankit')