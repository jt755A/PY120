'''
Always removing oldest value
- could just make a list of length buffer_size
- get pops the item at index 0

- calling get on empty buffer = None

- calling put when buffer is full replaces 
    - so pop the first element
'''

class CircularBuffer:
    state = []

    def __init__(self, buffer_size):
        self.buffer_size = buffer_size

    def put(self, item):
        if len(CircularBuffer.state) < self.buffer_size:
            CircularBuffer.state.append(item)
        else:
            CircularBuffer.state.pop(0)
            CircularBuffer.state.append(item)



    
    def get(self):
        if CircularBuffer.state:
            oldest_value = CircularBuffer.state.pop(0)
            return oldest_value
        
        elif not CircularBuffer.state:
            return None


buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True