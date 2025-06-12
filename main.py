# Hello world!
# The power of love is a curious thing
# Making one man weep
# And another man sing
#It is is Friday, I am in love.
import seaborn as sns
import matplotlib.pyplot as plt

# Load a built-in dataset
tips = sns.load_dataset("tips")

# Create a simple scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)

plt.show()
sns.get_dataset_names()



"""
# Stage ALL changes, including new and modified files
git add .

# Commit them with a message
git commit -m "Add notebook and plot.py, update index.html and main.py"

# Push to GitHub
git push
https://docs.google.com/presentation/d/1Pr4b3cRc8W9yNH_CUHE3crgbH1RmySqyZG5fDxRvy_Q/edit?slide=id.g301fed9a61c_0_0#slide=id.g301fed9a61c_0_0



git add .
git commit -m "your message"
git push

import random
for i in range(1, 100):
    print(i)
for j in range(-5,5):
    print(j)
    import random
number = random.randint(1, 10)  # Generates a random integer between 1 and 10, inclusive
print(number)

import random
number = random.randint(1, 10)  # Generates a random integer between 1 and 10, inclusive
print(number)
my_list = [1, 2, 3]
print(len(my_list))  # Output: 3

my_string = "hello"
print(len(my_string))  # Output: 5

my_dict = {"a": 1, "b": 2}
print(len(my_dict))  # Output: 2
"""
my_string = "hello"
print(len(my_string))