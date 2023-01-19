boolAns = True
while boolAns:

    print("1. Model Taining\n" +
        "2. Model Testing\n" +
        "3. Translate a Tagalog Document to Ilokano\n" +
        "4. Translate an Ilokano Document to Tagalog\n" +
        "5. Exit\n")
    
    try:
        intChoice = input("Enter your choice: ")
        
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if intChoice=="1": 
      print("\n Model Training Selected")
      
    elif intChoice=="2": 
      print("\n Model Testing Selected")
      
    elif intChoice=="3": 
      print("\n Translate a Tagalog Document to Ilokano Selected")
    
    elif intChoice=="4": 
      print("\n Translate an Ilokano Document to Tagalog Selected")
    
    elif intChoice=="5": 
      print("\n Exit Selected")
      boolAns = False
    
    else:
      print("\n Invalid input. Please enter a number from 1 to 5.")
                  