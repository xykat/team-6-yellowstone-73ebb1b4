class Character:
    # def __init__(self):
    #     self.name = None  # Initialize the name attribute
    
    # def get_user_input(self, prompt):
    #     user_input = input(prompt)
    #     return user_input

# Create an instance of the class
    input_handler = Character()

# Show to the user and collect the data
user_text = input_handler.get_user_input("Enter the name of your character: ")
print("You entered: ", user_text)