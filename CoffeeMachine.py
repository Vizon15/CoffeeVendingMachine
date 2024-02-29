class CoffeeMachine:
    def __init__(self, balance=500, water=1000, milk=540, c_beans=200, d_cups=10):
        self.balance = balance
        self.water = water
        self.milk = milk
        self.coffee_beans = c_beans
        self.d_cups = d_cups

    def status_printer(self):
        print(f"""
        The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee_beans} of coffee beans
        {self.d_cups} of disposable cups
        {self.balance} of money
        """)


    def action_perform(self):
        while True:
            input_action = input( "Write action (buy, fill, take, remaining, exit): " )
            if input_action == "exit":
                break
            elif input_action == "buy":
                self.buy()
            elif input_action == "fill":
                self.fill()
            elif input_action == "take":
                self.take()
            elif input_action == "remaining":
                self.status_printer()
            else:
                print( "Invalid input!" )

    def buy(self):
        input_option = input( """What do you want to buy? 1 - espresso,
        2 - latte, 3 - cappuccino, back - to main menu :""" )
        if input_option == '1':
            coffee_name = "Espresso"
            water = 250
            coffee = 16
            price = 4
            if self.water < water:
                print("Sorry, not enough water!")
            elif self.coffee_beans < coffee:
                print("Sorry, not enough coffee beans!")
            elif self.d_cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print(f"""
                    Invoice
                =========================
                Item            Qty         Price
                1) {coffee_name}     1           ${price}
                Thank You, Enjoy Your Coffee. 
                """)
                self.balance += price
                self.water -= water
                self.coffee_beans -= coffee
                self.d_cups -= 1

        elif input_option == '2':
            coffee_name = "Latte"
            water = 350
            milk = 75
            coffee = 20
            price = 7
            self.check_ingredients(coffee_name=coffee_name, water=water, milk=milk, coffee=coffee, price=price )

        elif input_option == '3':
            coffee_name = "Latte"
            water = 200
            milk = 100
            coffee = 12
            price = 6
            self.check_ingredients(coffee_name=coffee_name,water=water,milk=milk,coffee=coffee,price=price)
        elif input_option == "back":
            self.action_perform()
            # return -1
            exit()

        # else:
        #     print("Invalid input!")
        # self.status_printer()

    def fill(self):
        water = int(input("Write how many ml of water you want to add: "))
        milk = int(input("Write how many ml of milk you want to add: "))
        c_beans = int(input("Write how many grams of coffee beans you want to add: "))
        d_cups = int(input("Write how many disposable coffee cups you want to add: "))
        self.water += water
        self.milk += milk
        self.coffee_beans += c_beans
        self.d_cups += d_cups
        # self.status_printer()

    def take(self):
        print(f"I gave you ${self.balance}")
        self.balance = 0
        # self.status_printer()
    def check_ingredients(self,coffee_name, water=0, milk=0, coffee=0, price=0):
        if self.water < water:
            print( "Sorry, not enough water!" )
        elif self.coffee_beans < coffee:
            print( "Sorry, not enough coffee beans!" )
        elif self.d_cups < 1:
            print( "Sorry, not disposable cups!" )
        elif self.milk < milk:
            print( "Sorry, not enough milk!" )
        else:
            print( f"""
                Invoice
            ==========================
            Item            Qty       Price
            1) {coffee_name}         1       ${price}
            Thank You, Enjoy Your Coffee.
            """ )
            self.balance += price
            self.water -= water
            self.milk -= milk
            self.coffee_beans -= coffee
            self.d_cups -= 1



coffee_machine = CoffeeMachine()
# coffee_machine.status_printer()
coffee_machine.action_perform()