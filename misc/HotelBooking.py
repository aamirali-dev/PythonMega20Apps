import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_card_security = pd.read_csv('card_security.csv', dtype=str)


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {'number': self.number, 'expiration': expiration, 'holder': holder, 'cvc': cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security['number'] == self.number, 'password'].squeeze()
        if password == given_password:
            return True
        else:
            return False


class Hotel:

    def __init__(self, hotel_id) -> None:
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f'''
        THANK YOU for your reservation!
        Here are your booking details:
        Name: {self.customer_name}
        Hotel Name: {self.hotel_object.name}'''
        return content


class SpaReservation(ReservationTicket):
    def generate(self):
        content = f'''
        THANK YOU for your SPA reservation! 
        HERE are your SPA booking details!
        Name: {self.customer_name}
        Hotel Name: {self.hotel_object.name}'''
        return content


print(df)
id = input('Enter the id of the hotel: ')
hotel = Hotel(id)
if hotel.available():
    credit_card = SecureCreditCard(number='1234')
    if credit_card.validate(expiration='12/26', holder='JOHN SMITH', cvc='123'):
        if credit_card.authenticate('mypass'):
            hotel.book()
            name = input('Enter your name: ')
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())
            yes = input('Do you want to book a spa package? ')
            if yes == 'yes':
                print(SpaReservation(name, hotel).generate())
        else:
            print('Credit Card authentication failed.')
    else:
        print('there was a problem with your payment method')
else:
    print('hotel is not free')
