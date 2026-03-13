# Set starting number of infected students
# Set growth rate
# Set class size
# Set day counter

infected = 5
growth_rate = 0.40
class_size = 91
day = 1

while infected < class_size: # Repeat while not everyone is infected
    print("Day", day, ":", int(infected), "students infected") # print current day and number infected
    infected = infected + infected * growth_rate # update infected number using growth rate
    day = day + 1 # increase day counter

# Print final day and total days taken
print("It took", day, "days to infect the whole class.")