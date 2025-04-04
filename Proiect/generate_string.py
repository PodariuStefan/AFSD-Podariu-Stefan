#import random
#from environmental_variables import *#
#
#def column_generator(nums):
#    random_numbers = []
#    for i in range(nums):
#        random_numbers.append(random.randint(10, 200))
#
#    c_height = 400
#    c_width = 512
#    x_width = c_width / (len(nums) + 1)
#    offset = 30#
#
#    for i, height in enumerate(random_numbers):
#        x0 = (i * x_width) + offset
#        y0 = c_height - height
#        x1 = (i + 1) * x_width + offset
#        y1 = c_height
#
#        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
#        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(nums[i]))


