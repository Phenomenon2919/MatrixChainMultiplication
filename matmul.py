import sys
INP_FILE = sys.argv[1]


def inorder(source, length, s, name_list):
    if length == 1:
        return name_list[source]
    elif length == 2:
        return "(" + name_list[source] + " " + name_list[source + 1] + ")"

    s_point = s[source + 1, source + length]
    left_length = s_point - source
    right_length = length - left_length
    left = inorder(source, left_length, s, name_list)
    right = inorder(s_point, right_length, s, name_list)

    if length == len(name_list):
        return left + right
    else:
        return "(" + left + right + ")"


def matrix_chain_order(p, name_list):
    m = {}
    s = {}

    for i in range(1, len(p)):
        m[i, i] = 0

    for l in range(2, len(p)):
        for i in range(1, len(p) - l + 1):
            j = i + l - 1
            m[i, j] = None
            for k in range(i, j):
                q = m[i, k] + m[k + 1, j] + p[i - 1] * p[k] * p[j]
                if m[i, j] is None or q < m[i, j]:
                    m[i, j] = q
                    s[i, j] = k

    print("Cost = " +str(m[1, len(p)-1]))
    print("Order = " +str(inorder(0, len(p)-1, s, name_list)))


fileInp = open(INP_FILE, "r")
dim_list= fileInp.readline().split()
name_list = fileInp.readline().split()
for i in range(len(dim_list)):
    dim_list[i] = int(dim_list[i])
matrix_chain_order(dim_list,name_list)
fileInp.close()