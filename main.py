import cd
import oem
import office97

print("Available options:")
print("1. CD Key")
print("2. OEM Key")
print("3. Office 97 Key")
print("4. Quit")
sel = input("Select an option: ")
if sel == "1":
    print("\nCD Key: " + cd.cd())
elif sel == "2":
    print("\nOEM Key: " + oem.oem())
elif sel == "3":
    print("\nOffice 97 Key: " + office97.office97())

