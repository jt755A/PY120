'''
P 

Algorithm
- empty line function
    - leading, trailing |
    - len of message + 2 whitespace ' '

- horizontal rule function
    - leading, trailing +
    - len of message  dashes -

- message
    - leading, trailing whitespace ' '

'''

class Banner:
    def __init__(self, message, width=len(message) + 4):
        self.message = message
        self.width = width
    
    @property
    def message(self):
        return self.message

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        spaces = ' ' * len(self.message)
        return f"| {spaces} |"

    def _horizontal_rule(self):
        dashes = '-' * (len(self.message) + 2)
        return f'+{dashes}+'

    def _message_line(self):
        return f"| {self.message} |"
    

# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+