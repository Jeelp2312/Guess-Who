# Guess Who
import random  # Imports the random library


# Game introduction and game loop set up
def intro():
  # Introductory statements
  print("Welcome To The Guess Who Game!".center(44))
  print("~ Single Player Edition ~".center(44))


# Function resets game variables
def restart_game():
  global game_done, game_run, questions_asked, char_num_list  # Allows changes to global variables within a function

  # Game loops
  game_done = False
  game_run = True

  # Character display is reset, 1s means the characters are all on the board
  char_num_list = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
  questions_asked = 0  # Questions asked gets reset
  character_selection()  # Calls another function which selects another character to guess


# Function declares character name positioning in 2-D list and dcitionary containing information of all 25 characters
def character_lists():
  global characters, char_num_list, characters_dict  # Declares global variables and allows for changes within the function

  # First row of names
  A1 = 'Aiden'
  A2 = 'Amber'
  A3 = 'Asher'
  A4 = 'Amara'
  A5 = 'Aaron'
  # Attribution codes for the row of names
  '''
  Aiden: A1, B2, C3, D4, E5.
  Amber: A1, B3, C5, D2, E2.
  Asher: A1, B4, C2, D5, E3.
  Amara: A1, B5, C1, D1, E4.
  Aaron: A1, B1, C4, D3, E1.
  '''

  # Second row of names
  B1 = 'Bryce'
  B2 = 'Blake'
  B3 = 'Bella'
  B4 = 'Brook'
  B5 = 'Betty'
  # Attribution codes for the row of names
  '''
  Bryce: A2, B3, C4, D5, E1.
  Blake: A2, B4, C1, D3, E3.
  Bella: A2, B5, C3, D1, E4.
  Brook: A2, B1, C5, D2, E5.
  Betty: A2, B2, C2, D4, E2.
  '''

  # Third row of names
  C1 = 'Chloe'
  C2 = 'Caleb'
  C3 = 'Clara'
  C4 = 'Chase'
  C5 = 'Chris'
  # Attribution codes for the row of names
  '''
  Chloe: A3, B4, C5, D1, E3.
  Caleb: A3, B5, C2, D4, E1.
  Clara: A3, B1, C4, D2, E5.
  Chase: A3, B3, C3, D3, E4.
  Chris: A3, B2, C1, D5, E2.
  '''

  # Fourth row of names
  D1 = 'Donna'
  D2 = 'Diana'
  D3 = 'Dylan'
  D4 = 'Daisy'
  D5 = 'David'
  # Attribution codes for the row of names
  '''
  Donna: A4, B5, C1, D5, E3.
  Diana: A4, B1, C2, D4, E1.
  Dylan: A4, B4, C5, D2, E5.
  Daisy: A4, B2, C3, D1, E2.
  David: A4, B3, C4, D3, E4.
  '''

  # Fifth row of names
  E1 = 'Edwin'
  E2 = 'Eddie'
  E3 = 'Emily'
  E4 = 'Eliza'
  E5 = 'Ethan'
  # Attribution codes for the row of names
  '''
  Edwin: A5, B1, C3, D5, E5.
  Eddie: A5, B2, C4, D1, E3.
  Emily: A5, B3, C1, D4, E2.
  Eliza: A5, B5, C5, D2, E4.
  Ethan: A5, B4, C2, D3, E1.
  '''

  # Putting the characters into a 2-D list to display on the terminal/console
  characters = [[A1, A2, A3, A4, A5], [B1, B2, B3, B4, B5], [C1, C2, C3, C4, C5], [D1, D2, D3, D4, D5], [E1, E2, E3, E4, E5]]
  char_num_list = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]  # Tracks if characters should be displayed (1 - Yes and 0 - No)

  # Dictionary containing all information for the 25 characters
  characters_dict = {
    "char1_name": "Aiden",
    "char1_row": 0,
    "char1_col": 0,
    "char1_initial": "A",
    "char1_region": "America",
    "char1_hair": "Blonde",
    "char1_accessory": "Hat",
    "char1_feature": "Beard",
    "char2_name": "Amber",
    "char2_row": 0,
    "char2_col": 1,
    "char2_initial": "A",
    "char2_region": "Europe",
    "char2_hair": "White",
    "char2_accessory": "Ring",
    "char2_feature": "Big Nose",
    "char3_name": "Asher",
    "char3_row": 0,
    "char3_col": 2,
    "char3_initial": "A",
    "char3_region": "Australia",
    "char3_hair": "Brown",
    "char3_accessory": "Makeup",
    "char3_feature": "Moustache",
    "char4_name": "Amara",
    "char4_row": 0,
    "char4_col": 3,
    "char4_initial": "A",
    "char4_region": "Africa",
    "char4_hair": "Black",
    "char4_accessory": "Glasses",
    "char4_feature": "Braces",
    "char5_name": "Aaron",
    "char5_row": 0,
    "char5_col": 4,
    "char5_initial": "A",
    "char5_region": "Asia",
    "char5_hair": "Ginger",
    "char5_accessory": "Wig",
    "char5_feature": "Rosey Cheeks",
    "char6_name": "Bryce",
    "char6_row": 1,
    "char6_col": 0,
    "char6_initial": "B",
    "char6_region": "Europe",
    "char6_hair": "Ginger",
    "char6_accessory": "Makeup",
    "char6_feature": "Rosey Cheeks",
    "char7_name": "Blake",
    "char7_row": 1,
    "char7_col": 1,
    "char7_initial": "B",
    "char7_region": "Australia",
    "char7_hair": "Black",
    "char7_accessory": "Wig",
    "char7_feature": "Moustache",
    "char8_name": "Bella",
    "char8_row": 1,
    "char8_col": 2,
    "char8_initial": "B",
    "char8_region": "Africa",
    "char8_hair": "Blonde",
    "char8_accessory": "Glasses",
    "char8_feature": "Braces",
    "char9_name": "Brook",
    "char9_row": 1,
    "char9_col": 3,
    "char9_initial": "B",
    "char9_region": "Asia",
    "char9_hair": "White",
    "char9_accessory": "Ring",
    "char9_feature": "Beard",
    "char10_name": "Betty",
    "char10_row": 1,
    "char10_col": 4,
    "char10_initial": "B",
    "char10_region": "America",
    "char10_hair": "Brown",
    "char10_accessory": "Hat",
    "char10_feature": "Big Nose",
    "char11_name": "Chloe",
    "char11_row": 2,
    "char11_col": 0,
    "char11_initial": "C",
    "char11_region": "Australia",
    "char11_hair": "White",
    "char11_accessory": "Glasses",
    "char11_feature": "Moustache",
    "char12_name": "Caleb",
    "char12_row": 2,
    "char12_col": 1,
    "char12_initial": "C",
    "char12_region": "Africa",
    "char12_hair": "Brown",
    "char12_accessory": "Hat",
    "char12_feature": "Rosey Cheeks",
    "char13_name": "Clara",
    "char13_row": 2,
    "char13_col": 2,
    "char13_initial": "C",
    "char13_region": "Asia",
    "char13_hair": "Ginger",
    "char13_accessory": "Ring",
    "char13_feature": "Beard",
    "char14_name": "Chase",
    "char14_row": 2,
    "char14_col": 3,
    "char14_initial": "C",
    "char14_region": "Europe",
    "char14_hair": "Blonde",
    "char14_accessory": "Wig",
    "char14_feature": "Braces",
    "char15_name": "Chris",
    "char15_row": 2,
    "char15_col": 4,
    "char15_initial": "C",
    "char15_region": "America",
    "char15_hair": "Black",
    "char15_accessory": "Makeup",
    "char15_feature": "Big Nose",
    "char16_name": "Donna",
    "char16_row": 3,
    "char16_col": 0,
    "char16_initial": "D",
    "char16_region": "Africa",
    "char16_hair": "Black",
    "char16_accessory": "Makeup",
    "char16_feature": "Moustache",
    "char17_name": "Diana",
    "char17_row": 3,
    "char17_col": 1,
    "char17_initial": "D",
    "char17_region": "Asia",
    "char17_hair": "Brown",
    "char17_accessory": "Hat",
    "char17_feature": "Rosey Cheeks",
    "char18_name": "Dylan",
    "char18_row": 3,
    "char18_col": 2,
    "char18_initial": "D",
    "char18_region": "Australia",
    "char18_hair": "White",
    "char18_accessory": "Ring",
    "char18_feature": "Beard",
    "char19_name": "Daisy",
    "char19_row": 3,
    "char19_col": 3,
    "char19_initial": "D",
    "char19_region": "America",
    "char19_hair": "Blonde",
    "char19_accessory": "Glasses",
    "char19_feature": "Big Nose",
    "char20_name": "David",
    "char20_row": 3,
    "char20_col": 4,
    "char20_initial": "D",
    "char20_region": "Europe",
    "char20_hair": "Ginger",
    "char20_accessory": "Wig",
    "char20_feature": "Braces",
    "char21_name": "Edwin",
    "char21_row": 4,
    "char21_col": 0,
    "char21_initial": "E",
    "char21_region": "Asia",
    "char21_hair": "Blonde",
    "char21_accessory": "Makeup",
    "char21_feature": "Beard",
    "char22_name": "Eddie",
    "char22_row": 4,
    "char22_col": 1,
    "char22_initial": "E",
    "char22_region": "America",
    "char22_hair": "Ginger",
    "char22_accessory": "Glasses",
    "char22_feature": "Moustache",
    "char23_name": "Emily",
    "char23_row": 4,
    "char23_col": 2,
    "char23_initial": "E",
    "char23_region": "Europe",
    "char23_hair": "Black",
    "char23_accessory": "Hat",
    "char23_feature": "Big Nose",
    "char24_name": "Eliza",
    "char24_row": 4,
    "char24_col": 3,
    "char24_initial": "E",
    "char24_region": "Africa",
    "char24_hair": "White",
    "char24_accessory": "Ring",
    "char24_feature": "Braces",
    "char25_name": "Ethan",
    "char25_row": 4,
    "char25_col": 4,
    "char25_initial": "E",
    "char25_region": "Australia",
    "char25_hair": "Brown",
    "char25_accessory": "Wig",
    "char25_feature": "Rosey Cheeks",
  }


