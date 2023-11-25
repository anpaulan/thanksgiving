import random as r

class ThanksgivingGuestList:
    def __init__(self, guests):
        self.guests = guests
        self.guest_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
        self.dishes = ['macaroni and cheese', 'pecan pie' ,'winter squash' ,'sweet potatoes', 'coffee' , 'biscuits', 'salad', 'dressing' ,'gravy', 'corn', 'cranberry sauce' , 'quiche']
        self.assignment= {}

    def add_dish(self, dish):
        self.dish = dish
        self.dishes.append(dish)

    def add_guest(self, guest):
        self.guest = guest
        self.guests.append(guest)

    def randomize_guest(self):
        r.shuffle(self.dishes) #chages order of the dishes
        num_guests = len(self.guests) #set boundaries if the dishes list exceeds the guest list
        for i in range(num_guests):
            self.assignment[self.guests[i]] = self.dishes[i] #assigns dish to a person

    def print_list(self):
        print('Thanksgiving Guest List \n')
            print(f'{guest}: {dish}')
    
    def print_guest_dish(self,guest):
        self.guest = guest # takes which guest you want to check
        if guest in self.assignment: # makes sure the guest is in the list
            print(f"{guest}'s Dish: {self.assignment[guest]}")
        else:
            print('Imaginary friends do not count') #saying guest does not exist in your guest list

    def enough_food(self): #only works if there is more food than people, if more people, print list does not work, did not have enough time to figure that bit out
        if len(self.guest_list) > len(self.dishes): 
            print('There is not enough food')
        else: 
            print('You will be eating good tonight!')
        
        pass

guests = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
thanksgiving = ThanksgivingGuestList(guests)
thanksgiving.add_dish('Z')
thanksgiving.add_dish('O')
thanksgiving.add_guest('X')
thanksgiving.randomize_guest()
thanksgiving.print_list()
thanksgiving.enough_food()
guest_to_check = 'z'  # Change this to check assignments for different guests
thanksgiving.print_guest_dish(guest_to_check)