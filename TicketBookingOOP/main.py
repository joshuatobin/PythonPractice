import datetime

class TicketBookingSystem():
    def __init__(self):
        pass
    
    def list_events():
        pass
    
    def book():
        pass
    
    def cancel():
        pass
    
class Event():
    def __init__(self, name, date, available_seats):
        self.name = name
        self.date = date
        self.available_seats = available_seats

class User():
    pass

class Reservation():

    def store():
        pass

    def process():
        pass


def main():
    date = datetime.datetime.now()
    ticket = TicketBookingSystem()
    event = Event(name="WWF", date=date, available_seats=True)
    
    print(ticket)
    print(event)
    
if __name__ == "__main__":
    main()
