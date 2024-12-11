book_list = ["Data Structure", "Algorithm", "Web dev"]
sorted(book_list)
print(book_list)
print("**************************")
book_list.index("Algorithm")
book_list.index("Web dev")
print(book_list)
book_list = ['Data Structure',"Data Structure", 'Algorithm', 'Web dev']
print(book_list)
print(book_list.count('Data Structure'))
(book_list.remove('Data Structure'))
print("**************************")
print(book_list)
book_list.sort()
print("**************************")
print(book_list)
del book_list
book_list = ['Algorithm', 'Data Structure', 'Web dev']
print("**************************")
print(book_list)
book_list.clear()
print("**************************")
print(book_list)
book_list = ['Algorithm', 'Data Structure', 'Web dev']
book_list.pop()
print("********gg****************")
print(book_list)
book_list = ['Algorithm', 'Data Structure', 'Web dev']
book_list.pop(1)
print(book_list)
print("**********gg**************")
#list comprehension
prices = [10, 20, 30, 40, 50]
doubled_price = []
for i in prices:
    doubled_price.append(i*2)
print("**************************")
print(doubled_price)
doubled_price = [price * 2 for price in prices]
print("**************************")
print(doubled_price)
names = ["Ajay", "bijay", "sanjay"]
[name.capitalize() for name in names]
numbers = [1, 2, 3, 4, 5]
[num ** 2 for num in numbers]
str1 = "doc1.ppt"
str1.split(".")[-1]
file_name = ["doc1.ppt", "doc2.pdf", "doc3.jpg", "doc4.py"]

[file.split(".")[-1] for file in file_name]
#conditional list comprehension


email_address = ["aj@gmail.com", "sj@yahoo.com", "rj@yahoo.com", "mj@gmail.com"]

[email for email in email_address if email.endswith("@yahoo.com")]
#Nested list comprehension
pairs = []

for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        pairs.append([x, y])
pairs#[[x, y] for x in [1, 2, 3] for y in [4, 5, 6]]
stack_of_plates = []
stack_of_plates.append("plate1")
stack_of_plates.append("plate2")
stack_of_plates.append("plate3")
stack_of_plates.append("plate4")
stack_of_plates
stack_of_plates.pop()
print(stack_of_plates)
browsing_history = []
browsing_history.append("home_page")
browsing_history.append("about us")
browsing_history.append("contact")
browsing_history
browsing_history.pop()
browsing_history
from collections import deque
checkout = deque()
checkout.append("cus1")
checkout.append("cus2")
checkout.append("cus3")
checkout.append("cus4")
checkout
while checkout:
    customer = checkout.popleft()
    print("serving", customer)
from queue import Queue
print_queue = Queue()

print_queue.put("Print job 1")
print_queue.put("Print job 2")
print_queue.put("Print job 3")


while not print_queue.empty():
    print_job = print_queue.get()
    print("printing" ,print_job)
print("**************************")
tuple1=(1,55,2,3,69,87,2)
tuple1.count(1)
tuple1.count(2)
tuple1.index(2)
#tuple1.index('azad')
print("**************************")
print(tuple1 * 2)
print(tuple1[0:4])
print(tuple1[::-1])
print(tuple1[-1])
set=[(i+1)**2 for i in range (10)]
print(set)