# Sets game loop variables
def game_loop():
  global game_done, game_run, str_format  # Allows adjustment of global variables

  # Starts the game loop and sets variables
  game_done = False
  game_run = True
  str_format = "= = = = = = = = = = = = = = = = = = = = = = ="  # For visual seperation of game features/activities


# Function selects a random character to attemp to guess
def character_selection():
  global character_picked, character_place  # Adjustments for global variables

  row_num = random.randint(0, 4)  # Picks a random integer representing a row of names
  item_num = random.randint(0, 4)  # Picks a random integer representing a name from a row of names
  character_picked = str(characters[row_num][item_num])  # Stores the chosen character in a variable for game purposes
  character_place = (row_num * 5) + (item_num + 1)  # Determines its character number (1 - 25)

  # THIS FEATURE IS JUST FOR MARKING/TESTING PURPOSES ONLY, SHOULD BE REMOVED IF USER IS PLAYING GAME
  print(character_picked, character_place)  # Displays game choosen character on screen


# Displays the board with all the characters
def board_display(numbers_list, names_list):
  # Displays text for game clarity and visuals
  print(str_format)
  print("Guess Who - Game Board".center(44))
  print()
  row_display = ''  # Defines the variable displaying each row

  # Displays the names onto the board
  for row in range(len(numbers_list)):
    for name in range(len(numbers_list[row])):
      if numbers_list[row][name] == 1:  # Checks to see if the character is still in the game
        row_display += '   ' + str(names_list[row][name])  # If he/she is then add it to the row displaying variable
      else:
        row_display += '     X  '  # Otherwise we can add an X to show the character is not in the game
    print(row_display)
    row_display = ''  # Clears the previous row for the next row
  print(str_format)  # Visual formatting of text


