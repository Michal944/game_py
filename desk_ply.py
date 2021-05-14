class Desk():
    def __init__(self,size, x_size):
        self.desk = ['='*size,
                     '='*size]
   
        x_size-=2
        self.x_size=x_size
        self.size=size
        self.speed = 0
        self.desk_field = ['|' + ' '*int((x_size-size)/2) + self.desk[0] + ' '*int((x_size-size)/2) + '|',
                           '|' + ' '*int((x_size-size)/2) + self.desk[0] + ' '*int((x_size-size)/2) + '|']
            
    def move_left(self,speed=2):
        if (self.x_size / 2) - (self.size / 2) > self.speed:
            self.speed+=speed
            self.desk_field = ['|' + ' '*(int((self.x_size-self.size)/2)-self.speed) + self.desk[0] + ' '*(int((self.x_size-self.size)/2)+self.speed) + '|',
                               '|' + ' '*(int((self.x_size-self.size)/2)-self.speed) + self.desk[0] + ' '*(int((self.x_size-self.size)/2)+self.speed) + '|']
        
    def move_right(self,speed=2):
        if (self.size / 2) - (self.x_size / 2) < self.speed:
            self.speed-=speed
            self.desk_field = ['|' + ' '*(int((self.x_size-self.size)/2)-self.speed) + self.desk[0] + ' '*(int((self.x_size-self.size)/2)+self.speed) + '|',
                               '|' + ' '*(int((self.x_size-self.size)/2)-self.speed) + self.desk[0] + ' '*(int((self.x_size-self.size)/2)+self.speed) + '|']
        

    def get_desk(self):
        return self.desk_field
