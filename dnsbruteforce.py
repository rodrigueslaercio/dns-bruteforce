import dns.resolver, os
from datetime import date, datetime

print("If you want to bf subdominons create a file called wordlist.txt in this direcotry.\n")
host = input("Host: ")
path = os.getcwd()

if os.path.exists(path+"/wordlist.txt"):
        os.mkdir(path + "/subdominions")
        
        wordlist = open(path + "/wordlist.txt", "r")
        
        for subdominion in wordlist.read().splitlines():
            new_path = os.path.join(path + "/subdominions", f"{subdominion + "." + host}_ips_{date.today()}_{datetime.now().strftime('%H-%M-%S')}.txt")
            try:
                res = dns.resolver.Resolver()
                result = res.resolve(subdominion + "." + host, "A")
                
                file = open(new_path, "w")
                for ip in result:
                    file.write(f"{subdominion + "." + host} -> {ip}\n")
                file.close()
            except:
                print(f"Host {subdominion + "." + host} does not exist")

else:
    try:
        res = dns.resolver.Resolver()
        result = res.resolve(host, "A")
        
        file = open(f"{host}_ips_{date.today()}_{datetime.now().strftime('%H-%M-%S')}.txt", "w")
        for ip in result:
            file.write(f"{host} -> {ip}\n")
        file.close()
    except:
        print(f"Host {host} does not exist")
