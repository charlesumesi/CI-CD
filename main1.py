import argparse
import Person_PythonExample1 as person
import CreditCardValidator_C

parser = argparse.ArgumentParser()
parser.add_argument("--git", action="store_true", help="For Git push command only")
args = parser.parse_args()

# Person instance (object)
han = person.Person('Han', 'Solo', '30', 'man', 'flying spaceships')

print(han.just_firstandlast())
han.full()
print('Checking that only card_verifier has this message')

if __name__ == "__main__":
    if args.git:
        print('The card number validator has been bypassed by Git push. (Check the validator locally.)')
    else:
        card = CreditCardValidator_C.CreditCardValidator()
        card.credit_card_validator(input('Enter credit card number (with no spaces) : '))
    