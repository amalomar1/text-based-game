
# TO PLAY GAME USE run() FUNCTION:

import sys
import os
import random
import time

def run():
    title_screen()



# Welcome Screen & END:

def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        start_game()
    elif option.lower() == "credits":
        credits()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ["play", "quit", "credits"]:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == "play":
            start_game()
        elif option.lower() == "credits":
            credits()
        elif option.lower() == "quit":
            sys.exit()

def title_screen():
    os.system("clear")
    print("########################################")
    print("########################################")
    print("###                                  ###")
    print("###    Welcome to Salmesbury Hall    ###".upper())
    print("###                                  ###")
    print("########################################")
    print("########################################")
    print("")
    print("                - Play -                ")
    print("               - Credits -              ")
    print("                - Quit -                ")
    print("")
    print("           Built by Team 1!             ")
    print("")
    title_screen_selections()

def credits():
    print("########################################")
    print("########################################")
    print("###                                  ###")
    print("###          Team 1: Credits         ###".upper())
    print("###                                  ###")
    print("########################################")
    print("########################################")
    print("")
    print("     Amal          |     Act 3          ".upper())
    print("     Constance     |     Act 4          ".upper())
    print("     John          |     Act 2          ".upper())
    print("     Pawel         |     Act 5          ".upper())
    print("     Ricardo       |     Act 1          ".upper())
    print("")
    input("---Press ENTER to Return to Main Screen---")
    title_screen()

def end():
    print("########################################")
    print("########################################")
    print("###                                  ###")
    print("###               End                ###".upper())
    print("###                                  ###")
    print("########################################")
    print("########################################")
    input("---Press ENTER to Return to Main Screen---")
    title_screen()

def start_game():
        act_1_1()

# Endings:

def neighbour_ending():
    print("You post the letter through your neighbours letter box, no one likes her anyway.")
    print("One month later you notice missing persons posters showing your neighbours face around town.")
    print("There's a loud knock at your door...")
    print("GAME OVER")
    print("")
    ntryagain = input("Try again? (y/n)")
    if ntryagain.lower() == "y":
            act_1_1()
    elif ntryagain.lower() == "n":
            sys.exit
    while ntryagain.lower() not in ["y", "n"]:
        print("Please enter a valid command.")
        ntryagain = input("Try again? (y/n)")
        if ntryagain.lower() == "y":
            act_1_1()
        elif ntryagain.lower() == "n":
            sys.exit

def boring_ending():
    print("You throw away the letter and get on with your life.")
    print("More and more missing persons posters spring up across town in the coming years, always around Oct 31.")
    print("GAME OVER")
    print("")
    btryagain = input("Try again? (y/n)")
    if btryagain.lower() == "y":
            act_1_1()
    elif btryagain.lower() == "n":
            sys.exit
    while btryagain.lower() not in ["y", "n"]:
        print("Please enter a valid command.")
        btryagain = input("Try again? (y/n)")
        if btryagain.lower() == "y":
            act_1_1()
        elif btryagain.lower() == "n":
            sys.exit

def go_home_ending():
    print("Feeling unnerved you decide to go home, what were you thinking coming here anyway!")
    print("As you turn to leave you notice that the lights and shadows have stopped")
    print("You see the odd man from earlier stood in a window of the manor. His face is pale, his expression furious")
    print("He didn't like that...")
    print("GAME OVER")
    print("")
    gtryagain = input("Try again? (y/n)")
    if gtryagain.lower() == "y":
            act_1_2()
    elif gtryagain.lower() == "n":
            sys.exit
    while gtryagain.lower() not in ["y", "n"]:
        print("Please enter a valid command.")
        gtryagain = input("Try again? (y/n)")
        if gtryagain.lower() == "y":
            act_1_1()
        elif gtryagain.lower() == "n":
            sys.exit

def peak():
    print("You approach the window and peer inside, as you get closer you are met with a staring unblinking pair of eyes!")
    print("Red tears are flowing from the unsettlingly familiar eyes!")
    print("""   
     ........                                                         .:~!7JJJ?!~:.           
     :~?YGB##&&&####BGP5J?!^:.                                       .^!?5GB&@@@@@@@@@@@#BPJ!^.     
   .:~!!!!!7??JYYY55PPGB#&&@@&B5?~:.                            :~?YG#@@@@@&#BGP5YJ??7!!!!7?JJ?!^   
                         .^!?5G#&#GYJ!.                     ^7YPB&@@@&B5?!^.                    .   
                               .~JG#BG5?.                  YP5G#&#P?~.    ..::::..                  
              :~~!7?77!7?!!!^:.    ^JGPPP:                Y#GBPJ^.   .^!7!!7!~~?!!7!~:.             
          .^!!!?J~~J7J!JY~7!^??77^.  .!P#5::             7@#J:    :~~7:.7~^JY!!5^:.:!?77.           
        .:^^~~~J5Y5GGY???JPGP5~!^^77:   ^!.J            :#Y.    ^!!^:!PPY?7!~~7JPB555??^....        
        .^?Y5Y!::J?:     ~^7PPJJ??!^!!:    J^           Y7    .~^~755GP^         ^5!:?5Y?~:         
     :~75PJ^.  .P!   :7JJY:^7:5^.~Y5!^~.   7!          :J      .!5J^JY    ^?Y7.   .G:  ^557^.       
      :^:!!:   !P    G@@@&^:  !P   JYY~  :.!!          ^~..   ~Y5: .#:    B@@@Y    G~   :55?~.      
          ^JJ^^~G^   ~5G5~    ?Y  .7~^?J  ^!~          .:~  :J?~?:  PJ    ^JY?:   !P:^^?Y~          
          :?.:~J7PJ^.       .?5^:^7?~~~5   ~:           ::  JJ^~7?^:~P5!.       :JP~J!^.!~          
          7:^!7!!!Y5J??!!!7J5J77!~?^:~^7:                  .?^~::7~~!7?P5Y7~!~~?55!!!!!!.J          
          J:?..~: ^!?7~?:?~!:~~^7!^~  !^7                  ~!!. ^!^?^~~:^~7^!!!?!! :^. ?:J.         
          ?:7.     ?:^7. : .  . .?^!  ~^?.                 ?:!  ^~7^ .  . :  !~.?.     ?.J          
          !~^!    .7:7           ?~!  :~!^                .?^~  :!?.          !^~^    ^!:?          
          :? ?    !^7:           !!7   7^7                ~!!:  !!?            ?:7    7.!!          
           J 7:   7:?.            7?^  7^?                !~7  :??.            ?.?   .? J:          
           ?^~~   7:7^             ??: 7~?                !!7 .?J:            .? ?   :7.J           
           ~7:7   !~.?             :?7.7!!                ^77 7?~     .       !~.7   ~~^7           
           :J.?   :? 7^             ?~!7!~                :?!!~?.            .? !^   !:7~           
            J ?    7::?             !~??7^                .?!Y:7             !~ ?    7.?:           
            J 7^   ^! ?:            ^!!!?:                 J^?^!             ? :7   .? ?:           
           .J J?   ^7 ^!            ^7 .J                  ?: ~!            ^! ~!   !5.7^           
           ~7.JJ~  !J7.?            ^7 :?                  !! ^!            !^~Y7  :JJ^^7           
           ?:7~7? .?7?:?            ~! !!                  ^? :7            !^77?^ 7?^? J           
          .J:? !J^^?!~~?            !~ ?^                  .J :?            !!!^7!.J7 !!7~          
          7~?: ^?7~7!^!?            7^ J.                   J..?            !!!^7!~?~  J^J          
         .J!7   ??~7!~~?            7^ J                    ?^ ?            7~7!!!7?:  ^77^        
    """)
    go_home_ending()


