# Python OOP Challenge: Digital Pet
# Tests the Pet class by creating a pet and calling its methods

from pet import Pet

# Create a new pet named "Buddy"
pet = Pet("Buddy")

# Test all methods, including bonus ones
print("=== Testing Buddy the Pet ===")
print(pet.get_status())  # Show initial status
print()

print(pet.eat())         # Feed Buddy
print(pet.get_status())  # Show status after eating
print()

print(pet.play())        # Play with Buddy
print(pet.get_status())  # Show status after playing
print()

print(pet.sleep())       # Let Buddy sleep
print(pet.get_status())  # Show status after sleeping
print()

print(pet.train("sit"))   # Train Buddy to sit
print(pet.train("roll over"))  # Train Buddy to roll over
print(pet.show_tricks())  # Show Buddy's tricks
print()

print(pet.play())        # Play again to test further changes
print(pet.get_status())  # Final status
print("=== Test Complete ===")