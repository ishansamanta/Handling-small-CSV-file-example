# Handling-small-CSV-file-example(MACHINE LEARNING )
A basic short and beginner friendly code to describe the looping structures and to demonstrate how to handle a small CSV type file containing data. A basic short concept on MACHINE LEARNING
ABOUT THE CODE:
How it processes your data:
Iteration 1:

i becomes 1
readline() reads "12,34,56\n"
Line exists, so continues
Extracts: m1="12", m2="34", m3="56"
Prints: "Marks of student 1: Subject1=12, Subject2=34, Subject3=56"
Iteration 2:

i becomes 2
readline() reads "23,45,68\n"
Line exists, so continues
Extracts: m1="23", m2="45", m3="68"
Prints: "Marks of student 2: Subject1=23, Subject2=45, Subject3=68"
Iteration 3:

i becomes 3
readline() reads "76,43,68\n"
Line exists, so continues
Extracts: m1="76", m2="43", m3="68"
Prints: "Marks of student 3: Subject1=76, Subject2=43, Subject3=68"
Iteration 4:

i becomes 4
readline() returns empty string "" (end of file)
if not line: is True, so break exits the loop
The loop efficiently reads the file line by line until all data is processed, then automatically stops when it reaches the end of the file.
