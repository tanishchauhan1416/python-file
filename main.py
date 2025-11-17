
rooms = {
    1: {'type': 'Single', 'price': 1000, 'status': 'Available'},
    2: {'type': 'Double', 'price': 1500, 'status': 'Available'},
    3: {'type': 'Suite', 'price': 3000, 'status': 'Available'}
}

bookings = []

def show_rooms():
    print("Room ID  Type    Price   Status")
    for room_id in rooms:
        info = rooms[room_id]
        print(room_id, info['type'], info['price'], info['status'])

def book_room():
    print("Tell me your name:")
    name = input()
    print("Which room do you want to book? Enter room number:")
    try:
        room_id = int(input())
    except:
        print("Invalid input. Please enter a number.")
        return
    if room_id not in rooms:
        print("Room does not exist.")
        return
    if rooms[room_id]['status'] == 'Booked':
        print("Sorry, that room is already taken.")
        return
    print("Enter check-in date (YYYY-MM-DD):")
    check_in = input()
    print("Enter check-out date (YYYY-MM-DD):")
    check_out = input()
    rooms[room_id]['status'] = 'Booked'
    booking = {'name': name, 'room_id': room_id, 'check_in': check_in, 'check_out': check_out}
    bookings.append(booking)
    print("You have successfully booked the room!")

def main():
    while True:
        print("\n1. Show Rooms")
        print("2. Book a Room")
        print("3. Exit")
        print("Choose (1, 2 or 3):")
        choice = input()
        if choice == '1':
            show_rooms()
        elif choice == '2':
            book_room()
        elif choice == '3':
            print("Thank you! Goodbye.")
            break
        else:
            print("Oops! That option does not exist. Try again.")

main()
