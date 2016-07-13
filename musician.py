'''
Extend the example code to add a Drummer class. Drummers should be able to solo, 
count to four, and spontaneously combust. Then add a Band class. Bands should be 
able to hire and fire musicians, and have the musicians play their solos after 
the drummer has counted time.
'''

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        #super().__init__(["Boink", "Bow", "Boom"])
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician): # The Musician class is the parent of the Drummer class
    def __init__(self):
        # Call the __init__ method of the parent class
        #super().__init__(["Bam", "Crash", "Smash"])
        super(Drummer, self).__init__(["bam","bash","crash"])
        
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()
        
    def count_to_four(self):
        for j in range(0,5):
            print ("{}, " .format(j))
    
    def combust(self):
        print "Boom!!"

class Band(object):
    def __init__(self):
        self.member = {}
        
    def hire(self):
        new_member = raw_input("What is the new bandmember's name? ")
        type_musician = raw_input("Is the person a drummer or a guitarist? ")
        if type_musician.lower() == "drummer":
            self.member[new_member] = Drummer()
        elif type_musician.lower() == "guitarist":
            self.member[new_member] = Guitarist()
        else:
            type_musician = raw_input("Please type either a drummer or a guitarist: ")
            

    def fire(self, fire_member): 
        #check to see if fire_member is in the bankd
        if fire_member in self.member:
            del self.member[fire_member]
            print ("{} has fired." .format(fire_member))
        else:
            print ("{} is not in the band." .format(fire_member))

      
    def play_solos(self, play_length):
        has_drummer = all( isinstance(e, Drummer) for e in self.member.itervalues() )

        if has_drummer:
            print ("There is a drummer.")
            for musician in self.member.itervalues():
                musician.count_to_four()
                musician.solo(play_length)
                musician.combust()
        else:
            print ("There is no drummer.")
            for musician in self.member.itervalues():
                musician.solo(play_length)
                
def main():
    iband = Band()
    iband.hire()
    iband.hire()
    iband.hire()
    
    who_to_fire = raw_input("Who do you want to fire? ")
    iband.fire(who_to_fire)
    print iband.member
    iband.play_solos(6)
  
    
if __name__ == '__main__':
    main()
        
        
        
        
        
        
        