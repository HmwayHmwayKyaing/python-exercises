from sys import argv
script, user_name=argv
prompt='>'
print(f"Hi {user_name},I'm the {script} script.")
print("I'd like to ask you a few questions")
print(f"Dp you like me {user_name}?")
likes=input(prompt)
print(f"Wher do you like {user_name}?")
lives=input(prompt)
print("Whtat kind of compputer do you have?")
computer=input(prompt)
print(f"""
        Alrilght ,so yo said {likes} about liking me,
        You live in {lives}.Not sure where that is .
        And you have a {computer} computer .Nice.
        """)

