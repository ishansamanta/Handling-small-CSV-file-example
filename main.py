f = open("mytxtfile.txt", "r")
i = 0
while True #infinite loop
  i=i+1 #increment student counter
  line= f.readline() #Scans the line
  if not line:
    break
  m1= line.strip().split(",")[0] #extracts first mark of subject1 from student{i}
  m2= line.strip().split(",")[1] #extracts second mark of subject2 from student{i}
  m3= line.strip().split(",")[3] #extracts third mark of subject3 from student{i}
  print(f" Marks of student{i} : Subject1 = {m1}, Subject2 = {m2}, Subject3 = {m3})
