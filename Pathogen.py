from os import system, name

class Pathogen:
    '''
    Represents the main player class in the game. Can be one of 2 different types.
    Has a range of attributes that confer health/damage advantages for the player.
    '''
    def __init__(self, organism):
        if organism == "Virus":
            self.type = "virus"
            self.resistance = 40
            self.location = ""
            self.attack_method = "antigens"
            self.attack_damage = 5
            self.replication_rate = 50
        elif organism == "Bacteria":
            self.type = "bacteria"
            self.resistance = 50
            self.location = ""
            self.attack_method = "endotoxins"
            self.attack_damage = 7
            self.replication_rate = 40

    def clear():
        '''
        A function to clear the screen.
        '''
        if name == 'nt':
            clear = system('cls')
        else:
            clear = system('clear')

class Organ:
    '''
    The parent class for all organs.
    Contains functions that the player can perform.
    The vasculature subclass represents a 'map' that the user (pathogen) takes to travel to the various organs.
    '''

    def invade(self, pathogen):
        '''
        Invade an organ and return a menu of options by calling behavior function.
        '''
        Pathogen.clear()
        print("You are in the {}. \nThe primary function of the {} is to {}.".format(self, self, self.function))
        enter = input("Press 'Enter' to continue.")
        Pathogen.clear()
        print("Location: {}".format(self))
        print("Resistance Level: {}".format(pathogen.resistance))
        self.decision = self.behavior(self.decision_list)
        return self.decision

    def behavior(self, decision_list):
        '''
        The list of actions the pathogen can take inside an organ.
        The decision list is unique to each organ class.
        '''
        choices = []
        print("Choose your next action: ".format(self))
        self.decision_list = decision_list
        for i in range(0, len(self.decision_list)):
            print("[{}] {}.".format((i + 1), self.decision_list[i]))
            choices += [str(i + 1)]
        while True:
            choice = input("Choose an action from the list of choices.")
            if choice not in choices:
                print("You must choose a number corresponding to the choices given.")
                continue
            else:
                break
        self.decision = self.decision_list[(int(choice) - 1)]
        return self.decision

    def next_organ(self, organ, organ_list):
        '''
        Invade an adjacent organ.
        This will either be back to the bloodstream or an adjacent organ, but not a distant one.
        '''
        Pathogen.clear()
        destinations = []
        print("From the {} you can invade: ".format(organ))
        for i in range(0, len(organ_list)):
            print("[{}] {}.".format((i + 1), self.organ_list[i]))
            destinations += [str(i + 1)]
        while True:
            choice = input("Where would you like to travel to?")
            if choice not in destinations:
                print("You must choose a valid destination.")
                continue
            else:
                break
        self.target = self.organ_list[(int(choice) - 1)]
        return self.target

    def attack(self, pathogen):
        '''
        The player will be attacked by various immune defenses and defeat them.
        '''
        Pathogen.clear()
        print("You are being attacked by {}s!. The primary immune defense of the {}.".format(self.defenses.type, self))
        pathogen.resistance -= self.defenses.attack_damage
        print("You have lost {} resistance points, remaining resistance is {}.".format(self.defenses.attack_damage, pathogen.resistance))
        while True:
            x = input("Press 'Enter' to attack the {} back!".format(self.defenses.type))
            if  self.defenses.health > 0:
                if pathogen.resistance > 0:
                    Pathogen.clear()
                    self.defenses.health -= pathogen.attack_damage
                    print("You fire off some {} at the attacking {}! \nThey damage the target, but they do not finish the {} off. Keep fighting!".format(pathogen.attack_method, self.defenses.type, self.defenses.type))
                    enter = input("Press 'Enter' to continue.")
                    Pathogen.clear()
                    pathogen.resistance -= self.defenses.attack_damage
                    print("The {} hits back! Your resistance is now {}. Keep fighting!".format(self.defenses.type, pathogen.resistance))
                else:
                    Pathogen.clear()
                    print("The {} {}s have managed to destroy the invading pathogen! You lose!".format(self, self.defenses.type))
                    enter = input("Press 'Enter' to exit game.")
                    exit()
            elif self.defenses.health <= 0:
                Pathogen.clear()
                print("Your {} have done the trick and successfully destroyed the attacking {}s. You have {} resistance remaining.".format(pathogen.attack_method, self.defenses.type, pathogen.resistance))
                enter = input("Press 'Enter' to continue.")
                Pathogen.clear()
                break

    def replicate(self, pathogen):
        '''
        Once the player defeats the defenses, they will be able to replicate within the organ.
        Replicating within an organ damages it.
        '''
        Pathogen.clear()
        print("Once defeating the defenses of the {}, you are now free to replicate.".format(self))
        while True:
            x = input("Press 'Enter' to replicate.")
            if x == "":
                old_health = self.health
                self.health -= pathogen.replication_rate
                functionality_reduction = ((old_health - self.health)/old_health)*100
                break
            else:
                continue
        Pathogen.clear()
        print("Your pathogenic replication has reduced the function of the {} by {}%.".format(self, round(functionality_reduction, 2)))

    class Defenses:
        '''
        A nested class defining each organ's unique defenses, 2 types.
        Each organ, when instantiated, will instantiate its own unique defense type either a lymphocyte or a macrophage.
        '''
        pass

    class Macrophage(Defenses):
        '''
        A type of defense.
        '''
        def __init__(self):
            self.type = "macrophage"
            self.health = 10
            self.attack_method = "Engulf"
            self.attack_damage = 2

        def __str__(self):
            return "macrophage"

        def __repr__(self):
            return self.__str__()

    class Lymphocyte(Defenses):
        '''
        A type of defense.
        '''
        def __init__(self):
            self.type = "lymphocyte"
            self.health = 8
            self.attack_method = "Antibodies"
            self.attack_damage = 3

        def __str__(self):
            return "lymphocyte"

        def __repr__(self):
            return self.__str__()

