# FILE NAME - grade_converter.py

# NAME: KEVIN LEE
# DATE: 10/8/2025
# BRIEF DESCRIPTION: This program converts numerical grades to letter grades based on a specified scale 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# Display header
print("===== Grade Converter =====")

# Get numerical grade from user
grade = int(input("Enter a numerical grade (1-100): "))

# Convert to letter grade based on the scale
if grade > 100:
    print("A+")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 65:
    print("D")
else:
    print("F")








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

Be very careful with the bracket notation and inequality signs. Pay close attention 
to whether ranges are inclusive or exclusive, as getting the boundaries wrong will 
affect multiple grade conversions.






'''
