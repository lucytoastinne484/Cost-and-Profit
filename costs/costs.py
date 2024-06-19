class level:
    def __init__(self):
        pass
    def Vital(self,water,energy,iptu,net):
        total_cost = water + energy + iptu + net
        print()
        print("O total com gastos da casa é: ",total_cost)
    def Health(self,odonto,check_up):
        health = odonto + check_up
        print()
        print("O custo de saúde é: ",health)
    def cel(self,cel):
        phone_services = cel
        print()
        print("O gasto com celular é: ",phone_services)
    def transport(self,bus,train):
        transport_total = bus + train
        print()
        print("O custo total com transporte é de: ",transport_total)
    def emergency(self,water,energy,iptu,odonto,check_up,cel,bus,train,net):
        
        res = water + energy + iptu + odonto + check_up + cel + bus + train + net
        
        ideal_res = res * 6
        print()
        print("A reserva de energencia ideal é de: ",ideal_res)
        
        
    
    
    
class Revenue:
    def __init__(self):
        pass
    def rx(self,rx):
        self.sales = rx
    def levelment(cx):
        #our levelment must be a the result of a subtraction where the cost and the revenue 
        #is zero or equal to each other
        our_revenue = 19.15
        our_cost = cx
        our_levelment = cx / 19.15
        print("Our cost is: ",our_cost)
        print("Our revenue is: ",our_revenue)
        print("Our point of levelment is: ",our_levelment)
    def profit(self,x,cx,ct):
        revenue = 19.15 * x
        total_cost = cx * x + ct
        my_cost = ct
        profit = revenue - total_cost
        my_profit = revenue - my_cost
        print("Custo: ",total_cost)
        print("Receita: ",revenue)
        print("Lucro: ",profit)
        print("Meu lucro: ",my_profit)
        print("Meu custo: ",my_cost)
    def reserv (profit):
        emergency_reserv = profit * 0.20
        print("A reserva de emergencia será de: ",emergency_reserv)





 
        
        
    
    
    
    
costs = level()

levelment_1 = Revenue.levelment(76.6)

total_profit = Revenue.profit(8,8,1.9,76.6)

total_reserv = Revenue.reserv(61.39)

vital_costs = costs.Vital(200,200,145.0,200)

health_care = costs.Health(54.99,214.27)

cellphone = costs.cel(50.0)

transport = costs.transport(100.0, 100.0)

emergency_cost = costs.emergency(200,200,145,54.99,214.27,50.0,100.0,100.0,200.0)

