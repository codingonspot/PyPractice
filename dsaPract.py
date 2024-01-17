# Time Complexity

# O(n)
# def get_sqrt_nos(num):
#     sqrt_no = []
#     for n in num:
#         sqrt_no.append(n*n)
#     return sqrt_no
#
#
# num = [2, 5, 8, 9]
# res = get_sqrt_nos(num)
# print(res)

# O(1)
# def find_first_pe(prices, eps, index):
#     pe = prices[index]/ eps[index]
#     return pe

# O(n^2)
# num = [3, 6, 2, 4, 3, 6, 8, 9]
# for i in range(len(num)):
#     for j in range(i+1, len(num)):
#         if num[i] == num[j]:
#             print(str(num[i]) + " is a duplicate.")
#             break

# time = an^2 + an + b --> O(n^2)
# num = [3, 6, 2, 4, 3, 6, 8, 9]
# dup = None
# for i in range(len(num)):
#     for j in range(i+1, len(num)):  # n^2 iterations
#         if num[i] == num[j]:
#             dup = num[i]
#             break
# for i in range(len(num)):            # n iterations
#     if num[i] == dup:
#         print(i)

#  Binary Search --> O(log n)
# --------------------------------------------------------

# ARRAYS
# Arr can store numbers, text or complex objects
# 2D Array
# stock_prices = [[2, 3, 5, 6],
#                 [40, 42, 38, 44],
#                 [78, 89, 71, 66]
#                 ]
# stock_prices = [298, 305, 320, 301, 292]
# Traversal = O(n)
# for price in stock_prices:
#     print(price)

# Search by Value = O(n)
# for i in range(len(stock_prices)):
#     if stock_prices[i] == 301:
#         print(i)

# Search by Index = O(1)
# print(stock_prices[2])
# stock_prices.insert(1, 284)
# stock_prices.remove(1)

# Insert & Delete = O(n)

# EXERCISE
# Q1

# e = [2200, 2350, 2600, 2130, 2190]
# febExp = e[1]-e[0]
# print("In Feb, dollars spent extra compare to January is: $" + str(febExp))
#
# totExp = e[0]+e[1]+e[2]
# print("total expense in first quarter (first three months) of the year is: $" + str(totExp))
#
# for i in range(len(e)):
#     if e[i] == 2000:
#         print("Y")
# print("N")
#
# e.append(1980)
# print(e)
#
# e[3] = e[3] - 200
# print(e)

# Q2

# hero = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
# print(len(hero))
# hero.append("black panther")
# print(hero)
# hero.remove("black panther")
# print(hero)
# hero.insert(3, "black panther")
# print(hero)
# hero[1:3] = ["doctor strange"]
# print(hero)
# hero.sort()
# print(hero)

# Q3

# num = int(input())
# odd_no = []
# for i in range(1, num+1):
#     if i % 2 == 1:
#         odd_no.append(i)
# print(odd_no)

# LINKED LIST

# Insert/ Delete Element at beg = O(1)
# Insert/ Delete Element at end = O(n)
# Traversal = O(n)
# Accessing Element by value = O(n)

# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert_at_beg(self, data):
#         node = Node(data, self.head)
#         self.head = node
#
#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data, None)
#
#     def insert_val(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)
#
#     def insert_after_val(self, data_after, data_to_insert):
#         if self.head is None:
#             return
#         if self.head.data == data_after:
#             self.head.next = Node(data_to_insert, self.head.next)
#             return
#         itr = self.head
#         while itr:
#             if itr.data == data_after:
#                 itr.next = Node(data_to_insert, itr.next)
#                 break
#
#             itr = itr.next
#
#     def remove_by_value(self, data):
#         if self.head is None:
#             return
#
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#
#         itr = self.head
#         while itr.next:
#             if itr.next.data == data:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
#
#     def remove_at(self, index):
#         if index < 0 or index >= self.get_len():
#             raise Exception("Invalid index")
#         if index == 0:
#             self.head = self.head.next
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
#             count += 1
#
#     def insert_at(self, index, data):
#         if index < 0 or index > self.get_len():
#             raise Exception("Invalid index")
#         if index == 0:
#             self.insert_at_beg(data)
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break
#             itr = itr.next
#             count += 1
#
#     def get_len(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count += 1
#             itr = itr.next
#         return count
#
#     def print(self):
#         if self.head is None:
#             print("Linked List is empty.")
#             return
#         itr = self.head
#         ll_str = ''
#
#         while itr:
#             ll_str += str(itr.data) + "-->"
#             itr = itr.next
#
#         print(ll_str)
#
#
# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_at_beg(5)
#     ll.insert_at_beg(10)
#     ll.remove_at(2)
#     ll.remove_at(5)
#     ll.insert_val(["A", "B", "C", "D", "E"])
#     ll.insert_at_end("Y")
#     ll.insert_at(5, "Z")
#     ll.insert_after_val("A", "O")
#     ll.remove_by_value("D")
#
#     ll.print()
#     print("Length:", ll.get_len())

