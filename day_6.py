class StrClass:
    def __init__(self,inp_str):
        self.inp_str = inp_str

    def Print_all(self):
        evn_inp_lst = list(self.inp_str[::2])
        evn_ListToString = "".join([str(letter) for letter in evn_inp_lst])
        odd_inp_list = list(self.inp_str[1::2])
        odd_ListToString = "".join([str(letter) for letter in odd_inp_list])
        print(evn_ListToString, odd_ListToString)

x = int(input())
for i in range(0, x):
    inp_str = str(input())
    n = StrClass(inp_str)
    n.Print_all()
