"""An adventure game programmed for COMP 110."""

__author__ = "730490960"

from random import randint

points: int = 0
player: str = ""
NAMED_CONSTANT: str = "\U0001F40F" 


def main() -> None:
    """The main function. Calls all other functions in game."""
    global player
    global points
    __name__ == "__main__"

    greet()
    print(f"Alright, { player }, let's begin!")
    story()
    points = custom(points)
    
    print(f"You now have { str(points) } points, and are determined to find { NAMED_CONSTANT }.")
    duke()

    # Game loop.
    repeat: int = 0
    repeat = int(input(f"You have finished with { str(points) } points!\nPlease type '1' if you would like to restart by searching at Duke, '2' if you would like to start the entire game over, or any other number to quit the game."))
    if repeat == 1:
        duke()
    elif repeat == 2:
        rep: int = 2
        while rep == 2:
            points = 0
            print("\n\nYour points have been reset to 0.")
            greet()
            print(f"Alright, { player }, let's begin!")
            story()
            points = custom(points)
            print(f"You now have { str(points) } points, and are determined to find { NAMED_CONSTANT }.")
            duke()
            rep = int(input(f"You have finished with { str(points) } points!\nPlease type '1' if you would like to restart by searching at Duke, '2' if you would like to start the entire game over, or any other number to quit the game."))
            if rep == 1:
                duke()
            elif rep == 3:
                quit()
    else:
        quit()


def greet() -> None:
    """Greets players to game."""
    global player
    print("Hello, and welcome to the ~Carolina Adventure Game~!")
    print("Today, you will be traversing across Chapel Hill in search of the live Rameses, who has gone missing!")
    print("However, you must be careful...there are dark secrets and mysteries everywhere.")
    player = input("Please enter your name to begin!  ")


def story() -> None:
    """Introduces story to player."""
    global player
    global NAMED_CONSTANT
    global points
    print(f"\nThe story begins on a rainy Saturday morning...as Carolina's chief detective, you, { player }, are tasked with all of UNC's investigations.")
    print("Would you like a squirrel for your animal sidekick on this adventure or not?")
    sidekick: int = int(input("Answer '1' for the squirrel and any other number for no. "))

    if sidekick == 1:
        print("Congrats for being cool. Your squirrel's name is Timmy!")
        points = points + 1
        print("+1 point!")
    else:
        print("You're lame...\nThe squirrel, Timmy, decides to come along anyways. Your distaste of him is reciprocated.")

    print("\nAnyways...your Saturday morning starts with the shrill ring of your phone on your nightstand.\nYou groan, your head pounding from the amount of...water...you consumed last night.")

    answer: int = int(input("Answer '1' if you pick up the phone, and any other number if you're a lazy bum. "))
    
    if answer == 1:
        print("Good job on picking up the phone. It is your job, after all.")
        points = points + 1
        print("+1 point!")
    else:
        print("This is literally your damn job. You HAVE to pick up the phone. No points for you!")

    print("\n\"Hello?\" You ask blearily, accepting the call.")
    print(f"\n\"{ player }...it's urgent. Rameses has gone missing!\"")
    print("\nYou shoot up with a bolt. Not Rameses....and not on game day, against Duke! There was absolutely no way the Tar Heels would win against the Blue Devils without the presence of the beloved Rameses.")
    print(f"\n\"{ player }, are you still there?")
    print("\n\"Yes!\" you call out, fear scrambling around in your brain. You needed to come up with a course of action... and fast.")
    print("\n\nThrowing your shoes and game day gear as fast as you can, grabbing an umbrella, you sprint to the large oak tree on the quad where Timmy spends his days.\"Timmy!\" you call out.")

    if sidekick == 1:
        print("Timmy scrambles down the tree with a chirp, excited to see you again. You feed him an acorn and he scrambles atop your shoulder.")
        points = points + 1
        print("+1 point!")
    else:
        print("Timmy emerges with reluctance, knowing that his contribution to your mission is essential. However, your mutual dislike of one another does not make you the best of partners. Perhaps you'll learn to work together better on this mission.")
    print(f"With your sidekick and { str(points) } points, you're ready to go on the search to find { NAMED_CONSTANT }!")


