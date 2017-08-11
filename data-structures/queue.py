class coolQueue(object):
    """a basic queue data structure"""
    items = []

    # default overrides
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    # queue functions
    def size(self):
        """return the size of the queue"""
        return len(self.items)

    def push(self, newItem):
        """push an item into the queue"""
        self.items.append(newItem)

    def pop(self):
        """remove and return the first item"""
        i = self.items.pop(0)
        return i

    def empty(self):
        """return true if queue is empty"""
        return self.size() == 0

    def front(self):
        """preview the front of the queue"""
        if self.size() > 0:
            return self.items[0]
        else:
            return None

    def back(self):
        """preview the back of the queue"""
        if self.size() > 0:
            return self.items[-1]
        else:
            return None