# Act 1 - The Journey:

def mash_pad():
    mash = random.randint(0,200)
    code = 195
    guesses = 0
    while mash != code:
        print(mash)
        mash = random.randint(0,200)
        guesses += 1
    print("")
    print(f"You finally enter {code}! It took you {guesses} guesses and only 2 hours, yay!")
    enter()

def enter():
    print("The keypad bleeps, and the door creaks open slowly.")
    input("Press ENTER to continue")
    act_1_4()

def act_1_1():
    print("""
    You wake up to loud banging at your front door. 
    You sluggishly answer the door and find a pale man holding an envelope.
    
    His hand trembles as you take the letter, his smile never reaches his eyes. 
    He nods and walks away.

    You slowly tear open the envelope and find a damaged and worn letter, you are 
    clearly not the first person this has been given to.
    
    The letter reads:

                You are invited to Salmesbury Hall to attend our annual
                'All Hallows' Eve' party.

                Your code is: 19'S'

    The final digit is smeared with what you hope is ketchup...looks like an 'S'?
    
    Option a: Go to the party, what's the worst that could happen?
    Option b: Post the letter in a neighbours letter box. 
    Option c: Throw away the letter and get on with your life.    
    """)
    first_choice = input("Will you go to the odd man's halloween party? (a/b/c)")
    print("")
    if first_choice.lower() == "a":
        act_1_2()
    elif first_choice.lower() == "b":
        neighbour_ending()
    elif first_choice.lower() == "c":
        boring_ending()
    while first_choice.lower() not in ["a", "b", "c"]:
        print("Please enter a valid command.")
        first_choice = input("Will you go to the odd man's halloween party? (a/b/c)")
        if first_choice.lower() == "a":
             act_1_2()
        elif first_choice.lower() == "b":
            neighbour_ending()
        elif first_choice.lower() == "c":
            boring_ending()

