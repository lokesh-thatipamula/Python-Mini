contacts={}

while True:
    print("Contact Book!")
    print("1.Create Contact")
    print("2.View Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Search Contact")
    print("6.Count Contacts")
    print("7.Exit")

    choice=input("Enter your Choice:")

    if choice == '1':
        name=input("Enter your Name:")
        if name in contacts:
            print(f"Contact Name {name}, Already Exists")
        else:
            age=input("Enter your Age:")
            mobile=input("Enter your Mobile Number:")
            email=input("Enter your Email ID:")
            contacts[name] = {'age':int(age), 'mobile':mobile, 'email':email}
            print(f"Contact Name {name} has been created succesfully!")

    elif choice == '2':
        name=input("Enter Contact Name to View:")
        if name in contacts:
            contact=contacts[name]
            print(f"Name:{name}, Age:{age}, Mobile:{mobile}, Email:{email}")
        else:
            print(f"Contact name {name} is not Found!")
    
    elif choice == '3':
        name=input("Enter Contact Name to be Updated:")
        if name in contacts:
            age=input("Enter updated Age:")
            mobile=input("Enter updated Mobile Number:")
            email=input("Enter updated Email ID:")
            contacts[name] = {'age':int(age), 'mobile':mobile, 'email':email}
            print(f"Contact Name {name} has been updated succesfully!")
        else:
            print(f"Contact name {name} is not Found!")

    elif choice == '4':
        name=input("Enter Contact Name to be Deleted:")
        if name in contacts:
            del contacts[name]
            print(f"Contact Name {name} has been deleted succesfully!")
        else:
            print(f"Contact name {name} is not Found!")

    elif choice == '5':
        search_name=input("Enter Contact Name to  be Searched:")
        found=False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name:{name}, Age:{age}, Mobile:{mobile}, Email:{email}")
                found=True
        if not found:
            print(f"Contact name {name} is not Found!")

    elif choice == '6':
        print(f"Total contacts in your book:{len(contacts)}")

    elif choice == '7':
        print("GoodBye...Closing the Program")
        break

    else:
        print("Invalid Choice!")