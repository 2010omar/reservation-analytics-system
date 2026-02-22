services = [    'اصدار رخصة سيارة اول مرة',
    'تجديد رخصة سيارة',
    'اصدار رخصة قيادة اول مرة',
    'تجديد رخصة قيادة',
    'اصدار بدل فاقد'
]
new_car_id = [
    ["13-04-2025", "Sunday",    [4, 6, 7, 8, 1]],
    ["14-04-2025", "Monday",    [2, 1, 8, 6, 4]],
    ["15-04-2025", "Tuesday",   [3, 1, 6, 6, 4]],
    ["16-04-2025", "Wednesday", [1, 6, 9, 8, 3]],
    ["17-04-2025", "Thursday",  [4, 7, 7, 10, 1]]
]

renew_car_id = [
    ["13-04-2025", "Sunday",    [4, 9, 7, 7, 1]],
    ["14-04-2025", "Monday",    [3, 1, 7, 7, 3]],
    ["15-04-2025", "Tuesday",   [3, 5, 9, 10, 2]],
    ["16-04-2025", "Wednesday", [3, 6, 6, 9, 1]],
    ["17-04-2025", "Thursday",  [1, 2, 9, 8, 4]]
]

new_driving_license = [
    ["13-04-2025", "Sunday",    [2, 4, 9, 6, 2]],
    ["14-04-2025", "Monday",    [2, 6, 8, 8, 1]],
    ["15-04-2025", "Tuesday",   [4, 5, 6, 8, 2]],
    ["16-04-2025", "Wednesday", [3, 10, 6, 10, 1]],
    ["17-04-2025", "Thursday",  [2, 5, 10, 6, 2]]
]

renew_driving_license = [
    ["13-04-2025", "Sunday",    [2, 6, 10, 8, 4]],
    ["14-04-2025", "Monday",    [1, 3, 7, 7, 4]],
    ["15-04-2025", "Tuesday",   [2, 6, 10, 6, 1]],
    ["16-04-2025", "Wednesday", [2, 10, 7, 8, 1]],
    ["17-04-2025", "Thursday",  [2, 7, 7, 7, 1]]
]

lost_id = [
    ["13-04-2025", "Sunday",    [1, 3, 9, 8, 3]],
    ["14-04-2025", "Monday",    [3, 9, 6, 6, 4]],
    ["15-04-2025", "Tuesday",   [4, 7, 8, 7, 3]],
    ["16-04-2025", "Wednesday", [3, 9, 6, 9, 4]],
    ["17-04-2025", "Thursday",  [2, 4, 10, 7, 1]]
]

# calculate the  mean
def calculate_mean(data):
    filter_slots = []
    for i in data:
        for m in i[2]:
            filter_slots.append(m)
    return sum(filter_slots) / 25
mean_ = calculate_mean(new_car_id)


# calculate maximum slot
def calculate_max(data):
    filter_slots = []
    for i in data:
        for m in i[2]:
            filter_slots.append(m)
    return max(filter_slots)
max_ = calculate_max(new_car_id)

# calculate minimum slot
def calculate_min(data):
    filter = []
    for i in data:
        for m in i[2]:
            filter.append(m)
    return min(filter)
min_ = calculate_min(new_car_id)

# calculate most crowded day and number of resrvation
def most_busy(data):
    filter = []
    for day in data:
        total = sum(day[2])
        name = day[1]
        filter.append([total, name])
    return max(filter)
busy_day= most_busy(new_car_id)[1]
busy_total = most_busy(new_car_id)[0]


# calculate leest crowded day and number of reservation
def least_busy(data):
    filter = []
    for day in data:
        total = sum(day[2])
        name = day[1]
        filter.append([total, name])
    return min(filter)
least_day = least_busy(new_car_id)[1]
least_total = least_busy(new_car_id)[0]


print("Service data")
print("")
print(f"Mean = {mean_}")
print("")
print(f"Maximum reservation slot= {max_}")
print("")
print(f"Minimum reservation slot= {min_}")
print("")
print(f"Most crowded Day =  {busy_day} ")
print(f"number of reservations =  {busy_total} ")
print("")
print(f"Least crowded Day = {least_day}")
print(f"number of reservations =  {least_total} ")
# this code works with any data but you will have to change every function assiginment
# wich has a soecific paremeter with the list you want
# least_day = least_busy(new_car_id)[1]
# least_total = least_busy(new_car_id)[0]
# (new_car_id) ----> change it to the list you want
#same for all functions
