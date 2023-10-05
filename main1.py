import Person_PythonExample1 as person
import CreditCardValidator_C

# Person instance (object)
han = person.Person('Han', 'Solo', '30', 'man', 'flying spaceships')

print(han.just_firstandlast())
han.full()
print('Checking that only card_verifier has this message')

card = CreditCardValidator_C.CreditCardValidator()
card.credit_card_validator()