def act_1_2():
    print("")
    print("You arrive at the gates to Salmesbury Hall and are greeted by the sight of a grand and unsettling manor")
    print("""

                                                                       .                                
                                                                  ~Y                                
                                                                  5G:                               
                                                                 7YJ?                               
                                                                77Y7?^                              
                                                               !Y^P~?J                              
                                                              7JJ~B~7~!                             
                                                             ?5JJ7P.?:J.                            
                                                            J5JG~JP~J:^7                            
                                                          :YY?5Y~JG:7~ J^                           
                                                         ^5YJYJ!~7G.~7:?5                           
                                                       .7Y!7J~!:!~P!~? ~Y!                          
                                                      ^?J~!!!.~^!7?^ !:^?7^                         
                                                    :!!~.?~7~~^!??7!~!~.?:J.                        
                                                  :??!!~7!!Y?!7?7J~JY7?~!^^7                        
                                                  ~?7!~7J~^^:.  .? ..~77JJ~5!                       
                                                       J.   ^^: :?      J!^~^                       
                                  ::.                  ?: :777!~.? .!?!.?                           
                             ^^^~!!Y!!~^~              ?: ?:^! ?:? ?:?7?!                           
                            :?~^^^~J!~!^J              ?: J!7J~J^7.Y!Y?Y:                           
                            7!?^7^!??.?.?.             7: ?:^7 ?:7^!~!JY                            
                           :?.7 ? 7!Y:?:7~             7^ ~!!7~7:7:7?!Y7                            
                           ?~?7~?:J~J:!7.J             7^  :~^. ^7 .. 7^                            
                          77.J ?:77?77 J.~!:!^         7^ !~J^7.^7!J?^?.                            
                         ~7:?~!!^J:J^7.!! 7P!~!        7^:? ? ^7:Y!7^Y?:~~:.                        
                        ^J.7::~.J7:7^^~.~^7J7 ^7:      !^^J^Y~!7:5?J7GJ^~Y77?7!                     
                       ^7^!7~!?~~!!JJ!J7!Y? J.  ~!:    !^^7 J ~!^Y!7~G?:^! !:7?                     
                      ~Y!??!J~7~:J^^:~~:75. 7~:~^^~!^. !^.?^J^7:^?7?75J^~?^J^JJ.                    
                      !!~~7J^!7~ ?: ^7!^?: .JJ:..^. ^~~?! ..    ~7.^75~ ^7.J.Y5!                    
                          .?7^?:7?::7~~J~  ?:~~   ! ..^^^!~~~!777Y7!~Y~:~7:Y.?JY:                   
                          .JJ:Y^JJ.~7?5~  7^  ?..^~?~^:! :!  7^.:7 J.~7 7~^?:!7Y?:                  
                           JY^J.?Y.~!77  7~   :?~:.7:  ~~ 7?^~7 .?.~!7P J::~ :^:77:                 
                           ??~?~7J.:Y!  7~     !!  .?.::J!.J: 7!~!7!77J??!~7!^!~~?Y!.               
                           7::~^ ?:~!  7~       7^:~!J^..7 .7:!!7^~~7J.Y~~7J!Y?7Y77J~               
                           !77?!7J?!  7^         J7  !! .7?:!777!J!J7~ 7:   .:.^J^                  
                           ~Y~7~7G~ .?: .~!!~:   .?:  7J~:?7 .?^?!J~J  ^?  :~~. ?.                  
                           ^57!JJ^ :?:.JJ?G7!JY:  .?^!^?~  ?^ ^!~?~7J7?~J.^7?~?.J                   
                           :Y7~J. ^?. 5! :P^  7P.  .J^  7~ :J^~!!::G~!~?J!!!J^J^?                   
                  ^!:..    .J?7  ~7  ~Y  .G^   G^   .?^ .7J^.J~^. JP 7:!?JY~J:J~7                   
                 .?.:^!~~~~!Y:  !!   !Y::~G7^^^G:     7~!.~! .7~:7Y?^Y!77!5^J.?!~                   
                .?~^ ^:~:~J7  .7^    7P!!7B?!!!G.      !!  :7!.7!7~7.J:~!~~J^^:7^                   
               .?: :!. .7:^!~^??     !Y   G^  .P        ~7 .~!: ??^!7?!7!~77!  ?:.^.                
              :?~.~7~:^7: ~^ .^?:    ~P   G^  ^5   ..... :?!. :^^7^ :?^:7~ 7??~?~~~?                
             ~7 :J!  !!.~7::!!^^Y    :5~^^5!^^7!   .:::.  ??~^::~.:^^.77.!!~?!7!.~:~7               
           .77^~7~^:?7:~?~ :7..?~7::. .....^^......::::...? :^^~~~~~~^^7~:7!:!~55~?^?~              
          ~!.:7^  !!..?~..~J: !!^?JJ^!~^~^~^J.     ....  ^7  ...:::.  ...::7?!?~7!~J 7^             
        ^?7:~~~^^7^ ^7:  !!.:!Y7~:!7~ ~^.~.~!7  ...::::. 7^.::::..       ::J!::7 ?~:?:Y^            
      ^7^:~^  :~::^~~^.:7!  !Y~.~!. ~?!^?!77~Y7   ..... :?  ..P?7!!!^^^:::7J:J^?7^?:!7:7^           
    .?J7^!J~^!J~:^?^.:~~...77.:7^    :7^.!!!!!JJ^  .....?.    Y?~~ :!.^!:~^YY:7~7^:7:^~:J!          
        . ^J::^^^^:::^^:~?7. !!        ~!:^!~!!7?7^    ^?     ?:?J7::7~!!~7~??~~^~^^^^^J!!.         
           ?:          !?~.^7:          .~!^!^!!~77?~   J...  7: !!!77!~:?7!!~!^      .?            
           ^? .........:::^Y.  .~?J???7~   ~J^!~^^J~~:.^7 .   7^  ^!!!^^77!!!??!7Y!^^7!~            
            J..J^^^77^^^7: ?: ~PJ:J. J~J5. !!^^^.~!    ~!     ~!    ~?!?7~~^77~~!7??^??.            
            ?^.J:. ~7   7^ 7^ P5^ ?: ?. 5J J^~~^.J.    ^!     ^7     J:^~~~~~~~^~Y!!7J?             
            !~ 77^^!J^~^J^ !~.G!~ 7^ ?. !P:?.^^.:? .::.~7 .:. :? ....?~7:^~?:^^7Y7..~??             
            !~ ~?..^J.. ?^ ~!:P!~ !~ ?. !G~7^^:.^7    .?.     .? ....?!! .^J..^Y?::::^?             
            ?^.:~~^^~^^^~. ^7^G!~ ~! ?.!?P~7:^^::?    ^7       J... .?!7^^~J::!G~....^?             
           .Y~^:......     :7^G!~ ^7 ?..!G~7.^^^.J:...^7.::....J:.  .?~7::~?^^!P^^^^^^^             
            ::::^^^^^^^~~~~77:G!~ :? ?. !P:?.:^~^!?:^^!?.::^^^^J~^::^J.^^^^^^^^J.                   
                           ^7^B7! :J J: 7G.J..^~~~!^^^^~^^:::::::::^^~^^^::::::.                    
                           .^^!~~^^!^!~^!?~7~^:. 
    """)
    print(""" 

There is something strange about this place - there are lights on and shadows moving but no sounds.
No music.
No laughter.
    
Option a: You go to the door, you've come this far why stop now?
Option b: Take a peak inside a window, what if you're the only one in a costume?!
Option c: Go home, this is crazy.
    """)
    second_choice = input("What do you do? (a/b/c)")
    print("")
    if second_choice.lower() == "a":
        act_1_3()
    elif second_choice.lower() == "b":
        peak()
    elif second_choice.lower() == "c":
        go_home_ending()
    while second_choice.lower() not in ["a", "b", "c"]:
        print("Please enter a valid command.")
        second_choice = input("What will you do? (a/b/c)")
        if second_choice.lower() == "a":
             act_1_3()
        elif second_choice.lower() == "b":
            peak()
        elif second_choice.lower() == "c":
            go_home_ending()

def act_1_3():
    print("")
    print("You approach the front door and notice a keypad on the lock, from the letter you recall that the code starts with '19#'.")
    print("""
    
    Option a: You mash the keypad and let fate take the wheel.
    Option b: You enter 1 and 9 and take a guess on the last digit.
    """)
    third_choice = input("Which do you choose? (a or enter the last digit)")
    if third_choice.lower() == "a":
        mash_pad() 
    elif third_choice.lower() == "5":
        enter()
    while third_choice.lower() not in ["a", "5"]:
        print("Please enter a valid command.")
        third_choice = input("Which do you choose? (a or enter the last digit)")
        if third_choice.lower() == "a":
            mash_pad() 
        elif third_choice.lower() == "5":
            enter()

