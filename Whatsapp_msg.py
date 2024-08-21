import pywhatkit
Mob_numb = input("Enter the mobile number with country code: ")
# b=input("enter the message you want to deliver: ")
pywhatkit.sendwhatmsg_instantly(f"{Mob_numb}",
                      input("Enter the meassage you want to deliver: "))