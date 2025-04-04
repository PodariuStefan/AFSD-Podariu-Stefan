import random
from weights import *

#ASSUME DS:data, CS:code

# data for generator
cnp_list = []
months1 = [1, 3, 5, 7, 8, 10, 12] # months with 31 days
months2 = [4, 6, 9, 11] # Months with 30 days
february = [28, 29]
regions = []
outliers = (51, 52)
cnp_constant = "279146358279"
for n in range(1,41):
    regions.append(n)
regions.extend(outliers)
# data ends

#data for name attribution
from faker import Faker
fake = Faker("ro_RO")
global people_dict
people_dict = {}

# data ends
# code segment
def cnp_generator(ammount):
    while ammount:
        gender_index_pool = [1, 2, 5, 6]
        verifying_digits = []
        index = 0
        
        #Anul
        millennium = random.choices((19, 20), weights_age, k=1)
        if millennium[0] == 19:
            gender_index_pool = gender_index_pool[:2]
            year_sector = random.randrange(0, 26)
        else:
            gender_index_pool = gender_index_pool[2:]
            year_sector = random.randrange(0, 100)

        if year_sector < 10:
            year_to_be_used = "0" + str(year_sector)
        else:
            year_to_be_used = str(year_sector)
        # Luna
        month_sector = random.randrange(1, 13)
        if month_sector < 10:
            month_to_be_used = "0" + str(month_sector)
        else:
            month_to_be_used = str(month_sector)

        #Ziua
        if month_sector in months1:
            day_sector = random.randrange(1, 32)
        elif month_sector in months2:
            day_sector = random.randrange(1, 31)
        else:
            day_sector = random.randrange(1, 30)

        if day_sector <10:
            day_to_be_used = "0" + str(day_sector)
        else:
            day_to_be_used = str(day_sector)

        #Sexul
        gender_region = random.choices(gender_index_pool,weights_gender, k=1)
        gender_to_be_used = str(gender_region[0])

        #Județ
        random_region = random.choices(regions, weights_region, k=1)
        if random_region[0] < 10:
            region_to_be_used = "0" + str(random_region[0])
        else:
            region_to_be_used = str(random_region[0])

        #Numar secvential
        secvential_section = random.randrange(1,1000)
        if secvential_section < 10:
            secvential_to_be_used = "00" + str(secvential_section)
        elif secvential_section < 100:
            secvential_to_be_used = "0" + str(secvential_section)
        else:
            secvential_to_be_used = str(secvential_section)

        cnp_to_be_used_ver = f"{gender_to_be_used}{year_to_be_used}{month_to_be_used}{day_to_be_used}{region_to_be_used}{secvential_to_be_used}"

        #Numar de control
        for digit in range(len(cnp_to_be_used_ver)):
            summed_index = int(cnp_to_be_used_ver[digit]) * int(cnp_constant[index])
            verifying_digits.append(summed_index)
            index += 1
        compare_num = sum(verifying_digits)
        if compare_num % 11 < 10:
            control_num = str(compare_num % 11)
        else:
            control_num = "1"
        cnp_list.append(f"{cnp_to_be_used_ver}{control_num}")

        ammount -= 1
    return cnp_list

def name_attribution(lst):
    for elements in lst:
        random_name = fake.name()
        people_dict.update({elements:random_name})