

class HandleCollision:
    def __init__(self):
        self.objects=[]
        self.lastPlay=0
    
    def registerObject(self,tamb):
        self.objects.insert(0,tamb)

    def Handle(self,position):
        if(not self.objects[self.lastPlay].active(position)):
            self.objects[self.lastPlay].playing=False
        for i,ob in enumerate(self.objects):
            if(ob.active(position)):
                if(not ob.playing):
                    ob.play()
                    self.lastPlay=i
                    
    def inObject(self,position):
        for i,ob in enumerate(self.objects):
            if(ob.active(position)):
                return True
        return False

