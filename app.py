class vi:
    def __init__(self, x, dx):
        self.x = x
        self.dx = dx

    def soma(self, y):
        self.x += y.x
        self.dx += y.dx
    
    def sub(self, y):
        self.x -= y.x
        self.dx += y.dx

    def produto(self, y):
        self.dx = ( (self.x*y.dx) + (y.x*self.dx) )
        self.x *= y.x

    def potencia(self,pt):
        self.dx = (pt*(pow(self.x , (pt-1) )*self.dx))
        self.x = pow(self.x , pt)
    
    def divisao(self,y):
        self.dx = ( (self.x*y.dx) + (y.x*self.dx) ) / (y.x**2)
        self.x /= y.x

    def produtoporconstante(self,cte):
        self.x *= cte
        self.dx *= cte
        


# p = vi(3.13 , 0.01)
# p.potencia(2)

# print(p.x)
# print(p.dx)


# t1 = vi(3.13 , 0.01)
# t2 = vi(3.14 , 0.01)
# t3 = vi(3.12 , 0.01)

# raioe = vi(0.006 , 0.0001)
# massa = vi(1.51575 , 0.0003)
# g = 9.81
# h_2 = vi(0.934 , 0.002)

# raioe.potencia(2)
# raioe.produto(massa)


# t1.potencia(2)
# t1.produtoporconstante(g)
# t1.divisao(h_2)
# t1.x -= 1
# t1.produto(raioe)
# print('t1 |' + str(t1.x) + '  +  ' + str(t1.dx) )


# t2.potencia(2)
# t2.produtoporconstante(g)
# t2.divisao(h_2)
# t2.x -= 1
# t2.produto(raioe)
# print('t2 |' + str(t2.x) + '  +  ' + str(t2.dx) )

# t3.potencia(2)
# t3.produtoporconstante(g)
# t3.divisao(h_2)
# t3.x -= 1
# t3.produto(raioe)
# print('t3 |' + str(t3.x) + '  +  ' + str(t3.dx) )

I = 0.0001

raioe = vi(0.006 , I)
massae = vi(0.12125 , I)


raio1df = vi(0.006 , I)
raio2df = vi(0.0625 , I)
massadf = vi(0.4707 , I)

raio1co = vi(0.0625 , I)
raio2co = vi(0.076 , I)
massaco = vi(0.9238 , I)

def eixoo(raioe, massae):
    raioe.potencia(2)
    raioe.produto(massae)
    raioe.produtoporconstante(0.5)

def cilindro(r1 , r2 , m):
    r1.potencia(2)
    r2.potencia(2)
    r1.soma(r2)
    r1.produto(m)
    r1.produtoporconstante(0.5)

eixoo(raioe, massae)
cilindro(raio1df, raio2df, massadf)
cilindro(raio1co, raio2co, massaco)


raioe.soma(raio1df)
raioe.soma(raio1co)

print(str(raioe.x) + "  +  " + str(raioe.dx))