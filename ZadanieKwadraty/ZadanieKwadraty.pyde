class Kwadrat():
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat): 
    def sketchPasiasty(self, x, y, paski): 
        Kwadrat.sketch(self, x, y) 
        space = self.bok/paski
        _xLinii_ = 0 
        fill(400,90,70,80)
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
class KraciastyKwadrat(Kwadrat): 
    def sketchKraciasty(self, x, y, paski): 
        Kwadrat.sketch(self, x, y) 
        space = self.bok/paski 
        _yLinii_ = 0  
        fill(400,90,70,80)
        for pasek in range(0, paski): 
            line(x, y+_yLinii_, x+self.bok, y+_yLinii_)
            _yLinii_ += space

def setup():
    size(500, 500)
    malyKwadrat = Kwadrat(50.0) 
    malyKwadrat.sketch(200, 300) 
    fill(100,100,40,100) 
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    fill(90,400,20,25)
    malyKwadrat.sketch(100, 200) 
    malyPasiastyKwadrat = PasiastyKwadrat(30.0)
    malyPasiastyKwadrat.sketchPasiasty(300, 300, 5) 
    malyPasiastyKwadrat.sketchPasiasty(100,300, 8) 
    duzyPasiastyKwadrat  = PasiastyKwadrat(120.0)
    duzyPasiastyKwadrat.sketchPasiasty(300, 50, 12)
    duzyPasiastyKwadrat.sketch(350, 300)
    malyKraciastyKwadrat = KraciastyKwadrat(70.0)
    malyKraciastyKwadrat.sketchKraciasty(400,100,5)
    malyKraciastyKwadrat.sketchKraciasty(400,200,10)
    # miały być dwa obiekty
    # 1,75pkt