# Function represents the menu screen of the game
def menu_options():
  print("What Action Would You Like To Take?".center(44))
  menu_op = ['1. Attrubution Statistics', '2. Character Profile', '3. Ask A Question','4. Guess Who', '5. Exit']  # List of game options for the user to select

  # Displays the options on the screen
  for item in menu_op:
    print(item)

  # Gets the user's input on the game options
  try:
    menu_op_selection = int(input('Enter An Integer To A Corresponding Activity: '))  # Asks user for input
    if menu_op_selection >= 1 and menu_op_selection <= 5:  # If the user enters a valid integer option, returns the integer
      return menu_op_selection
    else:
      print("\nInvalid Integer Option, Please Enter An Integer Above!")  # Invalid integer was given
  except:
    print("\nInvalid Activity Option, Please Enter An Integer Above!")  # Invalid input was given


# Function displays the attrubute statistics for overall characters still left in the game (infomation helps user with asking questions)
def attrubute_stats(names):
  # Initials of the characters (5 characters for each letter A - E)
  a1_initial_a = 0
  a2_initial_b = 0
  a3_initial_c = 0
  a4_initial_d = 0
  a5_initial_e = 0

  # Regions each character is from (5 from each region)
  b1_region_asians = 0
  b2_region_americans = 0
  b3_region_europeans = 0
  b4_region_australians = 0
  b5_region_africans = 0

  # Hair colors of the characters (5 characters for each color)
  c1_hair_black = 0
  c2_hair_brown = 0
  c3_hair_blonde = 0
  c4_hair_ginger = 0
  c5_hair_white = 0

  # Accessories of the characters (5 characters for each item)
  d1_accessories_glasses = 0
  d2_accessories_rings = 0
  d3_accessories_wigs = 0
  d4_accessories_hats = 0
  d5_accessories_makeup = 0

  # Facial features of the characters (5 characters for each feature)
  e1_feature_rosey = 0
  e2_feature_noses = 0
  e3_feature_moustaches = 0
  e4_feature_braces = 0
  e5_feature_beards = 0

  # For each character that is still left, it updates the attrubutes of that character to the overall counts for each attrubute
  # First row of characters
  if names[0][0] == 1:
    a1_initial_a += 1
    b2_region_americans += 1
    c3_hair_blonde += 1
    d4_accessories_hats += 1
    e5_feature_beards += 1
  if names[0][1] == 1:
    a1_initial_a += 1
    b3_region_europeans += 1
    c5_hair_white += 1
    d2_accessories_rings += 1
    e2_feature_noses += 1
  if names[0][2] == 1:
    a1_initial_a += 1
    b4_region_australians += 1
    c2_hair_brown += 1
    d5_accessories_makeup += 1
    e3_feature_moustaches += 1
  if names[0][3] == 1:
    a1_initial_a += 1
    b5_region_africans += 1
    c1_hair_black += 1
    d1_accessories_glasses += 1
    e4_feature_braces += 1
  if names[0][4] == 1:
    a1_initial_a += 1
    b1_region_asians += 1
    c4_hair_ginger += 1
    d3_accessories_wigs += 1
    e1_feature_rosey += 1

  # Second row of characters
  if names[1][0] == 1:
    a2_initial_b += 1
    b3_region_europeans += 1
    c4_hair_ginger += 1
    d5_accessories_makeup += 1
    e1_feature_rosey += 1
  if names[1][1] == 1:
    a2_initial_b += 1
    b4_region_australians += 1
    c1_hair_black += 1
    d3_accessories_wigs += 1
    e3_feature_moustaches += 1
  if names[1][2] == 1:
    a2_initial_b += 1
    b5_region_africans += 1
    c3_hair_blonde += 1
    d1_accessories_glasses += 1
    e4_feature_braces += 1
  if names[1][3] == 1:
    a2_initial_b += 1
    b1_region_asians += 1
    c5_hair_white += 1
    d2_accessories_rings += 1
    e5_feature_beards += 1
  if names[1][4] == 1:
    a2_initial_b += 1
    b2_region_americans += 1
    c2_hair_brown += 1
    d4_accessories_hats += 1
    e2_feature_noses += 1

  # Third row of characters
  if names[2][0] == 1:
    a3_initial_c += 1
    b4_region_australians += 1
    c5_hair_white += 1
    d1_accessories_glasses += 1
    e3_feature_moustaches += 1
  if names[2][1] == 1:
    a3_initial_c += 1
    b5_region_africans += 1
    c2_hair_brown += 1
    d4_accessories_hats += 1
    e1_feature_rosey += 1
  if names[2][2] == 1:
    a3_initial_c += 1
    b1_region_asians += 1
    c4_hair_ginger += 1
    d2_accessories_rings += 1
    e5_feature_beards += 1
  if names[2][3] == 1:
    a3_initial_c += 1
    b3_region_europeans += 1
    c3_hair_blonde += 1
    d3_accessories_wigs += 1
    e4_feature_braces += 1
  if names[2][4] == 1:
    a3_initial_c += 1
    b2_region_americans += 1
    c1_hair_black += 1
    d5_accessories_makeup += 1
    e2_feature_noses += 1

  # Fourth row of characters
  if names[3][0] == 1:
    a4_initial_d += 1
    b5_region_africans += 1
    c1_hair_black += 1
    d5_accessories_makeup += 1
    e3_feature_moustaches += 1
  if names[3][1] == 1:
    a4_initial_d += 1
    b1_region_asians += 1
    c2_hair_brown += 1
    d4_accessories_hats += 1
    e1_feature_rosey += 1
  if names[3][2] == 1:
    a4_initial_d += 1
    b4_region_australians += 1
    c5_hair_white += 1
    d2_accessories_rings += 1
    e5_feature_beards += 1
  if names[3][3] == 1:
    a4_initial_d += 1
    b2_region_americans += 1
    c3_hair_blonde += 1
    d1_accessories_glasses += 1
    e2_feature_noses += 1
  if names[3][4] == 1:
    a4_initial_d += 1
    b3_region_europeans += 1
    c4_hair_ginger += 1
    d3_accessories_wigs += 1
    e4_feature_braces += 1

  # Fifth row of characters
  if names[4][0] == 1:
    a5_initial_e += 1
    b1_region_asians += 1
    c3_hair_blonde += 1
    d5_accessories_makeup += 1
    e5_feature_beards += 1
  if names[4][1] == 1:
    a5_initial_e += 1
    b2_region_americans += 1
    c4_hair_ginger += 1
    d1_accessories_glasses += 1
    e3_feature_moustaches += 1
  if names[4][2] == 1:
    a5_initial_e += 1
    b3_region_europeans += 1
    c1_hair_black += 1
    d4_accessories_hats += 1
    e2_feature_noses += 1
  if names[4][3] == 1:
    a5_initial_e += 1
    b5_region_africans += 1
    c5_hair_white += 1
    d2_accessories_rings += 1
    e4_feature_braces += 1
  if names[4][4] == 1:
    a5_initial_e += 1
    b4_region_australians += 1
    c2_hair_brown += 1
    d3_accessories_wigs += 1
    e1_feature_rosey += 1

  # Displays all attrubutes for the user to see
  print(str_format)
  print("Remaining Character Attribution Stastics!".center(44))
  print()

  # Displays first category's statistics
  print('Character Initials:'.center(44))
  print(f'Initial A. - {a1_initial_a} Characters')
  print(f'Initial B. - {a2_initial_b} Characters')
  print(f'Initial C. - {a3_initial_c} Characters')
  print(f'Initial D. - {a4_initial_d} Characters')
  print(f'Initial E. - {a5_initial_e} Characters')
  print()

  # Displays second category's statistics
  print('Character Regions:'.center(44))
  print(f'Asians - {b1_region_asians} Characters')
  print(f'Americans - {b2_region_americans} Characters')
  print(f'Europeans - {b3_region_europeans} Characters')
  print(f'Australians - {b4_region_australians} Characters')
  print(f'Africans - {b5_region_africans} Characters')
  print()

  # Displays third category's statistics
  print('Character Hair Colors:'.center(44))
  print(f'Black Hair - {c1_hair_black} Characters')
  print(f'Brown Hair - {c2_hair_brown} Characters')
  print(f'Blonde Hair - {c3_hair_blonde} Characters')
  print(f'Ginger Hair - {c4_hair_ginger} Characters')
  print(f'White Hair - {c5_hair_white} Characters')
  print()

  # Displays fourth category's statistics
  print('Character Accessories:'.center(44))
  print(f'Glasses - {d1_accessories_glasses} Characters')
  print(f'Rings - {d2_accessories_rings} Characters')
  print(f'Wigs - {d3_accessories_wigs} Characters')
  print(f'Hats - {d4_accessories_hats} Characters')
  print(f'Makeup - {d5_accessories_makeup} Characters')
  print()

  # Displays fifth category's statistics
  print('Character Facial Features:'.center(44))
  print(f'Rosey Cheeks - {e1_feature_rosey} Characters')
  print(f'Big Noses - {e2_feature_noses} Characters')
  print(f'Moustaches - {e3_feature_moustaches} Characters')
  print(f'Braces - {e4_feature_braces} Characters')
  print(f'Beards - {e5_feature_beards} Characters')


