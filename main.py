# Build list of data dictionaries
# Write list_names function definition
    # for items in data
        # print "{Position} {value}"
# Write get_new_student function definition
    # create new dictionary
    # ask user for required input and save in variables
    # add input to new dictionary
# Define flag variable for loop
# Start main program while loop based on flag variable condition
    # Call menu_selection function and pass selection to main program
    # Based on menu selection:
        # Match view
            # Call list_names function
            # Ask user to return to main menu or quit
        # Match add
            # Call get_new_student_function
            # append new dictionary to original dictionary
            # Ask user to return to main menu or quit
        # Match quit
            # flag_variable set to terminate loop

data = [
  { "name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow" },
  { "name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza" },
  { "name": "Julia", "hometown": "Houston", "favorite_food": "shrimp" }
]

def list_names(data):
    for items in data:
        print(f"{data.index(items) + 1}. {items.get("name")}")

def get_new_student():
    new_name = input("What is the name of the new student? ")
    new_town = input("What is the hometown of the new student? ")
    new_food = input("What is the new student's favorite food? ")
    new_student = {
        "name": f"{new_name}", "hometown": f"{new_town}", "favorite_food": f"{new_food}"
    }
    return new_student
    # print(new_student)

return_to_main = True

while return_to_main:
    print("Welcome to the GC Student Database!")
    selection = input("Please select which action you'd like to take: add, view, or quit ")
    selection = selection.lower()
    match selection:
        case 'add':
            new_list = get_new_student()
            data.append(new_list)
            print("Student successfully added to database!")
            print()
        case 'view':
            list_names(data)
            selection_type_valid = False
            while selection_type_valid == False:
                try:
                    selection_type = int(input(f"Which student would you like to learn more about? Select 1) to select by number or 2) to select by name: "))
                    selection_type_valid = True
                except:
                    print("Please enter a valid option!")
            match selection_type:
                case 1:
                    student_selection_valid = False
                    while student_selection_valid == False:
                        try:
                            student_selection = int(input(f"Please select student by number shown from 1-{len(data)}: "))
                            student_selection_valid = True
                        except:
                            print("Please enter a valid option!")
                    if student_selection <= 0 or student_selection > len(data):
                        print("Invalid selection!")
                        student_selection = int(input(f"Please select student by number shown from 1-{len(data)}: "))
                    elif type(student_selection) is not int:
                        print("Invalid selection!")
                        student_selection = int(input(f"Please select student by number shown from 1-{len(data)}: "))
                    else:
                        print("Student {0} is {1}. What would you like to know?".format(student_selection, data[student_selection - 1].get("name")))
                        info_selection = ""
                        while info_selection != 'hometown' or info_selection != 'favorite food':
                            info_selection = input("Enter 'hometown' or 'favorite food': ").lower()
                            if info_selection == 'hometown':
                                print("{0} is from {1}".format(data[student_selection - 1].get("name"), data[student_selection - 1].get("hometown")))
                                print()
                                return_to_main = input("Return to main menu? (y/n)")
                                if return_to_main == 'y':
                                    break
                            elif info_selection == 'favorite food':
                                print("{0}'s favorite food is {1}".format(data[student_selection - 1].get("name"), data[student_selection - 1].get("favorite_food")))
                                print()
                                return_to_main = input("Return to main menu? (y/n)")
                                if return_to_main == 'y':
                                    break
                            else:
                                print("Invalid input!")
                                print()
                case 2:
                    name_list = []
                    for x in data:
                        name_list.append(x.get("name"))
                    student_search_valid = False
                    while student_search_valid == False:
                        student_search = input("Please enter the name of the student you're searching for: ").capitalize()
                        if student_search in name_list:
                            student_index = name_list.index(student_search)
                            student_search_valid = True
                        else:
                            print("Student not in database! Please try again!")
                    print("{0} is Student {1}. What would you like to know?".format(student_search, student_index + 1))
                    info_selection = ""
                    while info_selection != 'hometown' or info_selection != 'favorite food':
                        info_selection = input("Enter 'hometown' or 'favorite food': ").lower()
                        if info_selection == 'hometown':
                            print("{0} is from {1}".format(student_search, data[student_index].get("hometown")))
                            print()
                            return_to_main = input("Return to main menu? (y/n)")
                            if return_to_main == 'y':
                                break
                        elif info_selection == 'favorite food':
                            print("{0}'s favorite food is {1}".format(student_search, data[student_index].get("favorite_food")))
                            print()
                            return_to_main = input("Return to main menu? (y/n)")
                            if return_to_main == 'y':
                                break
                        else:
                            print("Invalid input!")
                            print()
                case _:
                    print("Please select 1 or 2 to determine your search option!")
                    print()
                    selection = 'view'
        case 'quit':
            print("Goodbye!")
            return_to_main = False
        case _:
            print("Invalid selection! Please try again!")
            print()