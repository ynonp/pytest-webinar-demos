class Greeter:
    def hi(self):
        print("Hello World")

    def years_to_months(self):
        print("How old are you (in years)? ")
        age_in_years = int(input("> "))
        age_in_months = age_in_years * 12
        print(f"Wow that's {age_in_months} months old")

    def get_name(self):
        print("who are you?")
        self.name = input("> ")