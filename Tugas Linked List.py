class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node("Izal")
n2 = Node("Azmi")
n3 = Node("Ojak")

n1.next = n2
n2.next = n3

head = n1
while head:
    print(head.data, end=" -> ")
    head = head.next
print("None")