import random as r

class ThanksgivingGuestList:
    def __init__(self, guests:list):
        self.guests = guests
        self.dishes = ['macaroni and cheese', ' pecan pie' ,' winter squash' ,'sweet potatoes', 'coffee' , 'biscuits', 'salad', 'dressing' ,' gravy', 'corn', 'cranberry sauce' , 'quiche']
        self.assignment= {}

    def randomize_guest(self):
        r.shuffle(self.dishes) #chages order of the dishes
        num_guests = len(self.guests) #set boundaries if the dishes list exceeds the guest list
        for i in range(num_guests):
            self.assignment[self.guests[i]] = self.dishes[i] #assigns dish to a person

    def print_list(self):
        print('Thanksgiving Guest List')
        for guest,dish in self.assignment.items(): # this prints everyone in the list with their assigned dish
            print(f'{guest}: {dish}')
    
    def print_guest_dish(self,guest):
        self.guest = guest # takes which guest you want to check
        if guest in self.assignment: # makes sure the guest is in the list
            print(f'{guest} has been assigned {self.assignment[guest]}')
        else:
            print('Imaginary friends do not count') #saying guest does not exist in your guest list

guests = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'] #can add more if you want
thanksgiving = ThanksgivingGuestList(guests)
thanksgiving.randomize_guest()
thanksgiving.print_list()
guest_to_check = 'z'  # Change this to check assignments for different guests
thanksgiving.print_guest_dish(guest_to_check)