
class tools:
    def __init__(self):
        pass

    @staticmethod
    def save(filename,text):
        f= open(filename,"a")
        f.write(text)
        print("save completed")


if __name__ == "__main__":
    print("tools")