# Functions allows user to check individual character statistics
def character_profile():
  print(str_format)
  profile_selection = input('Which Character Would You Like To Profile? ')  # Asks user for a character's name
  char_profile = profile_selection.title()
  char_num = 0

  # Checks through the dictionary containing the information of all 25 characters for the inputed character's number placement information (placement from 1 - 25)
  for num in range(1, 26):
    curr_char = "char" + str(num)
    if characters_dict[curr_char + "_name"] == char_profile:
      char_num = num  # Updates a variable with the character's placement number

  # If a valid character name was displayed, then the program displays the attrubutes of that character
  if char_num != 0:
    print(f"Initial - {characters_dict['char' + str(char_num) + '_initial']}.")
    print(f"Region - {characters_dict['char' + str(char_num) + '_region']}")
    print(f"Hair - {characters_dict['char' + str(char_num) + '_hair']}")
    print(f"Accessory - {characters_dict['char' + str(char_num) + '_accessory']}")
    print(f"Feature - {characters_dict['char' + str(char_num) + '_feature']}")

  # If the user entered an invalid character then program tells the user to enter a valid name
  if char_num == 0:
    print("Enter A Valid/Remaining Character's Name Next Time!")


# Function allows the user to ask questions regarding the characters on the board
def asking_questions():
  print(str_format)
  print("What Category Would You Like To Ask About? ")

  # Asks the user which category they would like to ask about
  category = input("Category (Initial/Region/Hair/Accessory/Feature): ")
  asked = 0
  print()

  # For the character being guessed, the character's attrubutes are stored
  attribute_initial = characters_dict["char" + str(character_place) + "_initial"]
  attribute_region = characters_dict["char" + str(character_place) + "_region"]
  attribute_hair = characters_dict["char" + str(character_place) + "_hair"]
  attribute_accessory = characters_dict["char" + str(character_place) + "_accessory"]
  attribute_feature = characters_dict["char" + str(character_place) + "_feature"]

  # If an invalid category was entered, invalid input message comes up
  if category.title() != 'Initial' and category.title() != 'Region' and category.title() != 'Hair' and category.title() != 'Accessory' and category.title() != 'Feature':
    print("Please Select A Valid Category Next Time!")

  # If the user selected the initial category
  elif category.title() == "Initial":
    print("Which Option Would You Like To Question About? ")
    category_op = input("Category Option (A/B/C/D/E): ")  # Asks which option of the category the user wants to ask about

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    if category_op.title() == "A" and attribute_initial != "A":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_initial"] == "A":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "A" and attribute_initial == "A":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_initial"] != "A":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "B" and attribute_initial != "B":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_initial"] == "B":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "B" and attribute_initial == "B":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_initial"] != "B":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "C" and attribute_initial != "C":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_initial"] == "C":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "C" and attribute_initial == "C":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_initial"] != "C":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "D" and attribute_initial != "D":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_initial"] == "D":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "D" and attribute_initial == "D":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_initial"] != "D":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "E" and attribute_initial != "E":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_initial"] == "E":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "E" and attribute_initial == "E":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_initial"] != "E":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If an invalid option was selected, then invalid option message pops up
    else:
      print("Please Select A Valid Option Next Time!")

  # If the user selected the region category
  if category.title() == "Region":
    print("Which Option Would You Like To Question About? ")
    category_op = input(
      "Category Option (Asia/America/Europe/Australia/Africa): "
    )  # Asks which option of the category the user wants to ask about

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    if category_op.title() == "Asia" and attribute_region != "Asia":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_region"] == "Asia":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Asia" and attribute_region == "Asia":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_region"] != "Asia":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "America" and attribute_region != "America":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_region"] == "America":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "America" and attribute_region == "America":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_region"] != "America":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "Europe" and attribute_region != "Europe":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_region"] == "Europe":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Europe" and attribute_region == "Europe":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_region"] != "Europe":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title(
    ) == "Australia" and attribute_region != "Australia":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_region"] == "Australia":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title(
    ) == "Australia" and attribute_region == "Australia":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_region"] != "Australia":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "Africa" and attribute_region != "Africa":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_region"] == "Africa":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Africa" and attribute_region == "Africa":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_region"] != "Africa":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If an invalid option was selected, then invalid option message pops up
    else:
      print("Please Select A Valid Option Next Time!")

  # If the user selected the hair color category
  if category.title() == "Hair":
    print("Which Option Would You Like To Question About? ")
    category_op = input(
      "Category Option (Black/Brown/Blonde/Ginger/White): "
    )  # Asks which option of the category the user wants to ask about

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    if category_op.title() == "Black" and attribute_hair != "Black":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_hair"] == "Black":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Black" and attribute_hair == "Black":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_hair"] != "Black":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "Brown" and attribute_hair != "Brown":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_hair"] == "Brown":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Brown" and attribute_hair == "Brown":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_hair"] != "Brown":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "Blonde" and attribute_hair != "Blonde":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_hair"] == "Blonde":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Blonde" and attribute_hair == "Blonde":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_hair"] != "Blonde":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "Ginger" and attribute_hair != "Ginger":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_hair"] == "Ginger":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Ginger" and attribute_hair == "Ginger":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_hair"] != "Ginger":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "White" and attribute_hair != "White":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_hair"] == "White":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "White" and attribute_hair == "White":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_hair"] != "White":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If an invalid option was selected, then invalid option message pops up
    else:
      print("Please Select A Valid Option Next Time!")

  # If the user selected the accessory category
  if category.title() == "Accessory":
    print("Which Option Would You Like To Question About? ")
    category_op = input(
      "Category Option (Glasses/Ring/Wig/Hat/Makeup): "
    )  # Asks which option of the category the user wants to ask about

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    if category_op.title() == "Glasses" and attribute_accessory != "Glasses":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_accessory"] == "Glasses":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Glasses" and attribute_accessory == "Glasses":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_accessory"] != "Glasses":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "Ring" and attribute_accessory != "Ring":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_accessory"] == "Ring":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Ring" and attribute_accessory == "Ring":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_accessory"] != "Ring":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "Wig" and attribute_accessory != "Wig":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_accessory"] == "Wig":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Wig" and attribute_accessory == "Wig":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_accessory"] != "Wig":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "Hat" and attribute_accessory != "Hat":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_accessory"] == "Hat":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Hat" and attribute_accessory == "Hat":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_accessory"] != "Hat":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "Makeup" and attribute_accessory != "Makeup":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_accessory"] == "Makeup":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Makeup" and attribute_accessory == "Makeup":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_accessory"] != "Makeup":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If an invalid option was selected, then invalid option message pops up
    else:
      print("Please Select A Valid Option Next Time!")

  # If the user selected the facial feature category
  if category.title() == "Feature":
    print("Which Option Would You Like To Question About? ")
    category_op = input(
      "Category Option (Rosey-Cheeks/Big-Nose/Moustache/Braces/Beard): "
    )  # Asks which option of the category the user wants to ask about

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    if category_op.title(
    ) == "Rosey-Cheeks" and attribute_feature != "Rosey Cheeks":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_feature"] == "Rosey Cheeks":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title(
    ) == "Rosey-Cheeks" and attribute_feature == "Rosey Cheeks":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_feature"] != "Rosey Cheeks":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "Big-Nose" and attribute_feature != "Big Nose":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_feature"] == "Big Nose":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Big-Nose" and attribute_feature == "Big Nose":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_feature"] != "Big Nose":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title(
    ) == "Moustache" and attribute_feature != "Moustache":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_feature"] == "Moustache":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title(
    ) == "Moustache" and attribute_feature == "Moustache":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_feature"] != "Moustache":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "Braces" and attribute_feature != "Braces":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_feature"] == "Braces":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Braces" and attribute_feature == "Braces":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_feature"] != "Braces":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If the attrubute is not the same, then all characters with the attrubute option get removed from the board user
    elif category_op.title() == "Beard" and attribute_feature != "Beard":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_feature"] == "Beard":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Not Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1
    # However if inputed attrubute is the same as the character being guessed, then all other characters with other attrubute options get removed from the board
    elif category_op.title() == "Beard" and attribute_feature == "Beard":
      for num in range(1, 26):
        curr_char = "char" + str(num)
        if characters_dict[curr_char + "_feature"] != "Beard":
          char_num_list[characters_dict[curr_char + "_row"]][characters_dict[curr_char + "_col"]] = 0
      print("Character Does Have The Attribute!")
      print(f"Your On Question/Guess {questions_asked+1}!")
      asked += 1

    # If an invalid option was selected, then invalid option message pops up
    else:
      print("Please Select A Valid Option Next Time!")

  return asked  # Returns the value 1 if a question was asked, otherwise for invalid options the returned value would be 0


