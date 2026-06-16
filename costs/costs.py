class level:
    def __init__(self):
        pass
    def Vital(self,water,energy,iptu,net,gas,essential_products):
        products = essential_products
        monthy_inventory = 700.0
        month_taxes = 1200
        total_cost = water + energy + iptu + net + gas + monthy_inventory + month_taxes
        
        print()
        print("O total com gastos da casa é: ",total_cost)
        print()
        value_to_invest = total_cost * 200
        print()
        print("O valor ideal para investir em uma carteira que possa dar retornos é:",value_to_invest)
        
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
    def emergency(self,water,energy,iptu,odonto,check_up,cel,bus,train,net,gas,products):
        
        res = water + energy + iptu + cel + bus + train + net + gas
        
        ideal_res = res * 6
        print()
        print("A reserva de energencia ideal é de: ",ideal_res)
    def Mei(self):
        print()
        mei_value = 86.70
        print("The MEI tax is: ",mei_value)
        
        
    
    
    
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
    def delivery(self,q_of_deliveries,valor):
        total_valor = q_of_deliveries * valor
        print("The revenue with deliveries is:", total_valor)
        print("")
        month_delivery = total_valor * 26
        print("The month return is: ",month_delivery)
        
        
        





 
        
        
    
    
    
    
costs = level()


health_care = costs.Health(119,249)

cellphone = costs.cel(50.0)

transport = costs.transport(0, 100.0)

emergency_cost = costs.emergency(200,200,145,54.99,214.27,50.0,100.0,100.0,130.0,115.0,800.0)

mei_tax_cost = costs.Mei()


print("")
Revenue.delivery("", 7 , 7)