class Vasculature(Organ):
    '''
    Acts as a central lobby or 'map' for the player to travel to any organ they want to next.
    '''
    def __init__(self, pathogen):
    # Defines the organs that the player can travel to.
        self.function = "to circulate oxygen and nutrients around the body for metabolism"
        self.organ_list = ["Heart", "Lungs", "Stomach", "Intestines", "Liver", "Pancreas"]
        self.decision_list = ["Invade an organ", "Quit"]
        self.resume_list = ["Invade an organ", "Quit", "Get health stats", "Help"]
        self.defenses = self.Lymphocyte()

    def __str__(self):
        return "vasculature"

    def __repr__(self):
        return self.__str__()

class Heart(Organ):
    '''Heart subclass.'''
    def __init__(self, pathogen):
        self.name = "heart"
        self.function = "to pump blood around the body"
        self.health = 100
        self.organ_list = ["Lungs", "Vasculature"]
        self.decision_list = ["Replicate", "Battle", "Invade adjacent organ", "Exit to vascular system", "Get health stats", "Help"]
        self.defenses = self.Macrophage()

    def __str__(self):
        return "heart"

    def __repr__(self):
        return self.__str__()

class Lungs(Organ):
    '''Lungs subclass'''
    def __init__(self, pathogen):
        self.name = "lungs"
        self.function = "to oxygenate the blood and excrete carbon dioxide"
        self.health = 100
        self.organ_list = ["Heart", "Vasculature"]
        self.decision_list = ["Replicate", "Battle", "Invade adjacent organ", "Exit to vascular system", "Get health stats", "Help"]
        self.defenses = self.Lymphocyte()

    def __str__(self):
        return "lungs"

    def __repr__(self):
        return self.__str__()

class Stomach(Organ):
    '''Stomach subclass'''
    def __init__(self, pathogen):
        self.name = "stomach"
        self.function = "to function of the stomach is to digest food"
        self.health = 100
        self.organ_list = ["Intestines", "Vasculature"]
        self.decision_list = ["Replicate", "Battle", "Invade adjacent organ", "Exit to vascular system", "Get health stats", "Help"]
        self.defenses = self.Lymphocyte()

    def __str__(self):
        return "stomach"

    def __repr__(self):
        return self.__str__()

