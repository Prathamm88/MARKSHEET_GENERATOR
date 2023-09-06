institute=input("ENTER THE NAME OF INSTITUTE : ")
name=input("ENTER THE NAME OF THE STUDENT : ")
reg_no=input("ENTER THE REGISTRATION NUMBER :  ")
roll_no=input("ENTER THE ROLL NUMBER :  ")
maths=float(input("ENTER MARKS OBTAINED IN MATHS :"))
physics=float(input("ENTER MARKS OBTAINED IN PHYSICS: "))
civil=float(input("ENTER MARKS OBTAINED IN CIVIL: "))
cs =float(input("ENTER MARKS OBTAINED IN CS: "))
bme=float(input("ENTER MARKS OBTAINED IN BME: "))
practical1=float(input("ENTER MARKS OBTAINED IN PRACTICLE 1: "))
practical2=float(input("ENTER MARKS OBTAINED IN PRACTICLE 2: "))
practical3=float(input("ENTER MARKS OBTAINED IN PRACTICLE 3: "))
grand_total=maths+physics+civil + cs + bme + practical1+practical2+practical3

print("---------------------------------------------------------------------------------------------------------------------")


print(f'''                                                  {institute}


        Name = {name}                               Course = B.TECH
        ROLL NO. = {roll_no}                            Reg. No = {reg_no}                                  
         
 
          subject name         | subject code          |     Max. Marks     |         Marks Obtained          
                               |                       |                    |
            Maths              | 1fy1-23               |         100        |            {maths}
            physics            | 1fy1-24               |         100        |            {physics}
            civil              | 1fy1-25               |         100        |            {civil}
            CS                 | 1fy1-26               |         100        |            {cs}                                
            practical 1        | 1fy1-27               |         100        |            {practical1}                        
            Practical 2        | 1fy1-28               |         100        |            {practical2}                        
            Practical 3        | 1fy1-29               |         100        |            {practical3}   
            -----------------------------------------------------------------------------------------------------------------                      
            Grand Total                                |         800        |            {grand_total} ''')                  
print("---------------------------------------------------------RESULT-------------------------------------------------------")
result=(grand_total/800)*100
print((f"YOUR PERCENTAGE IS : {result:.2F} %"))

if result > 95 and result <= 100 :
  print( 'Pass \nGrade = A+')
elif result > 85 and result <95 :
  print ('Pass \nGrade = A')
elif result >75 and result < 85:
  print('Pass \nGrade = B+')
elif result > 65 and result <75 :    
  print('Pass \nGrade = B')
elif result > 55 and result <65 :
  print('Pass \nGrade = C')
elif result >35 and result <55:
  print('Pass \nGrade = D')
elif result >0 and result < 35 :
  print('YOU ARE FAIL.')
else:
  print("INVALID !")


print("-----------------------------------------------------------------! Press ENTER  to exit !---------------------------")
