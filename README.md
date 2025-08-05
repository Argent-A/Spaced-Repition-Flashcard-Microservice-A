

## **How to request data from the microservice:**

Main app will write comma seperated values file into 'project/FlashcardData Microservice Input' folder.

with open('FlashcardData Microservice Input/Flashcard Data.txt', 'w') as output_file:
    output_file.write(data)

Once the file written, main app will can make subprocess run to microservice A to initate the microservice script. This is preferable to having it run on loop looking for new files as it wastes less resources. 
Main app does not need to give the filename a specific name, the microservice will just read in the latest file that was written to the directory specified above. 

you can directly run the microservice by <microservice_A.py> - replace with your own filename for the service. : 
subprocess.run(["python", "microservice_A.py"])



Main app needs to write csv file with columns (front of card), (level), (score) : data types, str, int, int
Microservice will read this file as a .txt file, reading only the latest file that was written to the folder: 

example code: 

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




## **How to recieve data from the microservice:**
Once the microservice has run the output file is a txt file with values in csv format, able to be consumed by the main service. In this scenario I used the pandas module to read the csv file: 

os.chdir(os.getcwd() + "\\FlashcardData Microservice Output") 
os.listdir()
df = pd.read_csv('processed_Flashcard Data.txt')



<img width="805" height="662" alt="image" src="https://github.com/user-attachments/assets/0e0bb31e-7909-4315-92e6-887c5330a004" />
