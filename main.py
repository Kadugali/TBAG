from room import Room
from character import Enemy
from character import Character
from character import Friend
from item import Item
# Create rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

# Create friendly
rupert = Character("Rupert", "A friendly character")
rupert.set_conversation("Hi there, I am one of the last survivors")

# Create Enemy
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh...rgrhl... brains...")
dave.set_weakness("cheese")

# Set room description
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
# print(kitchen.get_description())
dining_hall.set_description("A large room with ornate golden decorations")

# Link Rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Place a character in each room
dining_hall.set_character(dave)
kitchen.set_character(rupert)

# Set the current_room
current_room = kitchen

# Add key to the game 
key = Item()
key.set_name("Secret Key")
key.set_description("This key opens the magic door")

# Pass gift to friend
charles = Friend("Charles", "Rupert's son")
dave.item.append(key)
dave.item.append("key")
[print(dave.item)]


# Ask user for room direction 
while True:
  print('\n')
  current_room.get_details()

  check_inhabitant = current_room.get_character()
  
  if check_inhabitant is not None:
    check_inhabitant.describe()

  command = input(">")
  if command in ['north', 'south', 'east']:
    current_room = current_room.move(command)
  elif command == "talk": 
    if current_room == kitchen:
      rupert.talk()
    elif current_room == dining_hall:
      dave.talk()
  elif command == "fight":
    if current_room == dining_hall:
      fight = input("Choose an item to fight with > ")
      dave.fight(fight)
    elif current_room == kitchen:
      rupert.fight()
  elif command == "steal":
    if current_room == dining_hall:
      stolen_item = input("what item would you like to steal > ")
      if stolen_item in dave.item:
        dave.item.remove(stolen_item)
        print(f"You have stolen the {stolen_item} from Dave, you can use this to open the locked door.")
      else:
        print("This item doesn't exsits")
    elif current_room == kitchen:
      print("You need to find Dave, he has the key")
  elif command == "west":
    if current_room == dining_hall:
      if "key" in dave.item:
        print("Sorry but you need to steal the key from Dave")
      else:
          current_room = current_room.move(command)
          print("Congratulations, you have made it to the ballroom, END GAME")
          break

  # print("END GAME")
  # break
  