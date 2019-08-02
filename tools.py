
class tools:
    """
    tools class
    """
    def __init__(self):
        pass

    @staticmethod
    def save(filename,text):
        """
        save file
        ファイルを保存
        :param filename: str
            filename
            ファイルの名前
        :param text: str
            saved text
            保存したテキスト
        :return:
        """
        f= open(filename,"a", encoding="utf-8")
        f.write(text)
        print("save completed")

    @staticmethod
    def read(filename):
        """
        read file
        ファイルを読む
        :param filename: str
            filename
            ファイルの名前
        :return: str
            file text
            ファイルテキスト
        """
        retval=[]
        f= open(filename,"r",encoding="utf-8_sig")

        for line in f.readlines():
            # -1 to discard last \n
            retval.append(line[:-1].split("\t"))

        return retval

    @staticmethod
    def clearFile(filename):
        """
        make file clear
        ファイルを明確にする
        :param filename: str
            filename
            ファイルの名前
        :return: -
        """
        open(filename, 'w').close()
        print("Clear file")

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

if __name__ == "__main__":
    print("tools")

    print(tools.read("../result.txt")[0])
    tools.clearFile("../test.txt")