floor = 1
target = int(input())
print(f"Elevator is now on {floor} floor")
while floor != target:
    direction = 1 if target > floor else -1
    floor += direction
    print(f"{floor}" if direction > 0 else f"{floor}")
print("You've reached youre floor")
