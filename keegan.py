def keegan():
    print("Choudhury")
def default():
    print("Eileen")

def main():
    if sys.argv[1] == "keegan":
        keegan()
    else:
        default()
if __name__ == '__main__':
    main()