# Functions allows user to guess characters
def character_guess(names):
  print(str_format)
  name_selection = input('Which Character Would You Like To Guess? ')  # Asks for input for the character being guessed
  char_name = name_selection.strip()
  char_name = name_selection.title()
  asked = 1

  # If the character being guessed is no the correct character, the guessed character would be removed from the board
  # If guessed character is on the first row
  if char_name == names[0][0] and char_name != character_picked:
    char_num_list[0][0] = 0
  elif char_name == names[0][1] and char_name != character_picked:
    char_num_list[0][1] = 0
  elif char_name == names[0][2] and char_name != character_picked:
    char_num_list[0][2] = 0
  elif char_name == names[0][3] and char_name != character_picked:
    char_num_list[0][3] = 0
  elif char_name == names[0][4] and char_name != character_picked:
    char_num_list[0][4] = 0

  # If guessed character is on the second row
  elif char_name == names[1][0] and char_name != character_picked:
    char_num_list[1][0] = 0
  elif char_name == names[1][1] and char_name != character_picked:
    char_num_list[1][1] = 0
  elif char_name == names[1][2] and char_name != character_picked:
    char_num_list[1][2] = 0
  elif char_name == names[1][3] and char_name != character_picked:
    char_num_list[1][3] = 0
  elif char_name == names[1][4] and char_name != character_picked:
    char_num_list[1][4] = 0

  # If guessed character is on the third row
  elif char_name == names[2][0] and char_name != character_picked:
    char_num_list[2][0] = 0
  elif char_name == names[2][1] and char_name != character_picked:
    char_num_list[2][1] = 0
  elif char_name == names[2][2] and char_name != character_picked:
    char_num_list[2][2] = 0
  elif char_name == names[2][3] and char_name != character_picked:
    char_num_list[2][3] = 0
  elif char_name == names[2][4] and char_name != character_picked:
    char_num_list[2][4] = 0

  # If guessed character is on the fourth row
  elif char_name == names[3][0] and char_name != character_picked:
    char_num_list[3][0] = 0
  elif char_name == names[3][1] and char_name != character_picked:
    char_num_list[3][1] = 0
  elif char_name == names[3][2] and char_name != character_picked:
    char_num_list[3][2] = 0
  elif char_name == names[3][3] and char_name != character_picked:
    char_num_list[3][3] = 0
  elif char_name == names[3][4] and char_name != character_picked:
    char_num_list[3][4] = 0

  # If guessed character is on the fifth row
  elif char_name == names[4][0] and char_name != character_picked:
    char_num_list[4][0] = 0
  elif char_name == names[4][1] and char_name != character_picked:
    char_num_list[4][1] = 0
  elif char_name == names[4][2] and char_name != character_picked:
    char_num_list[4][2] = 0
  elif char_name == names[4][3] and char_name != character_picked:
    char_num_list[4][3] = 0
  elif char_name == names[4][4] and char_name != character_picked:
    char_num_list[4][4] = 0

  # If guessed character is the correct character slected to be guessed, then the game ends
  elif char_name == character_picked:
    # Displays messages of player score (score is number of guesses/questions taken)
    print('You Guessed The Correct Character!')
    print(f"You Guessed In {questions_asked+1} Question(s)/Guess(es)!")

    # Ends the game loop
    global game_run
    game_run = False
  else:  # If a valid character name was not given, then invalid message is displayed
    print("Please Enter A Valid Name Next Time!")
    asked -= 1  # No guess was made, so score should not go up

  # If guess was not correct, game continues and number of guesses/questions is displayed
  if char_name != character_picked:
    print(f"Incorrect Guess! Your On Question/Guess {questions_asked+1}!")

  return asked  # Returns 1 if a guess was made, and 0 if there was a invalid input made by the user


