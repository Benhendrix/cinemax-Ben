
def valideer_getal(bereik):
    while True:
        invoer = input()
        try:
            invoer = int(invoer)
        except ValueError:
            return False
        else:
            if invoer not in bereik:
                return False
            else:
                return invoer
