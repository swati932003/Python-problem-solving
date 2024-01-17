# WATCH COCO
# ask user's name and age
# if user's name start with ('a' or'A') and age is abouve 10 then
# print 'you can watch coco movie'
# else print sorry, you cannot watch coco

name = input(" enter your name  : ")
age =  int (input(" enter your age :"))
if (name[0]=='a' or 'A') and age >=10 :
    print( "you can watch coco movie")
else :
    print( " sorry, you cannot watch coco movie")
