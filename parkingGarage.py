class ParkingGarage():
    def __init__(self, numberOfSpaces):
        self.tickets =[]
        self.parkingSpaces = []
        self.currentTicket = {'paid': False}
        for i in range(numberOfSpaces):
            self.parkingSpaces.append('Space')

    def takeTicket(self, tickets, parkingSpaces):
        if parkingSpaces:
            tickets.append(parkingSpaces.pop())
            print("Please take your ticket and proceed to parking.")
        else:
            print("Sorry, there are no more parking spaces.")

    def payForParking(self, tickets, currentTicket):
        while True:
            if tickets and currentTicket['paid'] == False:
                try:
                    payment = int(input("Please enter the $dollar payment amount: "))
                    if payment:
                        currentTicket["paid"] = True
                        print("Your ticket has been paid and you have 15 mins to leave.")
                        break
                    else: 
                        print("Your response is invalid.")
                except:
                    print("Please enter a valid number.")
            else:
                print("There are no tickets to pay for. ")
                break
            
    def leaveGarage(self, tickets, parkingSpaces, currentTicket):
        if tickets:    
            if currentTicket['paid']:
                print("Thank you, have a nice day.")
            else:
                self.payForParking(tickets, currentTicket)
                print("Thank you, have a nice day.")
            parkingSpaces.append(tickets.pop())
            currentTicket['paid'] = False
        else:
            print("The garage is empty!")
        
    def run(self):
        while True:
            answer = input("What would you like to do? (Park, Pay, Leave, or Quit): ")
            if answer.lower() == 'park':
                self.takeTicket(self.tickets, self.parkingSpaces)
            elif answer.lower() == 'pay':
                self.payForParking(self.tickets, self.currentTicket)
            elif answer.lower() == 'leave':
                self.leaveGarage(self.tickets, self.parkingSpaces, self.currentTicket)
            elif answer.lower() == 'quit':
                break
            else:
                print("Invalid input, please enter 'Park', 'Pay', 'Leave', or 'Quit'.")

myGarage = ParkingGarage(10)
myGarage.run()
            