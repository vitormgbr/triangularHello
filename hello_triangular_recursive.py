class hello:
    
    def hello_triangular_cres(self, num, a=1):  #recursive function that generates 'Hellos' from 1 to num#
                                                ##a is an auxiliary variable used to get the inverse result from hello_triangular_decres##
        Hello_World_end = "Hello!\n"            
        Hello_World = "Hello! "    

        if num <= 0 or num - a <= 0:
            return ""
        else:
            return (a-1)*(Hello_World) + Hello_World_end + self.hello_triangular_cres(num, a+1)

    def hello_triangular_decres(self, num):     #recursive function that generates 'Hellos' from num-1 to 1#

        Hello_World_end = "Hello!\n"
        Hello_World = "Hello! "    

        if num <= 0:
            return ""
        else:
            return (num-1)*(Hello_World) + Hello_World_end + self.hello_triangular_decres(num-1)


if __name__ == "__main__":                      
    num = 1
    h = hello()
    while num > 0:
        num = int(input("How many times do you want to say hello to everyone (triangularly)? \n"))
        print(h.hello_triangular_cres(num)+h.hello_triangular_decres(num))
    
    
