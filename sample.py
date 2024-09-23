class Cookie:
    def __init__(self, color):
        self.color = color
        print(f"This is the {color} color")


    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color = color    

cookie_color = Cookie("red")        
        