# HASH TABLE
# Look up by Key is O(n) on avg
# Insertion/ Deletion is O(n) on avg

# stock_prices = {}   # Dictionary || [] --> List
# with open("stock_priceDSA.csv", "r") as f:
#     for line in f:
#         tokens = line.split(',')
#         day = tokens[0]
#         price = float(tokens[1])
#         stock_prices[day] = price

# for element in stock_prices:   # --> O(n) For List operation
#     if element[0] == "09-Mar":
#         print(element[1])

# print(stock_prices["09-Mar"])   # --> O(1) For Dictionary operation
# print(stock_prices)

# def get_hash(key):
#     h = 0
#     for char in key:
#         h += ord(char)
#     return h % 100
#
#
# print(get_hash('Ishan'))

# class HashTable:
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [[] for i in range(self.MAX)]
#
#     def get_hash(self, key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.MAX
#
#     def __setitem__(self, key, val):
#         found = False
#         h = self.get_hash(key)
#         for idx, element in enumerate(self.arr[h]):
#             if len(element) == 2 and element[0] == key:
#                 self.arr[h][idx] = (key, val)
#                 found = True
#                 break
#         if not found:
#             self.arr[h].append((key, val))
#         # self.arr[h] = value
#
#     def __getitem__(self, key):
#         h = self.get_hash(key)
#         for element in self.arr[h]:
#             if element[0] == key:
#                 return element[1]
#
#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         for index, element in enumerate(self.arr[h]):
#             if element[0] == key:
#                 del self.arr[h][index]


# t = HashTable()
# print(t.get_hash('and'))
# print(t.get_hash('march 4'))
# t['march 4'] = 120
# t['march 4'] = 78
# t['march 8'] = 67
# t['march 9'] = 4
# t['and'] = 459
# print(t['and'])
# del t['and']
# print(t.arr)
# print(t.arr)

# EXERCISE
# Q1

# arr = []
# with open("nyc_weatherDSA.csv", "r") as f:
#     for line in f:
#         tokens = line.split(',')
#         try:
#             temperature = int(tokens[1])
#             arr.append(temperature)
#         except:
#             print("Invalid temperature. Ignore the row")
#
# # print(arr)
# avg = float(sum(arr[0:7])/len(arr[0:7]))
# print(avg)
# print(max(arr[0:10]))

# Q2

# w_dict = {}
# with open("nyc_weatherDSA.csv", "r") as f:
#     for line in f:
#         tokens = line.split(',')
#         day = tokens[0]
#         try:
#             temperature = int(tokens[1])
#             w_dict[day] = temperature
#         except:
#             print("Invalid temperature. Ignore the row")

# print(w_dict)
# sum = 0
# count = 0
# for ele in w_dict.values():
#     if count == 7:
#         break
#     sum += ele
#     count += 1
# # print(sum)
#
# print(float(sum/7))

# print(sum(w_dict.values())/len(w_dict))
# print(w_dict["09-Jan"])
# print(w_dict["04-Jan"])

# Q3

# word_count = {}
# with open("poem.txt", "r") as f:
#     for line in f:
#         tokens = line.split(' ')
#         for token in tokens:
#             token = token.replace('\n', '')
#             if token in word_count:
#                 word_count[token] += 1
#             else:
#                 word_count[token] = 1
# print(word_count)

