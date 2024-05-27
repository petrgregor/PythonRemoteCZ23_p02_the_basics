def main():
    print("Hello in my library")


def my_function():
    return "Hello"


# tato část se spustí pouze v případě, že pouštím tento soubor přímo
# pokud je soubor importován jinam, pak se tato část neprovede
if __name__ == '__main__':
    main()
    print(my_function())
