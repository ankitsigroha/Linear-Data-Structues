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


node1 = dll("ankit")
print(node1.get_data())
node1.set_data('node1')
print(node1.get_data())
node2 = dll('node2')
node1.set_next(node2)
print(node1.get_next())

node3 = dll('node3')
node1.set_previous(node3)
print(node1.get_prev())

node3.set_previous(node2)
print(node3.get_prev())

node2.set_previous(node1)
print(node2.get_prev())

print(node1.get_data())
print(node2.get_data())
print(node3.get_data())