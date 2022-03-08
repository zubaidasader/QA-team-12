with open('python_code.txt') as f:
    # reading each line    
    for line in f:
   
        # reading each word        
        for word in line.split():

            # Handle what you need to handle. i.e.     
            if word == 'return':
                print(x)