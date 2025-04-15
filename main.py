#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
f_invited_names=open("Input/Names/invited_names.txt",mode="r")
name_list=f_invited_names.readlines()
for item in name_list:
    letter_template=open("Input/Letters/starting_letter.txt",mode="r")
    contents=letter_template.read()
    x=contents.replace("[name]",item.strip())

    final_letter=open(f"Output/ReadyToSend/letter_for_{item}.docx",mode="w")
    final_letter.write(x)

