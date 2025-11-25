class MyList(list):
        list = []
        def __init__ (self, list = []):
                self.list = list
 
        def print_sorted(self):
             self.sort()
             print(self)
