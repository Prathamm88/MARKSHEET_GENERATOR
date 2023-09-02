institute=input("enter name of the institute: ")
name=input("enter name of the student: ")
reg_no=input("enter the registration number of the student: ")
course=input("enter the course: ")
maths=float(input("enter marks obtained in maths :"))
physics=float(input("enter marks obtained in physics: "))
civil=float(input("enter marks obtained in civil: "))
cs =float(input("enter marks obtained in cs: "))
bme=float(input("enter marks obtained in bme: "))
practical1=float(input("enter marks obtained in practical 1: "))
practical2=float(input("enter marks obtained in practical 2: "))
practical3=float(input("enter marks obtained in practical 3: "))
grand_total=maths+physics+civil + cs + bme + practical1+practical2+practical3




print(f'''                           \t{institute}              
         Name={name}                                       Course={course}
         Reg. No={reg_no}
 
          subject name        subject code                  Max. Marks             Marks Obtained          
 
            Maths               1fy1-23                     100                     {maths}
            physics             1fy1-24                     100                     {physics}
            civil               1fy1-25                     100                     {civil}
            CS                  1fy1-26                     100                     {cs} 
            practical 1         1fy1-27                     100                     {practical1}
            Practical 2         1fy1-28                     100                     {practical2}
            Practical 3         1fy1-29                     100                     {practical3}
            Grand Total                                     800                     {grand_total} ''')
               
result=(grand_total/800)*100
if result<33:
  print((f"Fail with {result} percentage"))
else:
  print((f"Pass with {result} percentage"))
if result > 95 and result <= 100 :
  print( 'Grade = A+')
elif result > 85 and result <95 :
  print ('Grade = A')
elif result >75 and result < 85:
  print('Grade = B+')
elif result > 65 and result <75 :    
  print('Grade = B')
elif result > 55 and result <65 :
  print('Grade = C')
elif result >45 and result <55:
  print('Grade = D')
elif result >35 and result < 45 :
  print('Grade = E')
else:
  print("fail")