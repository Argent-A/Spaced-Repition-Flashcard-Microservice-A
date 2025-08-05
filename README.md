

## **How to request data from the microservice:**

Main app will write comma seperated values file into 'project/FlashcardData Microservice Input' folder.

    with open('FlashcardData Microservice Input/Flashcard Data.txt', 'w') as output_file:
        output_file.write(data)

Once the file written, main app can make subprocess run to microservice A to initate the microservice script. This is preferable to having it run on loop looking for new files as it wastes less resources. 
Main app does not need to give the filename a specific name, the microservice will just read in the latest file that was written to the directory specified above. 

you can directly run the microservice by <microservice_A.py> - replace with your own filename for the service. : 

    subprocess.run(["python", "microservice_A.py"])

or you can just have the main app wait on a loop until it sees that a file is written into the output folder (root_directory + "\\FlashcardData Microservice Output")

Main app needs to write csv file with columns [(front of card), (level), (score) : data types, str, int, int] to directory : root_directory + "\\FlashcardData Microservice Input"
Microservice will read this file as a .txt file, reading only the latest file that was written to the folder in case the main app writes many files to that directory: 

example code of microservice reading the input file: 

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
Once the microservice has run the output file is a txt file with values in csv format, able to be consumed by the main service. In this scenario I used the pandas module to read the output file from the microservice: 

    os.chdir(os.getcwd() + "\\FlashcardData Microservice Output") 
    os.listdir()
    df = pd.read_csv('processed_Flashcard Data.txt')

This data is a csv format of the negotiated output, the main app can now consume it for its main logic. 

<img width="821" height="640" alt="Screenshot 2025-08-04 233202" src="https://github.com/user-attachments/assets/25def942-a358-49cc-92c3-77391e170594" />



