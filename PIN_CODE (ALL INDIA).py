from colorama import Fore, Style, init
init()
import requests

while True:          

    print(Fore.MAGENTA + "=" * 60)
    print("🇮🇳           INDIAN PIN CODE FINDER           🇮🇳".center(60))
    print("=" * 60)

    print(Fore.LIGHTWHITE_EX + """
╔════════════════════════════╗
║          PIN CODE          ║
╠════════════════════════════╣
║ 1. PIN Code Lookup         ║
║ 2. City Lookup             ║
║ 3. Exit                    ║
╚════════════════════════════╝
""")

    print(Style.RESET_ALL)

    choice = input("Enter Your Choice (1/2/3): ")

    # PIN CODE LOOKUP 

    if choice == "1":

        pin = input("Enter Your PIN Code: ")

        url = f"https://api.postalpincode.in/pincode/{pin}"

        try:
            response = requests.get(
                url,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            data = response.json()

            if data[0]["Status"] == "Success":

                print("\n✅ PIN Code Found\n")

                for office in data[0]["PostOffice"]:
                    print("📮 Post Office :", office["Name"])
                    print("📍 District    :", office["District"])
                    print("🌍 State       :", office["State"])
                    print("🇮🇳 Country    :", office["Country"])
                    print("📌 PIN Code    :", office["Pincode"])
                    print("-" * 35)

            else:
                print(Fore.RED + "❌ Invalid PIN Code")
                print(Style.RESET_ALL)

        except requests.exceptions.RequestException as e:
            print(Fore.RED + "❌ API Connection Error")
            print(e)
            print(Style.RESET_ALL)

    # CITY LOOKUP 

    elif choice == "2":

        city = input("Enter City Name: ").strip()

        url = f"https://api.postalpincode.in/postoffice/{city}"

        try:
            response = requests.get(
                url,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            data = response.json()

            if data[0]["Status"] == "Success":

                print(f"\n📍 PIN Codes for {city.title()}\n")

                for office in data[0]["PostOffice"]:
                    print(f"📮 {office['Pincode']} - {office['Name']}")
                    print(f"District : {office['District']}")
                    print(f"State    : {office['State']}")
                    print("-" * 35)

            else:
                print(Fore.RED + "❌ City not found.")
                print(Style.RESET_ALL)

        except requests.exceptions.RequestException as e:
            print(Fore.RED + "❌ API Connection Error")
            print(e)
            print(Style.RESET_ALL)

    # EXIT 

    elif choice == "3":
        print(Fore.YELLOW + "👋 Exiting the program...")
        print(Fore.GREEN + "🙏 Thank You for using Indian PIN Code Finder.")
        print(Style.RESET_ALL)

    choice_exit = input("Do you want to exit? (y/n): ").strip().lower()
    if choice_exit == "y":
        break

    # INVALID CHOICE 

    else:
        print(Fore.RED + "❌ Invalid Choice")
        print(Style.RESET_ALL)