def act_1_4():
    print("""
:^^::..::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..::
  .:^^:::.::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.:::^^:  
      .:^^::.::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.::^^:.      
         .:^^:::.::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..::^^:.         
            ..:^^::.:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..::^^:..            
                .:^^::..::::::::::::::::::::::::::::::::::::::::::::::::::::..::^^:.                
                   .:^^^::.::::::::::::::::::::::::::::::::::::::::::::::.::^^^:.                   
                      .:^^^::..::::::::::::::::::::::::::::::::::::::..::^^^:                       
                          .:^^^:..::::::::::::::::::::::::::::::::..::^^:.                          
  :Y?~:                      .:^^^::::::::::::::::::::::::::::::::^^^:.                      :~?5^  
  ^Y!JY5J7^.                     .^~^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~.                     .^7YP5J7J~  
  ^J:::^!JY55J!^.                 ^^                            ^^                 .^!J5PY?!^:::?~  
  ^J::::::::^!?555J!:             :^                            ^^             :~J5P5Y7~^:::::::?~  
  ^?::::::::::::^~7J55Y7^.        :^                            ^^        .^7YPP5?!^::::::::::::7~  
  ^J:::::::::::::::::^~?&7        :^                            ^:        !&J!~:::::::::::::::::?!  
  ~J::::::::::::::::::::B7        :^                            ^^        !&^:::::::::::::::::::?!  
  ^J::::::::::::::::::::B7        :^     .?!!!!!!!!!!!!!!J:     ^^        !&^:::::::::::::::::::7!  
  ^?:::::::::::::::::::^&!        :^     ^5::^^^::^^:::^:5!     ^^        7#^:::::::::::::::::::7!  
  ^?:::::::::::::::::::^&!        :^     ^5::::::::::::::5~     ^^        7#^:::::::::::::::::::7!  
  ~?:::::::::::::::::::~@?        :^     ^5::::::::::::::5~     ^:        ?#^:::::::::::::::::::?!  
  ^?:::::::::::::::::::^&?        :^     ^Y::::::::::::::5~     ^:        ?B::::::::::::::::::::7~  
  ^7:::::::::::::::::::^&7        :^     ^5::::::::::::::5~     ^:        ?B::::::::::::::::::::7~  
  ~?:::::::::::::::::::^#?        :^     ^5::::::::::::::5~     ^:        ?B::::::::::::::::::::7~  
  !?::::::::::::::::::::#J        :^     ^Y::::::::::::::5~     ^:        ?B::::::::::::::::::::?!  
  ~7:::::::::::::::::^^:#J        :^     ^Y^7::::::::::::P~     ^^        JB:^^:::::::::::::::::7~  
  ~7:::::::::::::::::P!:PJ        :^     :5^J::::::::::::P~     ^^        J#:~G^::::::::::::::::7~  
  ~?:::::::::::::::::P!:PY        :^     :Y:^::::::::::::5~     ^^        J#^^G^::::::::::::::::7!  
  ~?:::::::::::::::::^^:PY        :^     ^Y::::::::::::::5~     ^^        Y&^:^^::::::::::::::::7!  
  ~?::::::::::::::::::::5Y        :^     ^5::::::::::::::5!     ^^        YB::::::::::::::::::::7!  
  ~?::::::::::::::::::::5Y        :^     ^5::::::::::::::5~     ^^        YB::::::::::::::::::::7!  
  !?::::::::::::::::::::5Y        :^     ^5::::::::::::::5~     ^:        YG::::::::::::::::::::7!  
  ~?::::::::::::::::::::PY        :^     :Y::::::::::::::5~     ^:        5G::::::::::::::::::::!!  
  !7::::::::::::::::::::55       .!7^^~~^!5!!!!!!!777777!57^~~^^!!.       5P::::::::::::::::::::7!  
  7?::::::::::::::::::::Y5     :!!^:^^^^:::::::^^::::^^::::^^^:::^!!:     P5::::::::::::::::::::?!  
  77::::::::::::::::::::5P  .~7~:..................................:!7~.  55::::::::::::::::::::?!  
  77::::::::::::::::::::PP:77~. .................................... .^77:P5::::::::::::::::::::?!  
  77:::::::::::::::::::^P5~:............................................:~5Y^:::::::::::::::::::7!  
  !?:::::::::::::::::~77^. ..............................................  ^77~^::::::::::::::::77  
  !J::::::::::::::^!7~: .....................................................:~77^::::::::::::::!?  
  ~?:::::::::::^~77^. ........................................................ .^77~^:::::::::::!7  
  !?:::::::::^!!~:............................................................... :~!!^:::::::::77  
  !7::::::^~7!^. ....................................................................^!7~^::::::!7  
  !7::::^!!~: ........................................................................ :~!!^::::!7  
  !7:^~7!:. ............................................................................ .:!7!^:!7  
  ~?!7~:.....................................................................................~7!7?  
  ?7^. ...................................................................................... .:!?^ 
  7!: ............................................................................................ """)
    print("")
    print("Welcome to Salmesbury Hall...")
    print("")
    print("As you enter you hear a slam and a click behind you, you move to leave the way you came in, but its locked!")
    print("")
    print("There are three doors, left, centre and right. All have unlit torches above them.")
    print("You hear a cold voice:")
    print("")
    print("'It won't be that easy, if you ever want to leave you'll have to play my game!''")
    print("")
    print("The door to your left creaks open and a torch above the door bursts into light!")
    print("")
    print("You have no choice but to enter...")
    lstart()

# Act 2 - Left Room Mini Game:
inventory = []
explore = ""

class player(object):                         ## Defines the player as an entity/object
    name = ""
    health = 50
    attack = 12
    defence = 2 
    weapon = ""

class shadow(object):                          ## Defines the enemy as an entity/object
    name = "Shadow"
    health = 13
    attack = 6
    defence = 3
    loot = random.randint(0,3)

class skeleton(object):                          ## Defines the enemy as an entity/object
    name = "Skeleton"
    health = 13
    attack = 9
    defence = 2
    loot = random.randint(0,3)