class Intestines(Organ):
    '''Intestines subclass'''
    def __init__(self, pathogen):
        self.name = "intestines"
        self.function = "to absorb nutrients"
        self.health = 100
        self.organ_list = ["Stomach", "Vasculature"]
        self.decision_list = ["Replicate", "Battle", "Invade adjacent organ", "Exit to vascular system", "Get health stats", "Help"]
        self.defenses = self.Macrophage()

    def __str__(self):
        return "intestines"

    def __repr__(self):
        return self.__str__()

class Liver(Organ):
    '''Liver subclass'''
    def __init__(self, pathogen):
        self.name = "liver"
        self.function = "to remove toxins"
        self.health = 100
        self.organ_list = ["Pancreas", "Vasculature"]
        self.decision_list = ["Replicate", "Battle", "Invade adjacent organ", "Exit to vascular system", "Get health stats", "Help"]
        self.defenses = self.Macrophage()

    def __str__(self):
        return "liver"

    def __repr__(self):
        return self.__str__()

class Pancreas(Organ):
    '''Pancreas subclass'''
    def __init__(self, pathogen):
        self.name = "pancreas"
        self.function = "to secrete digestive intestines"
        self.health = 100
        self.organ_list = ["Liver", "Vasculature"]
        self.decision_list = ["Replicate", "Battle", "Invade adjacent organ", "Exit to vascular system", "Get health stats", "Help"]
        self.defenses = self.Lymphocyte()

    def __str__(self):
        return "pancreas"

    def __repr__(self):
        return self.__str__()

