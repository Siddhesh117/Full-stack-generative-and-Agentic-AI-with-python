# You're building a ticket ifo system for railway app.
# Based on seat type, show its features.

# Task:
#  - Input: "sleeper", "AC", "general", "luxury"
#  - Match using match-case
#  - Unknown -> show: "Invalid seat type"

seat_type = input("Enter seat type (sleeper/AC/General/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")                