class vampire(object):                           ## Defines the final boss as an entity/object
    name = "Vampire"   
    health = 40
    attack = 13
    defence = 2
    loot = 1

def lstart():                    ## Defines the start of the game
    character = player
    player.health = 50
    choice = input("You enter the door and a bright flash blinds you, you see a Sword and Shield on the ground. Pick them up? y/n: ")
    if choice.lower() == ("y"):
        time.sleep (0.5)
        print ("You feel a surge of energy rush through you.")
        time.sleep (0.5)
        print ("------------------------")
        print ("You have,", player.health, "health")
        print ("------------------------")
    else:
        print ("You have no other choice...")
        time.sleep (1)
        lstart() 
    print ("You look around your new surroundings, a large cavernous area with a stone and dirt")
    print ("floor. Cobwebs cover the walls nearby and from the darkness ahead you hear ominous noises.")
    input("---Press ENTER to Continue---")
    print ("You see on the ground to your left a skeleton, long since dead, with a small bottle") 
    print ("in it's hand.")
    inventory.append("a healing potion")
    print ("You found a Healing Potion!")
    input("---Press ENTER to Continue---")
    print ("From the darkness, all of a sudden a shape lashes out at you!!")
    damage = random.randint(1,6)
    player.health = player.health - damage
    print ("You take", damage, "HP of damage!!")
    battlestate(inventory)
    input("---Press ENTER to Continue---")
    print ("You gather yourself after the encounter, what is this place?")
    print ("Up ahead in the darkness a pair of torches burst into flames, enticing you further into")
    print ("this strange place.")
    input("---Press ENTER to Continue---")
    print ("You tentatively walk forwards and see a pile of bones to your left and a chest to your right.")
    input("---Press ENTER to Continue---")
    lmiddle ()
    print ("As you move past the torches, back in to the looming darkness, something lunges out")
    print ("at you again!! This time you're prepared, you evade and ready yourself for combat...")
    input("---Press ENTER to Continue---")
    battlestate(inventory)
    input("---Press ENTER to Continue---")
    print ("You begin to move forwards and from the depths of the darkness you see a pair of")
    print ("glowing red eyes...")
    print ("\033[1;31;48m⠀⠀⠀⣰⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣆⠀")
    print ("⠀⠀⣼⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣧⠀")
    print ("⠀⢰⣿⣿⡟⠈⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠁⢻⣿⣿⡆")
    print ("⠀⠘⣿⣿⡇⠀⠸⡟⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⢻⠇⠀⢸⣿⣿⠃⠀")
    print ("⠀⠀⠈⠙⠻⠦⢤⣄⣀⣙⣷⣤⡀⠀⠀⠀⠀⢀⣤⣾⣋⣀⣠⡤⠴⠟⠋⠁\033[0;0m")
    input("---Press ENTER to Continue---")
    lfinal()
    input("---Press ENTER to Continue---")
    print ("The Vampire begins to crumble into dust, it's eyes remain fixed on you the whole time.")
    print ("The bright flash of light from earlier returns, as it dissipates you are back in the first room...")
    print("")
    print("The torch above the door in the centre of the room burts into light.")
    print("You approach wearily, what is waiting for you behind the next door?")
    input("---Press ENTER to Continue---")
    cstart()

def lmiddle():
    print ("1. Search the pile of bones.")
    print ("2. Search the chest.")
    print ("3. Keep moving forwards")
    explore = input ("What do you want to do? 1,2 or 3: ")
    if explore == "1":
        print ("You walk over to the pile of bones and kneel down, searching through the pile gently.")
        reward = loot(inventory)
        print ("You found", reward, "!!!")
        input("---Press ENTER to Continue---")
        print ("You turn towards the chest, but it is no longer there...")
        print ("You decide to move on further into the darkness")
    elif explore == "2":
        print ("You walk over to the chest, and as you arrive you hear a click...")
        input("---Press ENTER to Continue---")
        print ("A burst of energy fires out from a small hole in the wall above the chest and hits you")
        print ("in your chest. It sends you falling backwards into the pile of bones, destroying any")
        print ("loot within...")
        damage = player.health - random.randint(1,5)
        player.health = player.health - damage
        print ("You lost", damage, "HP!")
        input("---Press ENTER to Continue---")
        print ("You decide to move on further into the darkness")
    elif explore == "3":
        print ("You decide to move on further into the darkness")
    else:
        lmiddle()

