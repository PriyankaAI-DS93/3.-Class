class allFunctions():
    def SubfieLds():
        lists='Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing'
        print("Subfields in AI are:")   
        len(lists)
        for temp in range(len(lists)):
            print(lists[temp])
            
    def OddEven():
        num=int(input("Enter a number"))
        if num%2==1:
            print(num, "is Odd number")
        else:
            print(num, "is Even number")

    def Eligible():
        gender=input("Your Gender")
        age=int(input("Your Age"))
        if gender=="Male":
            if age<21:
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        if gender=="Female":
            if age<18:
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")

    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        print("Total:", total)
        percentage=total/5
        print("Percentge:", percentage)

    def traingle():
        height=int(input("Height="))
        breadth=int(input("Breadth="))
        area=(height*breadth)/2
        print("Area formula:(Height*Breadth)/2")
        print("Area of trainlge", area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        perimeter=(height1+height2+breadth)
        print("Perimeter formula: Height1+Height2+Breath3")
        print("Perimeter of Traingle:", perimeter)    


    