def custom(n: int) -> int:
    """Continues the story for the player."""
    global player
    global points

    n = points
    print(f"\n\nYou and Timmy sit down on the steps of Wilson Library to discuss your plan on where to go first, as you pin your badge onto your chest, now in official Detective { player } mode.\nYou decide to choose randomly the first place to look for clues...")
    randy: int = randint(1, 4)

    if randy == 1:
        print("Your mind settles on the Campus Y - maybe Rameses wanted to educate himself on social justice!")
        print("You and Timmy cross the quad to check out the Y. However, the building is quiet and Meantime Coffee Co. is closed. There's no sign of Rameses anywhere.")
        n = n + 1
        print("+1 point! Good job for trying!")
    elif randy == 2:
        print("You decide to check out Davis Library. It seems entirely probable that Rameses wanted to do some light reading before the game.")
        print("You and Timmy head inside Davis and ask the librarians if they've seen Rameses at all, but they have no clue. You also try asking the student body on the first floor of Davis, but the Make Davis Loud Again movement was far too successful and students are too busy making TikToks and yelling to answer your questions.")
        n = n + 1
        print("+1 point! Good job for trying!")
    elif randy == 3:
        print("Timmy and you agree to go to Kenan Memorial Stadium. Perhaps Rameses just wanted to arrive to the game super early.")
        print("You and Timmy head towards South Campus for the stadium. All the games are locked, so you send Timmy in to investigate the situation. Timmy scrambles over the gates to observe the stadium, but when he returns, his tail is drooped. It appears the mission was unsuccessful.")
        n = n + 1
        print("+1 point! Good job for trying!")
    elif randy == 4:
        print("Your first spot will be the Dean E. Smith Center. Maybe Rameses got confused and went to the wrong stadium.")
        print("You and Timmy are feeling lazy, so you take the U down to South Campus and head for the basketball arena. With the doors locked, you send in Timmy to investigate the situation. Timmy squeezes in through a vent to observe the Center, but when he returns, his tail is drooped. It appears the mission was unsuccessful.")
        n = n + 1
        print("+1 point! Good job for trying!")
    print("\nFeeling slightly deflated by the failure of your morning search, you and Timmy decide to hit the dining hall for some food before you resume looking for clues.")

    dining: int = int(input("Answer '1' to go to Lenoir or any other number to go to Chase."))
    if dining == 1:
        print("You and Timmy wander over to Lenoir to grab a quick brunch.")
    else:
        print("You and Timmy wander over to Chase to grab a quick brunch.")
        n = n + 1
        print("+1 point! Chase is obviously superior over Top of Lenoir.")

    print("\n\nHowever, just as you're leaving, you come across a scrap of dark blue fabric by the exit. Suddenly filled with fear, you immediately know where you must look: at Duke, on enemy grounds.")
    n = n + 1
    print("+1 point! Good job for finding a clue.")
    return n


def duke() -> None:
    """Your adventure is continuing at Duke."""
    global points
    print("\n\nYou and Timmy catch the next bus to Durham, determined to bring Rameses back before the game starts.\nWhen you get to Duke, you are immediately confused about where to look for Rameses.")
    campus: int = int(input("Type '1' to check out the gardens first, and any other number to look in the basketball stadium."))
    if campus == 1:
        print(f"Hurrying over to the garden, you are unsure of where to start in the vast spread of flowers and trees. However, as you near the pond in the middle, you spot signs of a scuffle and the prints of {  NAMED_CONSTANT } in the mud by the pond.")
        points = points + 1
        print("+1 point! You're on the right track.")
        gardens()
    else:
        print(f"You and Timmy have to rush all the way across campus to get to the basketball stadium, but there's no sign of Rameses anywhere. Figures- it's a football game day, so why are you at the basketball stadium looking for { NAMED_CONSTANT }?")
        print("By this time, it's getting too late, and the game is about to begin. You feel like an incredible failure for not locating Rameses. Exhausted and tired, you head back to Chapel Hill.")


def gardens() -> None:
    """The adventure continues at the Duke gardens."""
    global points
    print("You and Timmy follow the tracks as far as you can go. They end close to the north part of the gardens.")
    campus: int = int(input("Type '1' to check out the dining hall and any other number to search around the quad."))
    if campus == 1:
        print(f"You get the instinct that { NAMED_CONSTANT } might be facing some culinary torture in the dining hall, so you and Timmy rush towards the dining hall. Inside, you find Rameses and a bunch of evil-looking Duke students, and you breathe a sigh of relief. Mustering up your confrontation skills, you shout out your demands for the Blue Devils to return Rameses, and with Timmy baring his teeth, the Duke students reluctantly hand back Rameses' leash to you.")
        points = points + 3
        print("+3 points! Good job for finding Rameses.")
        print("\n\nThat night, Duke suffers a massive loss against UNC. With Rameses strutting around the field, you and Timmy enjoy the game, proud of your accomplishments that day.")
    else:
        print("You try to look around the quad for Rameses, but you realize that it is improbable for the Duke students to be holding Rameses hostage in broad daylight.")
        print("By this time, it's getting too late, and the game is about to begin. You feel like an incredible failure for not locating Rameses. Exhausted and tired, you head back to Chapel Hill.")
        

if __name__ == "__main__":
    main()
