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

node1= SimpleLL("ankit")
print(node1.get_data())
node1.set_data('sigroha')
node1.get_data()
node2= SimpleLL('node2')
node1.set_next(node2)
node1.get_next()

#print(node1.get_data())
print(node1.get_next())
#print(node2.get_data())



