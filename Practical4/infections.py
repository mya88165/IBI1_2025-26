# Set starting number of infected students
# Set growth rate
# Set class size
# Set day counter
# Repeat while not everyone is infected
#   print current day and number infected
#   update infected number using growth rate
#   increase day counter
# Print final day and total days taken

infected = 5
growth_rate = 0.40
class_size = 91
day = 1

while infected < class_size:
    print("Day", day, ":", infected, "students infected")
    infected = infected + infected * growth_rate
    day = day + 1

print("Day", day, ":", infected, "students infected")
print("It took", day, "days to infect the whole class.")