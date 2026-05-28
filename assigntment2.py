
people = int(input("Enter the number of people attending the cookout: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs each person will eat: "))


total_hot_dogs = people * hot_dogs_per_person


hot_dog_packages = total_hot_dogs // 10
if total_hot_dogs % 10 != 0:
    hot_dog_packages += 1

bun_packages = total_hot_dogs // 8
if total_hot_dogs % 8 != 0:
    bun_packages += 1


leftover_hot_dogs = (hot_dog_packages * 10) - total_hot_dogs
leftover_buns = (bun_packages * 8) - total_hot_dogs


print("\nCookout Information")
print("Minimum packages of hot dogs needed:", hot_dog_packages)
print("Minimum packages of hot dog buns needed:", bun_packages)
print("Hot dogs left over:", leftover_hot_dogs)
print("Hot dog buns left over:", leftover_buns)