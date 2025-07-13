class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            print('Name not set!')

    
cat1 = Cat()
# cat1.name = 'bobby'
print(cat1.get_name())