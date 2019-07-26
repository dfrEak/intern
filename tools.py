
class tools:
    def __init__(self):
        pass

    @staticmethod
    def save(filename,text):
        f= open(filename,"a", encoding="utf-8")
        f.write(text)
        print("save completed")

    @staticmethod
    def read(filename):
        retval=[]
        f= open(filename,"r")

        for line in f.readlines():
            # -1 to discard last \n
            retval.append(line[:-1].split("\t"))

        return retval

if __name__ == "__main__":
    print("tools")

    print(tools.read("../result_avg.txt")[0])