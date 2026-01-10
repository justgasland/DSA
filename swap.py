if __name__ == "__main__":
    a = 2
    b = 3
    print("a =", a, " b =", b)

    # Swap a and b using temp variable
    temp = a
    a = b
    b = temp

    print("a =", a, " b =", b)

    a, b = b, a

    print("a =", a, " b =", b)
    print("a =", a, " b =", b)