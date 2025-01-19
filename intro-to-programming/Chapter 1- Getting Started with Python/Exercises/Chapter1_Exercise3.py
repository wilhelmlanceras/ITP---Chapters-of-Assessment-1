from datetime import datetime

now = datetime.now()

print("Current date:", now.strftime("%Y-%m-%d"))
print("Current time:", now.strftime("%H:%M:%S"))