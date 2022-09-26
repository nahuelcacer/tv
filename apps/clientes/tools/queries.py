
class Queries():
    def __init__(self, obj):
        self.obj = obj


    def q_all(self):
        return self.obj.objects.all()


    def q_get(self,filter):
        return self.obj.objects.get(id=filter)
    
    def q_filter(self,filter):
        return self.obj.objects.filter(cliente=filter)