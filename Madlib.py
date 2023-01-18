#Madlib is a group of sentences with blanks in between. The blank should be filled with any word.
print("Today is the day the take my life _______. I have many ________ to do such as ___________, _______, __________. Need to \
    ________ for jobs. Designation __________.")

print("\nStart the Madlib")
verb1=input()
verb2=input()
noun1=input()
noun2=input()
noun3=input()
verb3=input()
destination=input()

madlib=f"Today is the day the take my life {verb1}. I have many {verb2} to do such as {noun1}, {noun2}, {noun3}. Need to\
 {verb3} for jobs. Designation {destination}."

print(madlib)