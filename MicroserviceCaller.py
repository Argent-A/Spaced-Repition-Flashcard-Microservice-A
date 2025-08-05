import os
import subprocess
import pandas as pd

print("Main program will write user data, this is mimicking that part of the process.")
print(f"writing file {'Flashcard Data.txt'} to {os.getcwd() + '\\FlashcardData Microservice Input'}")

print("Microservice A is processing the file:")
subprocess.run(["python", "microservice_A.py"])

print("Microservice A has finished processing the file.")

os.chdir(os.getcwd() + "\\FlashcardData Microservice Output")  # Change directory to the parent directory
os.listdir()
df = pd.read_csv('processed_Flashcard Data.txt')

print("Processed DataFrame:")
print(df)