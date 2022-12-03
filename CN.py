# Here i make a console for manage data in a better space
import Bank

exit = False

class console (Bank.bank(False)):
  while not exit:
    # Preguntaremos que quiere hacer
    command = input("""
      What you want to do:
      1-  Login    # Login for use your money
      2-  Register # Register for start using your money
    """)
    if command == "":
      pass
