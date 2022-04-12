#school administration form
import csv

def write_to_csv(info_list):
    with open('student_admin.csv','a', newline='') as exl_file:
        writer = csv.writer(exl_file)
        
        if exl_file.tell() == 0:
            #header for the csv file
            writer.writerow(["Name", "Class", "Age", "Contact Number", "Email-ID", "Address"])
                    
        #takes only lists so we use split funciton 
        writer.writerow(info_list)
    
if __name__ == '__main__':
    condition = True
    
    student_num = 1
    
    while (condition):
        student_info = input("enter student info for #{} as shown in the format (Name Class Age Contact_Number Email_ID Address): ".format(student_num))
        #print("Entered student_info is: " + student_info) 
        
        #split 
        student_info_list = student_info.split(' ')
        #print("Entered split up information is:" + str(student_info_list))
        
        print("\n The information you have entered is: \nName: {}\nClass: {}\nAge: {}\nContact Number: {}\nEmail-ID: {}\nAddress: {}"
              .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3], student_info_list[4], student_info_list[5]))
        
        check_data = input("Is this correct data? (yes/no)")
        
        if check_data == "yes":
            write_to_csv(student_info_list)
            
            check =  input("Do you want to add a new student (yes/no): ")
            if check == "yes":
                condition = True
                
                student_num += 1
                
            elif check == "no":
                condition = False
        
        elif check_data == "no":
            print("please re-enter the values!")
        
        
        
        
        
