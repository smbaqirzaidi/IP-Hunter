import requests
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
  
    print(Fore.RED + Style.BRIGHT + """
    __                                    
   / /  |      /  |           /             
  ( (___| ___ (___|      ___ (___  ___  ___ 
  | |         |   )|   )|   )|    |___)|   )
  | |         |  / |__/ |  / |__  |__  |    
                                          """)

   
    print(Fore.WHITE + "----------------------------------")
    print(Fore.WHITE + "       IP Address Lookup")
    print(Fore.WHITE + "----------------------------------\n")

def get_ip_details(ip_address):
   
    api_url = f"https://ipinfo.io/{ip_address}/json"
    
    try:
   
        response = requests.get(api_url)
        
      
        if response.status_code == 200:
            data = response.json()
            
         
            ip = data.get('ip', 'Not available')
            hostname = data.get('hostname', 'Not available')
            city = data.get('city', 'Not available')
            region = data.get('region', 'Not available')
            country = data.get('country', 'Not available')
            loc = data.get('loc', 'Not available')  
            org = data.get('org', 'Not available') 
            isp = data.get('org', 'Not available') 
            usage_type = "Residential" 

           
            print(f"IP Address: {ip}")
            print(f"Country: {country}") 
            print(f"Hostname: {hostname}")
            print(f"Location: {city}, {region}, {country}")
            print(f"Coordinates: {loc}")
            print(f"ISP/Organization: {org}")
            print(f"Usage Type: {usage_type}")
        else:
            print("Error: Unable to fetch details.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

### Main Program
print_banner() 
ip_address = input("Enter an IPv4 address to lookup: ")
get_ip_details(ip_address)