def lfinal():
    print ("The eyes grow in size as walking from the darkness, red eyes fixed on you, you see a", vampire.name)
    input("---Press ENTER to Continue---")
    enemy = vampire
    while enemy.health > 0:
        choice = input("What do you want to do? \n1.Attack\n2.Defend\n3.Use Healing Potion\n4.Flee\nChoose 1, 2, 3 or 4: ")
        time.sleep (0.5)
        if choice == "1":
            print ("----------")
            print ("You swing at the", enemy.name, "with your sword")
            time.sleep (0.5)
            hitChance = random.randint(1,10)
            if hitChance > 2:
                playerDamage = player.attack / enemy.defence
                playerDamage = round(playerDamage)
                enemy.health = enemy.health - playerDamage
                if enemy.health < 0:
                    enemy.health = 0
                print ("You cut the", enemy.name, "for", playerDamage, "points of damage!!! \nThe", enemy.name, "now has", enemy.health, "HP")
                print ("----------")
                time.sleep (0.5)
                if enemy.health > 0:
                    enemyHitChance = random.randint(1,10)
                    if enemyHitChance > 4:
                        damage = enemy.attack / player.defence
                        damage = round(damage)
                        player.health = player.health - damage
                        print ("The ", enemy.name, "lashes out at you dealing", damage, "HP of damage")
                        time.sleep (0.5)
                        gameOver()
                        print ("Your HP is now ", player.health)
                        print ("----------")
                        time.sleep (0.5)
                    else:
                        print ("The", enemy.name, "swung at you, but missed!")
                        time.sleep (0.5)
                else:
                    print ("You have killed the", enemy.name)
                    lootDrop = loot(inventory)
                    time.sleep (0.5)
                    print ("The", enemy.name, "dropped", lootDrop)
                    print ("----------")
            else:
                print ("You swing and miss the", enemy.name)
                print ("----------")
                time.sleep (0.5)
                enemyHitChance = random.randint(1,10)
                if enemyHitChance > 4:
                    damage = enemy.attack / player.defence
                    damage = round(damage)
                    player.health = player.health - damage
                    print ("The ", enemy.name, "lashes out at you dealing", damage, "HP of damage")
                    time.sleep (0.5)
                    gameOver()
                    print ("Your HP is now ", player.health)
                    print ("----------")
                    time.sleep (0.5)
                else:
                    print ("The", enemy.name, "swung at you, but missed!")
                    time.sleep (0.5)
        elif choice == "2":
            print ("----------")
            print ("You try to defend yourself!")
            time.sleep (0.5)
            enemyHitChance = random.randint(1,10)
            if enemyHitChance > 4:
                damage = enemy.attack / player.defence
                damage = round(damage)
                player.health = player.health - damage
                print ("The ", enemy.name, "lashes out at you dealing", damage, "HP of damage")
                time.sleep (0.5)
                gameOver()
                print ("Your HP is now ", player.health)
                print ("----------")
                time.sleep (0.5)
            else:
                print ("The", enemy.name, "swung at you, but missed!")
                time.sleep (0.5)
        elif choice == "3":
            useItem(inventory)
            enemyHitChance = random.randint(1,10)
            if enemyHitChance > 4:
                damage = enemy.attack / player.defence
                damage = round(damage)
                player.health = player.health - damage
                print ("The ", enemy.name, "lashes out at you dealing", damage, "HP of damage")
                time.sleep (0.5)
                gameOver()
                print ("Your HP is now ", player.health)
                print ("----------")
                time.sleep (0.5)
            else:
                print ("The", enemy.name, "swung at you, but missed!")
                time.sleep (0.5)
        else:
            print("You try to flee, but there's nowhere to go...")
            time.sleep (0.5)


def gameOver():                    ## Defines what to do when HP drops below 0 - Runs after each time player takes damage
    if player.health <= 0:
        print ("You have died, the house has claimed another soul...")
        print ("----------")
        time.sleep (0.5)
        playAgain = input ("Would you like to try again? Y/N:")
        if playAgain.lower() == "y":
            lstart()
        else:
            print ("----------")
            print ("Thank you for playing!")
            time.sleep (2)
            quit()

def cgameOver():                    ## Defines what to do when HP drops below 0 - Runs after each time player takes damage
    if player.health <= 0:
        print ("You have died, the house has claimed another soul...")
        print ("----------")
        time.sleep (0.5)
        playAgain = input ("Would you like to try again? Y/N:")
        if playAgain.lower() == "y":
            cstart()
        else:
            print ("----------")
            print ("Thank you for playing!")
            time.sleep (2)
            quit()

def rgameOver():                    ## Defines what to do when HP drops below 0 - Runs after each time player takes damage
    if player.health <= 0:
        print ("You have died, the house has claimed another soul...")
        print ("----------")
        time.sleep (0.5)
        playAgain = input ("Would you like to try again? Y/N:")
        if playAgain.lower() == "y":
            rstart()
        else:
            print ("----------")
            print ("Thank you for playing!")
            time.sleep (2)
            quit()

def healthCheck():
    if player.health < 10:
        ouch = input("Would you like to us an item? Y/N: ")
        if ouch.lower() == "y":
            useItem(inventory)
            
            
def enemyselect(shadow, skeleton):      # Randomises which enemy you encounter
    enemylist = [shadow, skeleton]
    chance = random.randint(0, 1)
    enemy = enemylist[chance]
    return enemy 

def loot(inventory):                            # Randomises the loot you receive
    loot = ["a healing potion", "a greater healing potion", "a magic orb", "nothing"]
    lootChance = random.randint(0, 3)
    lootDrop = loot[lootChance]
    if lootDrop == "a magic orb":
        lootEffect(lootDrop)
    elif lootDrop == "a healing potion":
        inventory.append(lootDrop)
    elif lootDrop == "a greater healing potion":
        inventory.append(lootDrop)
    else:
        pass
    return lootDrop

def lootEffect(lootDrop):               # If a magic orb drops, boosts your attack value
    if lootDrop == "a magic orb":
        player.attack = player.attack + 3
        print ("You feel a surge of power, your attack has increased.")
        time.sleep (0.5)

def useItem(inventory):                 # What to do if a players wants to use a potion
    print("Which item would you like to use?")
    time.sleep (0.5)
    print("----------")
    print ("1. Healing Potion: ", inventory.count("a healing potion"))
    print ("2. Greater Healing Potion: ", inventory.count("a greater healing potion"))
    print ("3. Nevermind...")
    itemChoice = input("1, 2 or 3: ")
    time.sleep (0.5)
    if itemChoice == "1":
        print ("----------")
        if inventory.count("a healing potion") > 0:
            player.health = player.health + 10
            print ("You healed 10 HP, your health is now", player.health)
            inventory.remove("a healing potion")
            time.sleep (0.5)
        else:
            print ("Sorry, you have none of those")
            time.sleep (0.5)
    elif itemChoice == "2":
        print ("----------")
        if inventory.count("a greater healing potion") > 0:
            player.health = player.health + 25
            print ("You healed 25 HP, your health is now", player.health)
            inventory.remove("a greater healing potion")
            time.sleep (0.5)

        else:
            print ("Sorry, you have none of those")
            time.sleep (0.5)
    else:
        print ("----------")
        time.sleep (0.5)