# Game setup functions are called and score variables are set
intro()
character_lists()
game_loop()
character_selection()
score = 100  # The score is better if it is a lower number, so a defult value of 100 is assigned
questions_asked = 0  # Declares variable that keeps track of questions/guesses asked by user

# Game loop, if game is not done the game continues
while game_done == False:
  if game_run == True:  # If the game is on, the program continues
    # Displays the board characters and presents game options to user
    board_display(char_num_list, characters)
    game_option = menu_options()

    # If the game option selected was 1, overall attrubutes are displayed
    if game_option == 1:
      attrubute_stats(char_num_list)

    # If the game option selected was 2, individual character attrubutes are displayed
    elif game_option == 2:
      character_profile()

    # If the game option selected was 3, user gets to propose a question about the character choosen to be guessed
    elif game_option == 3:
      questions_asked += asking_questions()

    # If the game option selected was 4, user gets to guess the character choosen to be guessed
    elif game_option == 4:
      questions_asked += character_guess(characters)

    # If the game option selected was 5, user selected to exit the program and so the game program ends
    elif game_option == 5:
      print(str_format)
      print("Thank You For Playing Guess Who!".center(44))

      # If the user exited on their first time playing, no previous score is avaliable
      if score == 100:
        print(f"Score Unavaliable!".center(44))
      # If the user had played a previous game, the previous best score/lowest score is shown
      else:
        print(f"Your Score Is {score}!".center(44))
      # Game loop ends
      game_done = True

  # If the game is ended, the user gets an option to restart the game and try to get a better score
  else:
    print(str_format)
    should_restart = input("Would You Like To Play Again (Yes/No)? ")  # Ask the user if they would like to restart
    response = should_restart.title()

    # If their game score is better/lower than the previous score, the score gets changed to the better/lower score
    if score > questions_asked:
      score = questions_asked

    # If the user wishes to replay the game, the game variables and game gets reset
    if response == 'Yes':
      # Visual formatting
      print(str_format)
      print("\n\n")

      # Resets game loop and recalls resetting functions
      intro()
      restart_game()
      game_run = True

    # if the user does not wish to play again, the game program ends
    elif response == 'No':
      # Game ending messages
      print(str_format)
      print("Thank You For Playing Guess Who!".center(44))
      print(f"Your Score Is {score}!".center(44))
      game_done = True  # Game loop ends
    else:
      print("Please Respond With 'Yes' Or 'No'!")  # If the user did not ask yes or no, invalid message gets displayed

  # If the game exceeds the question/guess capacity, the game by default ends
  if questions_asked > 99:
    print(str_format)
    print("GAME OVER!!".center(44))  # Game over text
