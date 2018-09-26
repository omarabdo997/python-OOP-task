import sys


class Matrix:
    __counter = 0

    def __init__(self, mat):
        while(1):
            check = 1
            self.mat = mat
            no_of_cols = self.cols()
            for i in self.mat:
                if(type(i) != list):
                    check = 1
                elif(len(i) != no_of_cols):
                    check = 0
            self.__id = Matrix.__counter
            Matrix.__counter += 1
            if(check == 1):
                break
            else:
                print(
                    "You must enter the same number of columns for each row program closing")
                sys.exit(1)

    def get_id(self):
        return "#"+str(self.__id)

    def rows(self):
        return len(self.mat)

    def cols(self):
        matleng = 0
        for i in self.mat:
            if(type(i) != list):
                return 1
            elif (len(i) >= matleng):
                matleng = len(i)
        return matleng

    def dimensions(self):
        return str(self.rows())+"X"+str(self.cols())

    def Matrix(self):
        return Matrix([0])

    def description(self):
        a = []
        for i in self.mat:
            a.append(i)
        b = str(a)
        c = ""
        i = 0
        while (i <= (len(b)-1)):
            if(b[i] == "]"):
                if (i == len(b)-2):
                    c += "]]"
                    i += 2
                else:
                    c += "]"
                    c += "\n"
                    i += 2

            else:
                c += b[i]
                i += 1
        return c


A = Matrix([[1, 2, 3], [4, 5], [2, 3, 4]])
rows = A.rows()
col = A.cols()
dim = A.dimensions()
id = A.get_id()
a = A.Matrix()
print(A.description())
print(rows)
print(col)
print(dim)
print(id)
print(a.mat)