def battlestate(inventory):                  #Defines how combat proceeds
    enemy = enemyselect(shadow, skeleton)
    shadow.health = 13
    skeleton.health = 13
    if enemy == shadow:
        print (f"A ghostly Shadow moves in front of you to bar your path...")
    else:
        print (f"You see a Skeleton readying for another strike, it's eyes glow a piercing red... ")
    input("---Press ENTER to Continue---")
    while enemy.health > 0:
        choice = input("What do you want to do? \n1.Attack\n2.Defend\n3.Use Healing Potion\n4.Flee\nChoose 1, 2, 3 or 4: ")
        time.sleep (0.5)
        if choice == "1":
            print ("----------")
            print ("You swing at the", enemy.name, "with your sword")
            time.sleep (0.5)
            hitChance = random.randint(1,10)
            if hitChance > 3:
                playerDamage = player.attack / enemy.defence
                playerDamage = round(playerDamage)
                enemy.health = enemy.health - playerDamage
                if enemy.health < 0:
                    enemy.health = 0
                print ("You cut the", enemy.name, "for", playerDamage, "points of damage!!! \nThe", enemy.name, "now has", enemy.health, "HP")
                print ("----------")
                time.sleep (0.5)
                if enemy.health > 0:
                    enemyHitChance = random.randint(1,10)
                    if enemyHitChance > 4:
                        damage = enemy.attack / player.defence
                        damage = round(damage)
                        player.health = player.health - damage
                        print ("The ", enemy.name, "lashes out at you dealing", damage, "HP of damage")
                        time.sleep (0.5)
                        gameOver()
                        print ("Your HP is now ", player.health)
                        print ("----------")
                        time.sleep (0.5)
                    else:
                        print ("The", enemy.name, "swung at you, but missed!")
                        time.sleep (0.5)
                else:
                    print ("You have killed the", enemy.name)
                    lootDrop = loot(inventory)
                    time.sleep (0.5)
                    print ("The", enemy.name, "dropped", lootDrop)
                    print ("----------")
            else:
                print ("You swing and miss the", enemy.name)
                print ("----------")
                time.sleep (0.5)
                enemyHitChance = random.randint(1,10)
                if enemyHitChance > 4:
                    damage = enemy.attack / player.defence
                    damage = round(damage)
                    player.health = player.health - damage
                    print ("The ", enemy.name, "lashes out at you dealing", damage, "HP of damage")
                    time.sleep (0.5)
                    gameOver()
                    print ("Your HP is now ", player.health)
                    print ("----------")
                    time.sleep (0.5)
                else:
                    print ("The", enemy.name, "swung at you, but missed!")
                    time.sleep (0.5)
        elif choice == "2":
            print ("----------")
            print ("You try to defend yourself!")
            time.sleep (0.5)
            enemyHitChance = random.randint(1,10)
            if enemyHitChance > 4:
                damage = enemy.attack / player.defence
                damage = round(damage)
                player.health = player.health - damage
                print ("The ", enemy.name, "lashes out at you dealing", damage, "HP of damage")
                time.sleep (0.5)
                gameOver()
                print ("Your HP is now ", player.health)
                print ("----------")
                time.sleep (0.5)
            else:
                print ("The", enemy.name, "swung at you, but missed!")
                time.sleep (0.5)
        elif choice == "3":
            useItem(inventory)
            enemyHitChance = random.randint(1,10)
            if enemyHitChance > 4:
                damage = enemy.attack / player.defence
                damage = round(damage)
                player.health = player.health - damage
                print ("The ", enemy.name, "lashes out at you dealing", damage, "HP of damage")
                time.sleep (0.5)
                gameOver()
                print ("Your HP is now ", player.health)
                print ("----------")
                time.sleep (0.5)
            else:
                print ("The", enemy.name, "swung at you, but missed!")
                time.sleep (0.5)
        else:
            print("You try to flee, but there's nowhere to go...")
            time.sleep (0.5)

# Act 3 - Centre Room Mini Game:

def cstart():
    print("")
    print("You enter the centre room; did you make a life or death choice?")
    print("Only time will tell.")
    print("")
    print("You feel a cold breeze brushing past you as you enter,")
    print("you feel like 5000 eyes are watching you in a pitch-black room.")
    print("")
    print("You start to get anxious and shout:")
    print("'Hello, is anyone there?! I am here to play the game and get this over with!'")
    print("Seconds of silence go by, you see a candle light flickering from a distance, you think you can see a face but you are unsure.")
    print("")
    print("'Well… what do we have here...'")
    print("'not my first and definitely not my last toy.'")
    print("'The key to win this riddle is in your mind. Crack this riddle and you may see light…'")
    print("")
    input("---Press ENTER to continue..if you dare---")
    guess = 0
    while True:
        print("")
        print("'I follow you all the time and copy your every move,")
        print("but you can't touch me or catch me. What am I??'")
        print("")
        print("Write your guess. (Type hint1 or hint2 for help; or 'i give up' to accept your fate.")
        answer = input()
        guess += 1
        if answer.lower() == "shadow":
            print("")
            print("You win the first riddle, the second riddle might be your last..") 
            print("It took you " +  str(guess) + " guesses!")
            break
        elif answer.lower() == "hint1":
            print("A spooky dark figure...")
        elif answer.lower() == "hint2":
            print("An outline of someone or something visible...")
        else:
            damage = random.randint(1, 8)
            player.health = player.health - damage
            print ("Your skin begins to burn and you suffer", damage, "HP of damage")
            healthCheck()
            time.sleep (0.5)
            gameOver()
            print ("Your HP is now ", player.health)
            print ("----------")
            print("Try again or you will be sorry!")

    input("---Press ENTER to continue.. if you dare---")
    guess = 0
    while True:
        print("")
        print("'I am a body with a leg, an arm, and a head but I look like I am naked and bare. What am I?'")
        print("")
        print("Write your guess. (Type hint1 or hint2 for help; or 'i give up' to accept your fate.")
        answer = input()
        guess += 1
        if answer.lower() == "skeleton":
            print("'You win the second riddle, complete the third riddle and the door unlocks.'")
            print("")
            print("'If you do not get the third riddle correct, you will stay here until")
            print("next Oct 31st, that is if you survive that long muahaha!'")
            print("")
            print("It took you " +  str(guess) + " guesses!")
            break
        elif answer.lower() == "hint1":
            print("It can snap if you break it...")
        elif answer.lower() == "hint2":
            print("Supports the body structurally...")
        else:
            damage = random.randint(1, 6)
            player.health = player.health - damage
            print ("Your skin begins to burn and you suffer", damage, "HP of damage")
            healthCheck()
            time.sleep (0.5)
            gameOver()
            print ("Your HP is now ", player.health)
            print ("----------")
            print("Try again or you will be sorry!")
    input("---Press ENTER to continue.. if you dare---")
    guess = 0
    while True:
        print("")
        print("'You can find me from head to toe, I make some people faint")
        print("and I am in every living being you know. What am I?'")
        print("")
        print("Write your guess. (Type hint1 or hint2 for help; or 'i give up' to accept your fate.")
        answer = input()
        guess += 1
        if answer.lower() == "blood":
            print("It took you " +  str(guess) + " guesses!")
            print("")
            print("You Win!") 
            print("You see the odd, pale man who handed you the letter floating towards you.")
            print("The room is pitch black, but the candlelight follows him around, only showing his face.")
            print("")
            print("His horrific face and deep spooky voice makes you anxiously look around for the exit!")
            print("'I see you are smarter than you look, if you did not win...you would have been next in my collection!'")
            print("")
            print("The man blows a powdery substance in your face.")
            print("You rub your eyes, and you see the room filled with hundreds of candles.")
            print("You see a big red door that's unlocked, and creaks open on its own, you make a run for it but you trip over and fall.")
            print("")
            print("You look behind you and see bones and clothes from various periods of time.")
            print("There are piles and piles of bones and you realise that these are the people who") 
            print("were given the letter in years past.")
            print("")
            input("---Press ENTER to leave the room quick!---")
            rstart()
            break
        elif answer.lower() == "hint1":
            print("It is a dark coloured...")
        elif answer.lower() == "hint2":
            print("It is a body fluid...")
        else:
            damage = random.randint(1, 8)
            player.health = player.health - damage
            print ("Your skin begins to burn and you suffer", damage, "HP of damage")
            healthCheck()
            time.sleep (0.5)
            gameOver()
            print ("Your HP is now ", player.health)
            print ("----------")
            print("Try again or you will be sorry!")

