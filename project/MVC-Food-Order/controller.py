import view as View

class Controller:
    
    def calTotal(self, order):
        print("\n ---- Your order ----")
        price = ["Price"]
        count = 0
        totalPrice = 0

        for key, value in order.items():
            print(f"{key}: {value}")

        for values in price:
            if values in order.keys():
                count += order[values]
        totalPrice = count

        return View.View().showTotal(totalPrice)

    def calPayment(self, totalPrice, amount):
        
        amount = int(amount)
        
        if amount < totalPrice:
            print("\nAMOUNT NOT SUFFICIENT !\n")
            return View.View().showTotal(totalPrice)
        else:
            balance = amount - totalPrice

        return View.View().showReceipt(balance, totalPrice, amount)
        
                