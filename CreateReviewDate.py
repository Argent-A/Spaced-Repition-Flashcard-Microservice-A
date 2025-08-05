import datetime
import os
import pandas as pd


# --------------- CUSTOM FUNCTIONS ---------------

# feel free to change the review table to modify the review times
review_table = {
    0: 0,  # Now
    1: 1,  # 1 day
    2: 2,  # 2 days
    3: 4,  # 4 days
    4: 8,  # 8 days
    5: 16, # 16 days
    6: 32, # 32 days
    7: 64, # 64 days
    8: 128,# 128 days
    9: 256, # 256 days
    10: None # Never review again!
}


def recalculate_level(level, score):
    '''increments or decrements the level based on the score'''
    if score == 0:
        # if level is 0, it stays at 0
        if level > 0:
            level -= 1
    elif score == 2:
        # if level is 10, it stays at 10
        if level < 10:
            level += 1
    return level
    # note that if the score is 1 the level does not change


def calculate_review_date(level, score):
    '''level = how advanced the card is 0 - 10
    score = how well the card was remembered 0 - 2:
    0 = they dont know, 1 = user hesitated, 2 = user knows it well
    
    Review table:
    if level = 0 then the review date is Now
    if level = 1 then review in 1 day
    if level = 2 then review in 2 days
    if level = 3 then review in 4 days
    if level = 4 then review in 8 days
    if level = 5 then review in 16 days
    if level = 6 then review in 32 days
    if level = 7 then review in 64 days
    if level = 8 then review in 128 days
    if level = 9 then review in 256 days
    if level = 10 then never review again
    
    if score = 0, review time is Now.
    if score = 1, look up the new level and divide the review time by 2.
    if score = 2, look up the new level and review time in the table.
    '''
    # validate inputs - confirm data types and ranges:
    if not isinstance(level, int) or not isinstance(score, int):
        raise TypeError("Both level and score must be integers")
    
    if level < 0 or level > 10:
        raise ValueError("Level must be between 0 and 10")
    
    if score < 0 or score > 2:
        raise ValueError("Score must be between 0 and 2")
    
    
    # calculate the new level based on score
    level = int(recalculate_level(level, score))
    
    current_time = datetime.datetime.now()
    
    # use score to determine review date, return the new level and review date
    if score == 0:
        return [level, current_time]
    elif score == 1 and level < 10:
        return [level, current_time + datetime.timedelta(days=(review_table[level] // 2))]
    elif score == 2 and level < 10:
        return [level, current_time + datetime.timedelta(days=(review_table[level]))]
    elif level == 10:
        return [level, "Card Mastered! No further reviews"]


# --------------- MAIN EXECUTION ---------------


# set directories
root_directory = os.getcwd()
input_directory = root_directory + "\\FlashcardData Microservice Input"
output_directory = root_directory + "\\FlashcardData Microservice Output"

# sort directory by modification time and get list of all files in the directory by modification time
files = sorted(os.listdir(input_directory), key=lambda x: os.path.getmtime(os.path.join(input_directory, x)))

# get the most recent file in the directory
if files:
    filename = files[-1]
else:
    raise FileNotFoundError("No files found in the input directory {}".format(os.getcwd()))

# read the file from the input directory
with open(os.path.join(input_directory, filename), 'r') as file:
    lines = file.readlines()

# create a DataFrame from the file, we assume its a txt file in csv format, or a .csv file. This function should be able to do both. 
# use first row of the file as column names
colnames = lines[0].strip().split(',')

# use the pandas module to create a DataFrame object
# first row as column names and the rest as the data
dataframe = pd.DataFrame([line.strip().split(',') for line in lines[1:]], columns=colnames)

# explicitly convert level and score columns to integers, otherwise pandas infers the data type as string
dataframe['level'] = dataframe['level'].astype(int)
dataframe['score'] = dataframe['score'].astype(int)

# apply the calculate_review_date function to each row in the DataFrame, respectively pull out the new level and review date
result = dataframe.apply(lambda row: calculate_review_date(row['level'], row['score']), axis=1)
dataframe['new_level'] = result.apply(lambda x: x[0])
dataframe['review_date'] = result.apply(lambda x: x[1])

# convert new_level to integer type
dataframe['new_level'] = dataframe['new_level'].astype(int)


# write the data to a new directory as a new file. 
output_filename = f"processed_{filename}"
output_path = os.path.join(output_directory, output_filename)

# ensure output directory exists, exits_ok = True means it will not raise an error if the directory already exists
os.makedirs(output_directory, exist_ok=True)

# write the DataFrame to txt file in csv format
dataframe.to_csv(output_path, index=False)