# STACK
# Push/Pop element = O(1)
# Search element by value = O(n)

# from collections import deque
# stack = deque()
# print(dir(stack))
# stack.append(5)
# stack.append(4)
# stack.append(3)
# stack.append(2)
# stack.append(1)
# stack.pop()
# print(stack)
# class Stack:
#     def __init__(self):
#         self.container = deque()
#
#     def push(self, val):
#         self.container.append(val)
#
#     def pop(self):
#         return self.container.pop()
#
#     def peek(self):
#         return self.container[-1]
#
#     def is_empty(self):
#         return len(self.container) == 0
#
#     def size(self):
#         return len(self.container)
# s = Stack()
# s.push(5)
# s.pop()
# print(s)
# print(s.is_empty())

# Q1

# def reverse_string(s):
#     st = Stack()
#
#     for ch in s:
#         st.push(ch)
#
#     rstr = ''
#     while st.size() != 0:
#         rstr += st.pop()
#     return rstr

# Q2

# def is_match(ch1, ch2):
#     match_dict = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }
#     return match_dict[ch1] == ch2
# def is_balanced(s):
#     st = Stack()
#     for ch in s:
#         if ch == '(' or ch == '{' or ch == '[':
#             st.push(ch)
#         if ch == ')' or ch == '}' or ch == ']':
#             if st.size() == 0:
#                 return False
#             if not is_match(ch, st.pop()):
#                 return False
#     return st.size() == 0
# if __name__ == '__main__':
#     print(reverse_string("We will conquer COVID-19"))
#     print(reverse_string("Ishan Singh"))
#     print(is_balanced("({a+b})"))
#     print(is_balanced("))((a+b}{"))
#     print(is_balanced("((a+b))"))
#     print(is_balanced("((a+g))"))
#     print(is_balanced("))"))
#     print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

# Queue

# Queue as a List
# q = []
# q.insert(0, 1)
# q.insert(0, 2)
# q.insert(0, 3)
# print(q)
# q.pop()
# print(q)

# Queue as collections.deque ( double ended queue)
# Avg access and search = O(n)
# Avg insert/ delete = O(1)

# from collections import deque
# class Queue:
#     def __init__(self):
#         self.buffer = deque()
#
#     def enqueue(self, val):
#         self.buffer.appendleft(val)
#
#     def dequeue(self):
#         self.buffer.pop()
#
#     def is_empty(self):
#         return len(self.buffer) == 0
#
#     def size(self):
#         return len(self.buffer)
# pq = Queue()
# pq .enqueue({
#     'company': 'Fly Singh',
#     'timestamp': '28 Jun, 11:01 AM',
#     'price': 181.23
# })
# pq .enqueue({
#     'company': 'Fly Singh',
#     'timestamp': '28 Jun, 11:02 AM',
#     'price': 181.09
# })
# pq .enqueue({
#     'company': 'Fly Singh',
#     'timestamp': '28 Jun, 11:03 AM',
#     'price': 182.01
# })
# pq.dequeue()
# print(pq.buffer)
# print(pq.size())
# queue = deque()
# queue.appendleft(1)
# queue.appendleft(2)
# queue.appendleft(3)
# print(queue)
# queue.pop()
# print(queue)
# import threading
# import time
# from collections import deque
#
#
# class Queue:
#     def __init__(self):
#         self.buffer = deque()
#
#     def enqueue(self, val):
#         self.buffer.appendleft(val)
#
#     def dequeue(self):
#         if len(self.buffer) == 0:
#             print("Queue is empty")
#             return
#         return self.buffer.pop()
#
#     def is_empty(self):
#         return len(self.buffer) == 0
#
#     def size(self):
#         return len(self.buffer)
#
#     def front(self):
#         return self.buffer[-1]
#
#
# food_order_queue = Queue()
#
#
# def produce_binary_numbers(n):
#     numbers_queue = Queue()
#     numbers_queue.enqueue("1")
#
#     for i in range(n):
#         front = numbers_queue.front()
#         print("   ", front)
#         numbers_queue.enqueue(front + "0")
#         numbers_queue.enqueue(front + "1")
#
#         numbers_queue.dequeue()


