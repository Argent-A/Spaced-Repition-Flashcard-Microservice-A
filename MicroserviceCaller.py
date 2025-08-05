import os
import subprocess
import pandas as pd

print("Main program will write user data, this is mimicking that part of the process.")
print(f"writing file {'Flashcard Data.txt'} to {os.getcwd() + '\\FlashcardData Microservice Input'}")



print("Microservice A is processing the file:")
result = subprocess.run(["python", "CreateReviewDate.py"], capture_output=True, text=True)

# if there were any issues with subprocess, print the error
if result.returncode != 0:
	print(f"Error running microservice: {result.stderr}")
	exit(1)


print("Microservice A has finished processing the file.")

os.chdir(os.getcwd() + "\\FlashcardData Microservice Output")  # Change directory to the parent directory
os.listdir()
df = pd.read_csv('processed_Flashcard Data.txt')

print("Processed DataFrame:")
print(df)
