# "Do you love me?"
question = input("what is your name?")
print(f"Hello {question}, I have a question for you.")

question2 = input("Do you love me? (yes/no):")
if question2.lower() == "no":
    print(f"shembade, khadoos, nay karat ka prem? gap Yes var click kar.")
    input("nit vichar karun sang yes/no:")
    if question2.lower() == "no":
        print ("khota khota na")
    elif question2.lower() == "yes":
        print("I love you my sweet big dhungi")
    input("yes/no:")
    if question2.lower() == "no":
        print ("mala mahitiye, majhi sweet booboo loves little dhungi. I love you my sweet big dhungi")
    elif question2.lower() == "yes":
        print("I love you my sweet big dhungi")
elif question2.lower() == "yes":
    print("I love you my sweet big dhungi") 