# def place_orders(orders):
#     for order in orders:
#         print("Placing order for:", order)
#         food_order_queue.enqueue(order)
#         time.sleep(0.5)
#
#
# def serve_orders():
#     time.sleep(1)
#     while True:
#         order = food_order_queue.dequeue()
#         print("Now Serving: ", order)
#         time.sleep(2)


# if __name__ == '__main__':
#     # orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
#     # t1 = threading.Thread(target=place_orders, args=(orders, ))
#     # t2 = threading.Thread(target=serve_orders)
#     #
#     # t1.start()
#     # t2.start()
#     produce_binary_numbers(10)

# Tree

# class TreeNode:
#     def __init__(self, data):   # name, # designation
#         self.data = data
#         # self.designation = designation
#         self.children = []
#         self.parent = None
#
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#         return level
#
#     def print_tree(self, level):    # property_name
#         if self.get_level() > level:
#             return
#         if property_name == "both":
#             value = self.name + "(" + self.designation + ")"
#         elif property_name == "name":
#             value = self.name
#         else:
#             value = self.designation
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree(level)
#
#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
#
#
# def build_location_tree():
#     root = TreeNode("Global")
#
#     india = TreeNode("India")
#
#     gujarat = TreeNode("Gujarat")
#     gujarat.add_child(TreeNode("Ahmedabad"))
#     gujarat.add_child(TreeNode("Baroda"))
#
#     karnataka = TreeNode("Karnataka")
#     karnataka.add_child(TreeNode("Bangluru"))
#     karnataka.add_child(TreeNode("Mysore"))
#
#     india.add_child(gujarat)
#     india.add_child(karnataka)
#
#     usa = TreeNode("USA")
#
#     nj = TreeNode("New Jersey")
#     nj.add_child(TreeNode("Princeton"))
#     nj.add_child(TreeNode("Trenton"))
#
#     california = TreeNode("California")
#     california.add_child(TreeNode("San Francisco"))
#     california.add_child(TreeNode("Mountain View"))
#     california.add_child(TreeNode("Palo Alto"))
#
#     usa.add_child(nj)
#     usa.add_child(california)
#
#     root.add_child(india)
#     root.add_child(usa)
#
#     return root
#     CTO Hierarchy
#     infra_head = TreeNode("Vishwa", "Infrastructure Head")
#     infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
#     infra_head.add_child(TreeNode("Abhijit", "App Manager"))
#
#     cto = TreeNode("Chinmay", "CTO")
#     cto.add_child(infra_head)
#     cto.add_child(TreeNode("Aamir", "Application Head"))
#
#     # HR hierarchy
#     hr_head = TreeNode("Gels", "HR Head")
#
#     hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
#     hr_head.add_child(TreeNode("Waqas", "Policy Manager"))
#
#     ceo = TreeNode("Nilupul", "CEO")
#     ceo.add_child(cto)
#     ceo.add_child(hr_head)
#
#     return ceo
#     root = TreeNode("Electronics")
#     laptop = TreeNode("Laptop")
#     laptop.add_child(TreeNode("Mac"))
#     laptop.add_child(TreeNode("HP"))
#     laptop.add_child(TreeNode("Dell"))
#
#     cellphone = TreeNode("Cell Phone")
#     cellphone.add_child(TreeNode("iPhone"))
#     cellphone.add_child(TreeNode("RealMe"))
#     cellphone.add_child(TreeNode("Google Pixel"))
#
#     tv = TreeNode("TV")
#     tv.add_child(TreeNode("Samsung"))
#     tv.add_child(TreeNode("LG"))
#
#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)
#
#     return root


# if __name__ == '__main__':
#     r = build_location_tree()
#     r.print_tree(3)
#     pass

# Binary Search Tree (BST)
# Search complexity = O(log n)
# Insertion = O(log n)
# BFS and DFS (In lRr/Pre Rlr/Post Order lrR)

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    # numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    numbers = [15, 12, 7, 14, 27, 20, 23, 88]

    numbers_tree = build_tree(numbers)
    print("Input numbers:", numbers)
    print("Min:", numbers_tree.find_min())
    print("Max:", numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
