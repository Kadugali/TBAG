class Character():
# create character

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.item = []

# describe(self):
    def describe(self):
      print(self.name + " is here!")

      print(self.description)

# Set what this character will say when talked to
    def set_conversation(self, conversation):
       self.conversation = conversation

# Talk to this character
    def talk(self):
       if self.conversation is not None:
          print("[" + self.name + " says]: " + self.conversation)
       else:
          print(self.name + " doesnt want to talk to you")
    
# Fight with this character
    def fight(self):
       print(self.name + " doesn't want to fight with you")
       return True

class Friend(Character):
   def __init__(self, char_name, char_description):
      super().__init__(char_name, char_description)
      self.weakness = None

   def gift(self, gift_item):
      if gift_item in self.item:
         print("Sorry, I can't carry any more of those")
      else:
         self.item.append(gift_item)
         return self.item
         


class Enemy(Character):
   def __init__(self, char_name, char_description):
      super().__init__(char_name, char_description)
      self.weakness = None
   
   def set_weakness(self, item_weakness):
      self.weakness = item_weakness
   
   def get_weakness(self):
      return self.weakness
   
   def fight(self, combat_item):
      if combat_item == self.weakness:
         print(f"A close shave! You fended off {self.name} with the {combat_item}")
         return True
      else:
         print(f"{self.name} crushes you, puny adventurer ")
      return False
   
   def steal(self, item):
      if item in self.item:
         self.item.remove(item)
         return True
      else:
         print("This item doesn't exist")
      return False
   
   def sleep(self, keyword):
      if keyword == "sleep":
         print("zzzzzzzzzzzzzzzzzz")
      else:
         print("You can't kill me")

      