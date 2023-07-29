class HelloTriangular:

    # Recursive function that generates 'Hellos' from 1 to num if direction == "crescent" and backwards from num to 1 if == "decrescent"
    def generate_hello_triangular(self, num, direction, a=0):
        
        Hello_end_string = "Hello!\n"            
        Hello_string = "Hello! "
        
        if direction == "crescent":                              
            if num <= 0 or num - a <= 0:
                return ""
            else:
                return (a)*(Hello_string) + Hello_end_string + self.generate_hello_triangular(num, direction, a+1)
        
        if direction == "decrescent":
            if num <= 0:
                return ""
            else:
                return (num-1)*(Hello_string) + Hello_end_string + self.generate_hello_triangular(num-1, direction)
    def check_user_input(self):
        while True:
            try:
                num = int(input("How many times do you want to say hello to everyone (triangularly)?\n"))       
            except ValueError:
                print("\nThis is not an integer.\n")
                continue
            else:
                return num 

# Program run with user input#
if __name__ == "__main__":                      
    num = 1
    h = HelloTriangular()
    while num > 0:
        num = h.check_user_input()
        print("\n", h.generate_hello_triangular(num, "crescent")+h.generate_hello_triangular(num-1, "decrescent"), sep="")
