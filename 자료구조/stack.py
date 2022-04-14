class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node(-1)

    def pop(self):
        """
        스택에서 가장 위에 있는 항목을 제거한다.
        :return:
        """
        current, prev = self.head, None
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def push(self, item):
        """
        item 하나를 스택의 가장 윗 부분에 추가한다.
        :param item:
        :return:
        """
        current = self.head
        while current.next:
            current = current.next
        node = Node(item)
        current.next = node

    def peek(self):
        """
        스택의 가장 위에 있는 항목을 반환한다.
        :return:
        """
        current = self.head
        while current.next:
            current = current.next
        return current.value

    def isEmpty(self):
        """
        스택이 비어 있을 때에 true를 반환한다.
        :return:
        """
        return self.head is None


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
print(stack.peek())
print(stack.isEmpty())
