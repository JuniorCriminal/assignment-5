a=input("Enter the student's name:")

result = {"Alice":85,
           "Bob":80,
           "Charlie":76,
           "David":96,
           "Eve":60,
           }
if a in result:
    print("{}'s marks:{}".format(a,result[a]))
else:
    print("student not found.")