class Engine():
    '''
    The main game engine. Initializes the player (pathogen), the vasculature and organs that form the body.
    '''
    def __init__(self, pathogen):
        #initialize player
        self.pathogen = pathogen

        #initialize organs
        self.Vasculature = Vasculature(self.pathogen)
        self.Heart = Heart(self.pathogen)
        self.Lungs = Lungs(self.pathogen)
        self.Stomach = Stomach(self.pathogen)
        self.Intestines = Intestines(self.pathogen)
        self.Liver = Liver(self.pathogen)
        self.Pancreas = Pancreas(self.pathogen)

        #Initialize organ dictionary for choosing.
        self.organ_dict = {"Vasculature": self.Vasculature, "Heart": self.Heart, "Lungs": self.Lungs, "Stomach": self.Stomach, "Intestines": self.Intestines, "Liver": self.Liver, "Pancreas": self.Pancreas}

        #Initialize behavior dictionary of choices.
        self.behavior_dict = {"Quit": 0, "Invade an organ": 1, "Replicate": 2, "Battle": 3, "Invade adjacent organ": 4, "Exit to vascular system": 5, "Get health stats": 6, "Help": 7}

        #Initialize the game process.
        self.start(self.pathogen)

    def start(self, pathogen):
        '''
        The actual gameplay process.
        '''
        self.pathogen = pathogen
        Pathogen.clear()
        print("You are a {}, a type of microbial pathogen. You have invaded the human host.".format(pathogen.type))
        enter = input("Press 'Enter' to continue.")
        Pathogen.clear()
        print("You must use the vasculature to travel between distant organs. \nYou can invade adjacent organs without having to re-enter the vasculature.")
        enter = input("Press 'Enter' to continue.")
        Pathogen.clear()
        print("Your goal is to spread around the host's body, invade their organs and replicate within them.")
        enter = input("Press 'Enter' to continue.")
        Pathogen.clear()
        print("Before replication, you must battle and defeat the host's immune defenses.")
        enter = input("Press 'Enter' to continue.")
        Pathogen.clear()
        print("When you replicate inside an organ, you damage it. \nDamaging an individual organ affects the hosts overall health.")
        enter = input("Press 'Enter' to continue.")
        Pathogen.clear()
        print("When the host's overall health drops below 60%, they die.")
        enter = input("Press 'Enter' to continue.")
        Pathogen.clear()
        print("Your goal is to kill the host.")
        enter = input("Press 'Enter' to continue.")
        Pathogen.clear()
        print("Good luck!")
        enter = input("Press 'Enter' to continue.")
        Pathogen.clear()
        if self.Vasculature.invade(self.pathogen) != "Quit":
            Pathogen.clear()
            self.pathogen.location = self.Vasculature.next_organ(self.Vasculature, self.Vasculature.organ_list)
            self.Vasculature.decision_list = self.Vasculature.resume_list
            choice = self.organ_dict[self.pathogen.location].invade(self.pathogen)
            while self.behavior_dict[choice] != 0:
                #The total health score which gets updated every time the player damages an organ by replicating within it.
                self.total_health = (self.Heart.health + self.Lungs.health + self.Stomach.health + self.Intestines.health + self.Liver.health + self.Pancreas.health)/6
                #Invade an organ.
                if self.behavior_dict[choice] == 1:
                    #Once total health drops below 60, the player wins...
                    #I tried to use a while loop to automatically quit when the global score dropped below a certain amount, but I could not get it to constantly update if total health located outside the loop.
                    if self.total_health > 60:
                        self.pathogen.location = self.Vasculature.next_organ(self.Vasculature, self.Vasculature.organ_list)
                        choice = self.organ_dict[self.pathogen.location].invade(self.pathogen)
                    else:
                        Pathogen.clear()
                        print("You have successfully invaded the host and killed them! \nThank you for playing Pathogen!")
                        enter = input("Press 'Enter' to exit.")
                        break
                        exit()
                #Replicate inside an organ.
                elif self.behavior_dict[choice] == 2:
                    if self.total_health > 60:
                        location = self.organ_dict[self.pathogen.location]
                        if location.defenses.health <= 0 and location.health > 0:
                            location.replicate(self.pathogen)
                            enter = input("Press 'Enter' to continue.")
                            Pathogen.clear()
                            choice = self.organ_dict[self.pathogen.location].invade(self.pathogen)
                        elif location.defenses.health > 0:
                            Pathogen.clear()
                            print("You must defeat the {}'s defenses before you can replicate.".format(self.pathogen.location))
                            enter = input("Press 'Enter' to continue.")
                            Pathogen.clear()
                            choice = self.organ_dict[self.pathogen.location].invade(self.pathogen)
                        elif location.health <= 0:
                            Pathogen.clear()
                            print("You have already fully destroyed the {}. Please invade another organ.".format(location))
                            enter = input("Press 'Enter' to continue.")
                            Pathogen.clear()
                            choice = self.organ_dict[self.pathogen.location].invade(self.pathogen)
                    else:
                        Pathogen.clear()
                        print("You have successfully invaded the host and killed them! \nThank you for playing Pathogen!")
                        enter = input("Press 'Enter' to exit.")
                        break
                        exit()
                #Initiate battle with organ defenses if conditions are met.
                elif self.behavior_dict[choice] == 3:
                    if self.total_health > 60:
                        location = self.organ_dict[self.pathogen.location]
                        if location.defenses.health <= 0:
                            Pathogen.clear()
                            print("You have already defeated the {}'s defenses. You are free to replicate.".format(self.pathogen.location))
                            enter = input("Press 'Enter' to continue.")
                            Pathogen.clear()
                            choice = self.organ_dict[self.pathogen.location].invade(self.pathogen)
                        else:
                            if location.defenses.health > 0:
                                location.attack(self.pathogen)
                            choice = self.organ_dict[self.pathogen.location].invade(self.pathogen)
                    else:
                        print("You have successfully invaded the host and killed them! \nThank you for playing Pathogen!")
                        enter = input("Press 'Enter' to exit.")
                        break
                        exit()
                #Invade the adjacent organ.
                elif self.behavior_dict[choice] == 4:
                    if self.total_health > 60:
                        self.pathogen.location = self.organ_dict[self.pathogen.location].next_organ(self.organ_dict[self.pathogen.location], self.organ_dict[self.pathogen.location].organ_list)
                        choice = self.organ_dict[self.pathogen.location].invade(self.pathogen)
                    else:
                        Pathogen.clear()
                        print("You have successfully invaded the host and killed them! \nThank you for playing Pathogen!")
                        enter = input("Press 'Enter' to exit.")
                        break
                        exit()
                #Exit to the vascular system to travel to a distant organ.
                elif self.behavior_dict[choice] == 5:
                    if self.total_health > 60:
                        choice = self.Vasculature.invade(self.pathogen)
                    else:
                        Pathogen.clear()
                        print("You have successfully invaded the host and killed them! \nThank you for playing Pathogen!")
                        enter = input("Press 'Enter' to exit.")
                        break
                        exit()
                #Bring up the health stats menu to track progress.
                elif self.behavior_dict[choice] == 6:
                    if self.total_health > 60:
                        Pathogen.clear()
                        location = self.organ_dict[self.pathogen.location]
                        print("Pathogen Resistance: {}".format(self.pathogen.resistance))
                        print("Total body health: {:.1f}%".format(self.total_health))
                        print("Individual Organ Health: \nHeart: {}% \nLungs: {}% \nStomach: {}% \nIntestines: {}% \nLiver: {}% \nPancreas: {}%".format(self.Heart.health, self.Lungs.health, self.Stomach.health, self.Intestines.health, self.Liver.health, self.Pancreas.health))
                        while True:
                            a = input("Press 'Enter' to exit back to organ.")
                            if a == "":
                                choice = self.organ_dict[self.pathogen.location].invade(self.pathogen)
                                break
                            else:
                                continue
                    else:
                        Pathogen.clear()
                        print("You have successfully invaded the host and killed them! \nThank you for playing Pathogen!")
                        enter = input("Press 'Enter' to exit.")
                        break
                        exit()
                # A rudimentary help menu.
                elif self.behavior_dict[choice] == 7:
                    if self.total_health > 60:
                        Pathogen.clear()
                        print("Opening instructions:")
                        print("-"*100)
                        print("You are a {}, a type of microbial pathogen. You have invaded the human host.".format(pathogen.type))
                        print("\nYou must use the vasculature to travel between distant organs.\n \nYou can invade adjacent organs without having to re-enter the vasculature.")
                        print("\nYour goal is to spread around the host's body, invade their organs and replicate within them.")
                        print("\nBefore replication, you must battle and defeat the host's immune defenses.")
                        print("\nWhen you replicate inside an organ, you damage it.\n \nDamaging an individual organ affects the hosts overall health.")
                        print("\nWhen the host's overall health drops below 60%, they die.")
                        print("\nYour goal is to kill the host.")
                        print("-"*100)
                        print("Functions: \n'Quit' - exit game. \n'Invade an Organ' - Enter an organ in order to attack and replicate inside of it. \n'Replicate' - Once you have defeated the host's defenses, you can replicate inside it and damage it.")
                        print("'Battle' - Enter battle mode. You must battle the host immune defenses before you can replicate inside of it. \n'Invade adjacent organ' - Invade the organ next to the organ you are currently inside of.")
                        print("'Exit to vascular system' - Exit back into the vasculature in order to invade a distant organ. \n'Get health stats' - Get your health status, the health status of the individual organs and the total body health.")
                        print("-"*100)
                        print("Player classes: \n'Virus' - Resistance: 40, Attack Method: Antigens, Attack Damage: 6, Replication Rate (damage): 50.")
                        print("'Bacteria' - Resistance: 50, Attack Method: Endotoxins, Attack Damage: 7, Replication Rate (damage): 40.")
                        print("-"*100)
                        print("Defense classes: \n'Macrophage' - Health: 10, Attack Method: Engulf, Attack Damage: 2 \n'Lymphocyte - Health: 8, Attack Method: Antibodies, Attack Damage: 3")
                        enter = input("Press 'Enter' to continue.")
                        Pathogen.clear()
                        choice = self.organ_dict[self.pathogen.location].invade(self.pathogen)
                    else:
                        Pathogen.clear()
                        print("You have successfully invaded the host and killed them! \nThank you for playing Pathogen!")
                        enter = input("Press 'Enter' to exit.")
                        break
                        exit()
            else:
                if self.behavior_dict[choice] != 0:
                    print("Quitting program. \nThank you for playing pathogen.")
                    exit()
        else:
            print("Quitting program. \nThank you for playing pathogen.")
            exit()

#Only non-class-based coding I used - to start the game, allowing player to make a choice between playing as a bacteria or a virus.
while True:
    x = input("Welcome to Pathogen! Please choose a class of pathogen to play as: \n Press [1] to play as a Virus. \n Press [2] to play as a Bacteria.\n")
    if x == "1":
        pathogen = "Virus"
        break
    elif x == "2":
        pathogen = "Bacteria"
        break
    else:
        print("Please select a pathogen class from the given options.")
        continue

#Initiate objects and start game.
player = Pathogen(pathogen)
e = Engine(player)
