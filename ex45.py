class Other(object):

    def override(self):
        print("OTHER override()")

        def implicit(self):
            print("OTHER imlicit()")

            def altered(self):
                print("OTHER altered()")

                class Chils(object):

                    def __init__(self):
                        self.other = Other()

                        def implicit(self):
                            print("CHILD override()")

                            def altered(sself):
                                print("CHILD, BEFORE OTHER altered()")
                                self.other.altered()
                                print("CHILD, AFTER OTHER altered()")

                                son = child()
                                son.implicit()
                                son.override()
                                son.altered()

                                    

