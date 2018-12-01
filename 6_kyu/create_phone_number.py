def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def create_phone_number1(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)
    