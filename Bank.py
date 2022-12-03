import json
import colorama as cr
import random
import time
import CN

# Bank Class

class Bank:
  def __init__(self, admin):
    self.admin = admin # IF the user is a admin do this...
    if self.admin == True:
      self.Bank_admin()
     else:
      pass
  def Console (self):
    CN.Console()

      
class Bank_admin(Bank):# Bank Admin have another command that a no admin dont have
  def See_Users (self):
    pass
