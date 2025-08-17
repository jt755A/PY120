class Cat:
    def get_name(self):
        try:
            return self.name

        except AttributeError:
            return 'Name not set!'

bayou = Cat()
print(bayou.get_name())