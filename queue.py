#Implementation of Queue

front = 0
rear = 0
mymax = 3
# Function to create a stack. It initializes size of stack as 0
def createQueue():
 queue = []
 return queue
# Stack is empty when stack size is 0
def isEmpty(queue):
 return len(queue) == 0
# Function to add an item to stack. It increases size by 1
def enqueue(queue,item):
 queue.append(item)
# Function to remove an item from stack. It decreases size by 1
def dequeue(queue):
 if (isEmpty(queue)):
 return "Queue is empty"
 item=queue[0]
 del queue[0]
 return item
 # Driver program to test above functions
queue = createQueue()
while True:
 print("1 Enqueue")
 print("2 Dequeue")
 print("3 Display")
 print("4 Quit")
47
 ch=int(input("Enter choice"))
 if(ch==1):
 if(rear < mymax):
 item=input("enter item")
 enqueue(queue, item)
 rear = rear + 1
 else:
 print("Queue is full")
 elif(ch==2):
 print(dequeue(queue))
 elif(ch==3):
 print(queue)
 else:
 break