# Act 4 - Right Room Mini Game:

def rstart():
    print("")
    print("You know what to expect as you return to the main room.")
    print("The torch above the final door lights up and you hear a click as the door unlocks.")
    print("You enter, resigned to your next challenge.")
    room4()

def room4():
    print("'Welcome to the cursed room, let's start the action!'")
    print("The door slams shut behind you and you hear a familiar and cold voice:")
    print("")
    print("'This won't be as forgiving as the last rooms...'")
    print("'The key to escape is the black cupboard behind you...")
    print("")
    print("You turn around and see a skeleton on the floor pointing at a black cupboard.")
    print("")
    print("Option - Open the cupboad.")
    print("Option - Ignore the skeleton.")
    c1 = input("Open or Ignore?:")
    time.sleep(1)
    if c1.lower() == "ignore":
        print("You ignore the cupboard, but as you turn away the cupboard doors burst open you are suddenly engulfed by a swarm of vampire bats.")
        print("The bats shriek with glee as they eat you alive.")
        print("Game Over!")
    elif c1.lower() == "open":
        print("As your hand touches the cupboards handle the skeletons bones crumble to dust, it was a curse?!")
        print("You notice that the floor of the room begins to fill with water. It isn't stopping!")
        print("")
        print("'One last riddle, and this time I'd be quick about it...'")
        print("")
        answer()
        

def answer():
    c1 = input("I run but I have no legs, you use me everyday. Without me you couldn't survive, what am I?")
    if c1.lower() == "water":
        print("The curse is now lifted. The door swings open, you have been set free from the cursed final room.")
        escape()
    else:
        print("The water fills to the top of the room, you scratch at the stone walls as your last breather leaves you body.")
        print("GAME OVER!")
        playAgain = input ("Would you like to try again? (y/n):")
        if playAgain.lower() == "y":
            room4()
        else:
            print ("----------")
            print ("Thank you for playing!")
            time.sleep (2)
            quit()

# Act 5 - Ending & Final Mini Game:

def escape():
    print("")
    print("With a rush of water you burst into the first room!")
    print("The exit door has flung wide open!")
    print("As you start to run towards the door, the pale man drops from the ceiling and blocks your way.")
    print("His eyes are blood red and furious")
    print("")
    print("'NO ONE'S EVER WON!', he spits angrily.")
    print("'NO NO NO! One last game, one last chance to make you mine...'")
    print("")
    print("The pale man produces a small box labelled , and opens it to reveal a single dice made from bone.")
    print("""'It's a simple game of chance: you roll higher you win, you roll lower
    ...well you've seen my collection...'""")
    input("---Press ENTER to Continue---")
    roll(playerScore, apocScore)
 
playerScore = 0
apocScore = 0

def roll(playerScore, apocScore):
    playerRoll = random.randint(1,6)
    apocRoll = random.randint(1,6)

    if playerRoll > apocRoll:
        playerScore += 1
    elif apocRoll > playerRoll:
        apocScore += 1

    print ("You rolled a", playerRoll)
    print ("The Pale Man rolled a", apocRoll)
    printScore(playerScore, apocScore)
    input("---Press ENTER to Roll---")
    scoreCheck(playerScore, apocScore)
    roll(playerScore, apocScore)

def finish():
    print("You've done it! No more games, no more tricks!")
    print("The pale man stares in disbelif, before he can react you run out the door.")
    print("Your legs are pounding as hard as they can.")
    print("")
    print("""As you near the end of the road you hear a scream and turn - the pale man stands in 
the doorway and as the sun finally rises on November 1st, Salmesbury Hall dissappears 
and with it The Pale Man.
""")
    print("")
    end()
    quit()

def tryAgain(playerScore, apocScore):
    retry = input("Try again? y/n")
    if retry.lower() == "y":
            playerScore = 0
            apocScore = 0
            roll(playerScore, apocScore)
    else:
            quit()

def printScore(playerScore, apocScore):
    print("You have won", playerScore, "games")
    print ("The Pale Man has won", apocScore, "games")

def scoreCheck(playerScore, apocScore):
    if playerScore >= 3:
        print("You Win!!!")
        finish()
    if apocScore >= 3:
        print ("You Lose!!!")
        tryAgain(playerScore, apocScore)

run()