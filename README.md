

## **How to request data from the microservice:**

Main app will write comma seperated values file into 'project/FlashcardData Microservice Input' folder. 
Once the file written, main app will make a subprocess call to microservice A to initate the microservice script. This is preferable to having it run on loop looking for new files as it wastes less resources. 

call: 
subprocess.run(["python", "microservice_A.py"])

Main app needs to write csv file in this format  with data types, str, int, int: 

front of card,level,score
what is the capital of France?,6,2
what is the capital of China?,5,2
where is Rhodesia located? ,1,2



## **How to recieve data from the microservice:**

Subprocess call will output a variety of value or type errors if there are issues with the input file, such as invalid data types, etc. 
If subprocess successfully runs, it will generate an output file in 'Project\Microservice A\FlashcardData Microservice Output' directory. 

Output file is a txt file with values in csv format, able to be consumed by the main service. 

os.chdir(os.getcwd() + "\\FlashcardData Microservice Output") 
os.listdir()
df = pd.read_csv('processed_Flashcard Data.txt')



<img width="805" height="662" alt="image" src="https://github.com/user-attachments/assets/0e0bb31e-7909-4315-92e6-887c5330a004" />
