'''
put: adds an item to empty space: AFTER most recently added space
    - only works if space in object is None

get: removes + returns oldest object in buffer UNLESS whole buffer empty
    = return None

- None represents empty spots in buffer

Rules
Argument passed in: int
    - Create a buffer with arg spots, filled with none



Need to keep track:
- oldest position in buffer
    - This increments in a circular loop, whenever an object is removed.
        - 1 -> 2 -> 3 - > 1 ...
- most recently added item
    - increments in a similar way to oldest....
        - since newest item always added after MOST RECENT new item

Put function
- requires a value argument to pass in
- if buffer empty, add at 1st space
- otherwise, increment position, add value here
    - adds value to NEXT position
    - adds 1 to current_buffer position

- IF BUFFER FULL: REPLACES item that's been there longest

get
    - return None, if buffer empty
    else:
    - go to oldeest_position
        - grab value
        -  REASSIGN? current space to None
        - return value
'''

class CircularBuffer:

    def __init__(self, size):
        self.size = size
        self._buffer = [None] * size
        # self.create_buffer(size)
        self.oldest_idx = 0
        self.newest_idx = 0

    # def create_buffer(self, size):
    #     buffer = [None for _ in range(size)]
    #     self._buffer = buffer

    def get(self):
        if self._is_empty():
            return None

        oldest = self.oldest_idx
        removed_item = self._buffer[oldest]
        self._replace_space(oldest)
        self.oldest_idx = self._increment(oldest)
        return removed_item


    def put(self, item):
        newest = self.newest_idx
        if self._is_full():
            # If buffer is full before replacement, increment oldest idx
            self.oldest_idx = self._increment(self.oldest_idx)


        self._buffer[newest] = item
        self.newest_idx = self._increment(newest)



    def _is_empty(self):
        return all([space == None for space in self._buffer])

    def _is_full(self):
        return all([space != None for space in self._buffer])

    def _increment(self, position):
        # increments oldest/newest variable, going back to beginning
        # if end of buffer reached
        next_position = position + 1
        next_position %= self.size
        # if next_position >= self.size:
        #     next_position -= self.size

        return next_position

    def _replace_space(self, idx):
        self._buffer[idx] = None


buffer = CircularBuffer(3)

# print(buffer._buffer)
# print(buffer._is_empty())

print(buffer.get() is None)          # True

buffer.put(1)
# print(buffer._buffer)

buffer.put(2)

# print(buffer._buffer)
print(buffer.get() == 1)             # True

buffer.put(3)

# print(buffer._buffer)
# print(f'Full: {buffer._is_full()}')

buffer.put(4)
print(buffer.get() == 2)             # True

print(buffer._buffer)


buffer.put(5)
print(buffer._buffer)
print(f'Full: {buffer._is_full()}')


buffer.put(6)
print(buffer._buffer)


buffer.put(7)

print(buffer._buffer)
print(buffer.oldest_idx)

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