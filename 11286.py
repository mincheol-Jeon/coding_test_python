from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline

N = int(input())
MyQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if MyQueue.empty():
            print('0\n')
        else:
            temp = MyQueue.get()
            print(str(temp[1])+'\n')
    else:
        MyQueue.put((abs(request),request))