"""
This module contains the main function to demonstrate the Person class functionality.
"""
# Import the Person class from the person module
# person represents the file name or module name 
# Person represents the class name 
# (Take a note of the lowercase 'p' in person and uppercase 'P' in Person)
from person import Person

def main():
    """
    Main function to demonstrate the Person class functionality.
    This function creates a Person object and prints its information.
    """
    # Create a Person object
    alice_obj = Person(name="Alice", age=56, height=165.5, weight=60.0, studying=True)
    
    sohaib_obj = Person(name="Sohaib", age=30, height=180.0, weight=75.0, studying=False)
    
    print(sohaib_obj)

    # Print the person's information
    print(alice_obj)

    # Check if the person is studying
    if sohaib_obj.is_studying():
        print(f"{sohaib_obj.get_name()} is currently studying.")
    else:
        print(f"{sohaib_obj.get_name()} is not studying.")
    
    print(alice_obj.is_old())

if __name__ == "__main__":
    main()