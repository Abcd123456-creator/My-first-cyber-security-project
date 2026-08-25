import socket

# This is our scanning function
def start_my_scan():
    # We are testing a safe website made for students to practice on
    target_website = "scanme.nmap.org"
    
    # These are the common digital doors (ports) we want to check
    doors_to_check = [22, 80, 443]
    
    print("Checking if the digital doors are locked...")
    print("----------------------------------------")
    
    for door in doors_to_check:
        # This line sets up a network tester
        tester = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tester.settimeout(2.0)
        
        # This line tries to connect to the door
        result = tester.connect_ex((target_website, door))
        
        # If the result is 0, the door is open!
        if result == 0:
            print(f"🔓 Door {door} is OPEN! Anyone can walk in.")
        else:
            print(f"🔒 Door {door} is Closed and Safe.")
            
        # Close the tester
        tester.close()

# Start the program
start_my_scan()
