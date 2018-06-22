class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        The Gothons of Palent Percal #25 have invaded your ship and destroyeed your entire crew. You are the last surviving membr and your last mission is to get the neutron destruct bomb from the Weapons Armory , put it in the bridge , and blow the ship up after getting into an escape pod.

        You're running down the central coridor to the WEapons
        Armory when a Gothon jumps out , red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate filled body . He's blocking the door to the Armory and about to pull a weapon to blast you.
        """))

        action = input(">")

        if action == "shoot!":
            print(ssedent("""
            Quick on the draw you yank out your blaster and fire it at the Gothn. His clown costume is flowing and moving around his body, which throws off your aim. Your laser hits his costume but misses him entirely. This completely euins his brand new costume his mother boought him , which makes him fly into an instance rage and blast you repeatedlt in the face until you are dead. Then he eats you.
            """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
            Like a world class boxer you dodge , weave ,slip and slide right as the Gothon's blaster cranks a laser past your head. In the middle of your artful dodge your foot slips and you bang your head on hte metal wall and pass out . You wake up shortly after only to die as the Gothon stomps on your head and eats you.
            """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
            Lucky for you they made you learn Gothon unsults in the academy. You tell the one gothon joke you know:
            Lbhe xbgure vf fb sng,jura fur fvgf nebhag gur ubhfr,fur fvgf nebhaq gur ubhfr. The Gothon stops , tries not to laugh ,then busts out laughing and can't  move .while he's laughing uoy run up and shoot him square in the head putting him down,then jump through the Weapon Armory door.
            """))
            return 'laser_weapon+armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
        class LaserWeaponAemory(Scene):

            def enter(self):
                print(dedent("""
                You do a dive roll into the Weapon Armory , crouch and scan the room for more Gothons that mght be hiding .It's dead quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb int its container. Thre's a keypad lock on the box and you need the code to get the bomb out . If you get the code wrong 10 timed then the lock closes foreover and you can't get the bomb . The code  is 3 digits.
                """))
                code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
                guess = input("[keypad]>")
                guesses = 0

                while guess != code and guesses <10:
                    print("BZZZZDDD!")
                    guess = input("[keypad]> ")

                    if guess == code:
                        print(dedent("""
                        The container clicks open and seal breaks , letting gas out . You grab the neutron bomb and run as fast as you can to the bridge wher you must place it in the right spot .
                        """))
                        return 'the_bridge'
                    else:
                        print(dedent("""
                        The lock buzzes one last time and then you hear a sicking melting sound as the mechanism is fused together .You decide to sit there , and finally the Gothon sblow up th ship from their ship and you die.
                        """))
                        return 'death'
                    class TheBridge(Scene):

                        def enter(self):
                            print(dedent("""
                            You burst onto the Bridge with the neutrondestruct bomb under your arm  and surprises 5 Gothons who are trying to take controll of the ship. Each of them has an even uglier clown costume than the last. They haven't pulled their weapons out yet , as they see active bomb under your arm and don't want to see set ita off.
                            """))
                            action = input(">")

                            if action == "throw the bomb":
                                print(dedent("""
                                In a panic you throw the bomb at the group of Gothons and make a leap for the door . Right as you drop it a Gothon shoots you right inthe back killing you . As you die you see another Gothon frantically try to disarm the bomb. You die knowing they will probably blow up when it goes off.
                                """))
                                return'death'

                            elif action == "slowly place th bomb":
                                print(dedent("""
                                You point your blaster at the bomb under your arm and the Gothon sput their hands uo and start to sweeat . You inch backward to the door , open it , and then carefully place the bomb onthe floor , pointing your blaster at it. You then jump back through the door , punch the close button and the lock so the Gothons can't  get out . Now wthat the bomb is placed you run to the escape pod to get off this can.
                                """))
                                return 'escape_pod'
                            else:
                                print("DOES NOT COMPUTE!")
                                return "the_bidge"
                            class EscapePod(Scene):

                                def enter(self):
                                    print(dedent("""
                                    You rush through the ship  desprately trying to make it to the escape pod before the whole ship explodes. It seems like hardly any Gothons are on the ship , so your run is clear of interference. You get to the chambet with the escapes pods , and now need to pick one to take . Some of them could be damaged but you don't have time to look . There's 5 pods, which one do you take?
                                    """))

                                    good_pod = randint(1,5)
                                    guess = input("[pod #]>")
                                    if int(guess)!= good_pod:
                                        print(dedent("""
                                        You jump into pod {guess} and hit the eject button . The pod escapes out into the void of space , then implodes as the hull ruptures, crushing your body into jam jelly.
                                        """))
                                        return 'death'
                                    else:
                                        print(dedent("""
                                        Tou jump into pod {guess} and hit he eject button . The pod eeasily slides out into space heeading to the palent below. As it flies to the planet , you look back and see your ship implode then explode like a bright star , taking out the Gothon ship at the same time . You won!
                                        """))

                                        return 'finished'
                                    class Finished(Scene):

                                        def enter(self):
                                            print("You won! Good job")
                                            return'finished'
                                        class Map(object):

                                            scenes = { 'central_cooridor': CentralCorridor(),
                                                    'laser_weapon_armory': LaserWeaponArmory(),
                                                    'the_bridge': TheBridge(),
                                                    'escape_pod': EscapePod(),
                                                    'death': Death(),
                                                    'finished': Finished(),
                                                self.start_scene = start_scene
                                                
                                                def next_scene(self, scene_name):}

                                            val = Map.scenes.get(scene_name)
                                            return val
                                        def opening_scene(self):
                                            return self.next_scene(self.start_scene)







