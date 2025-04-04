from CNP import *
import csv_writer
from hash_function import *
from random_search import *

if __name__=="__main__":
    cnp_generator(1000000)
    name_attribution(cnp_list)
    csv_writer.write_to_file("people",people_dict)
    for element in cnp_list:
        hash_mapper(element)
    target_list = rand_choice_1000(cnp_list)
    random.shuffle(target_list)
    random.shuffle(hash_map)
    for value in target_list:
        linear_search(value, hash_map)

