# Python program to demonstrate 
# filecmp.cmp() method  
    
import filecmp 
  
def compare(file1, file2):  
      
    # compare contents of both files with shallow = False
    comp = filecmp.cmp(file1, file2, shallow = False) 
      
    # Print the result of comparison 
    print(comp) 

# Use for direct compare
# comment out or delete if exporting to script
# compare("path/to/file1","path/to/file2")