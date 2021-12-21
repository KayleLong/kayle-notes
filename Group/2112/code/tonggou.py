import numpy as np
import copy
import random
from decimal import *
from collections import Counter
import time
import tgshenjing
time_begin = time.time()
infinity = float("inf")

# 深度优先搜索
def iter_dfs(init_adj_list, s):
    S, Q = set(), []  # Visited-set and queue
    Y = []
    Q.append(s)  # We plan on visiting s
    while Q:  # Planned nodes left?
        # u = Q.pop()               # Get one
        u = Q.pop(random.randint(0, len(Q) - 1))
        # print(u)
        if u in S:
            continue  # Already visited? Skip it
        else:
            for y in S:
                # print(y)
                for z in init_adj_list[y]:
                    # print(z,G[y])
                    if z == s:
                        Y.append(copy.copy(y))
                        break

        if Y != []:
            x = set(Y)
            if x not in lite2:
                lite2.append(x)
        S.add(u)  # We've visited it now
        Q = []
        Q.extend(init_adj_list[u])  # Schedule all neighbors
        # print(G[u])
        # print(Q)
        # print(S)
        yield (u)  # Report u as visited

# 排序后最大环路
def opo(adj_list,s):
    """
    :param adj_list: 邻接表
    :return: 顺逆时针相同环路排序
    """
    k=0
    lite = []
    global lite2
    lite2 = []
    print('起始连杆:',s)
    while k<600:
        k+=1
        for i in range(len(adj_list)): adj_list[i] = set(adj_list[i])
        # s=17  #起始连杆
        # print(list(iter_dfs(adj_list, s))) #[0, 5, 7, 6, 2, 3, 4, 1]
        h=list(iter_dfs(adj_list, s))#h为遍历的所有路径
        if h not in lite:#去掉重复路径
            lite.append(h)

    lite4=list(filter(lambda f: not any(set(f) < set(g) for g in lite2), lite2))

    set1 = lite4[-1]
    for i in range(0, len(lite4)):
         set1= set1.union(lite4[i])
    # print(set1)#确认是否完成环路

    l1=[]
    l2=[]
    for i in lite:
        for j in i[::-1]:
            if j in set1:
                # print(i.index(j))
                index = i.index(j)
                # print(i[:index+1])
                l1.append(i[:index+1])
                break

    # 采用倒序遍历，删除元素
    # remove()方法不可行
    for i in range(len(l1)-1,-1,-1):
        if len(l1[i])<3:
            l1.pop(i)

    res = max(l1, key=len, default='')
    for i in l1:
        if len(i)==len(res):
            l2.append(i)

    l3_reverse=[]
    l1_np= np.array(l1)
    l3_unique=np.unique(l1_np)
    for i in l3_unique:
        i.append(s)

    for i in l3_unique:
        l3_reverse.append(i[::-1])

    for i in l3_unique:
        if i in l3_reverse:
            continue
        else:
          l3_reverse.append(i)

    print('所有环路数：',len(l3_reverse))

    # l3 = add_index(l3_reverse)
    # print('所有环路：',l3_reverse)

    l4=[]
    res = max(l3_reverse, key=len, default='')
    for h in l3_reverse:
        if len(h)==len(res):
            l4.append(h)
    print('最大环路数：',len(l4))
    arr_l4.append(add_index(l4))
    print('最大环路:',arr_l4)

    l_empty = []
    # Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
    # capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero,
    # Overflow])
    # getcontext().prec = 20
    for i in adj_list:
        l_empty.append(list(i))
    l5=[]
    for i in l_empty:
        i1=copy.copy(i)
        l5.append(len(i))
    l6= []
    for i in l4:
        l6.append(i[::-1])
    print(l_empty)
    l_opo=[]
    for i in l6:
        if i in l_opo:
            continue
        if i in l4:
            l_opo.append(i)
            l_opo.append(i[::-1])

    # print('顺逆时针相同环路排序',l_opo) #顺逆时针相同环路排序
    return l_opo


# 创建映射后的邻接表
def create_graph(init_adj_list, arr):
    """
    :param init_adj_list:初始邻接表
    :param arr:环路排序
    :return:单个映射后的邻接表
    """
    mapper_dict = {}
    new_adj_list = []
    k = 0
    for x in arr:
        mapper_dict[x] = k
        k = k+1

    if len(arr)!=len(init_adj_list):
        for i in range(len(init_adj_list)):
            if i not in arr:
                mapper_dict[i] = k
                k = k+1

    # 映射表
    # print('mapper_dict==',mapper_dict)
    for x in init_adj_list:
        data = np.array(x)

        def mapper(entry):
            return mapper_dict[entry] if entry in mapper_dict else entry

        # 将函数向量化
        mp = np.vectorize(mapper)
        l= mp(data)
        new_adj_list.append(l)
    return new_adj_list


# 邻接表转矩阵
def list_to_matrix(adj_list):
    """
    :param adj_list:邻接表
    :return:邻接矩阵
    """
    if len(adj_list)<1:
        print('发生错误！邻接表为空')
        exit()
    gmat=np.zeros((len(adj_list), len(adj_list)))
    k=0
    for i in adj_list:
        for j in i:
            gmat[k][j]=1
        k=k+1
    return gmat

# 最大环路与对应连杆度映射：lh
def lh(init_adj_list, conv_arr):
    ppo=[]
    list_empty=[]
    for i in init_adj_list:
        list_empty.append(len(i))
    for i in conv_arr[:]:
        po=[]
        for j in i:
            op=list_empty[j]
            po.append(op)
        ppo.append(copy.copy(po))

    lh_list=list(enumerate(ppo,start=1))
    print('最大环路连杆度：')
    print(lh_list)
    return lh_list

# 环路编号+1，使其于图例编号一致
def add_index(arr):
    new_arr = np.array(arr)
    new_arr = new_arr +1
    return new_arr


# 映射
def arr_rc(init_adj_list, conv_arr):
    """
    :param init_adj_list: 初始邻接表，元素是set类型
    :param conv_arr: 环路排序
    :return:映射后的邻接表
    """
    temp_list = []
    for x in init_adj_list:
        l = list(x)
        l.sort()
        temp_list.append(l)

    init_adj_list = temp_list
    k = 0
    # 去除对称矩阵
    largest_arr = conv_arr[:]
    # print('最大环路:\n',largest_arr)



    # print(ppo)

    # 映射后的初始邻接表
    """
    映射实例
    映射前：
    {a, b, c, i, j, d, e, f, g}
    [0, 1, 2, 8, 9, 3, 4, 5, 6]
    映射后：
    {a, b, c, i, j, d, e, f, g}
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    """
    new_adj_list=[]
    for i in range(0,len(largest_arr)):
        # largest_arr是环路，需要去除最后一个元素
        new_adj_list.append(create_graph(init_adj_list, largest_arr[i][:-1]))
    return new_adj_list




#重新编号后字母编号邻接表
def sort_zip(arr1, arr2):
    """
    :param arr1:
    :param arr2:
    :return:
    """
    zipped = zip(arr1, arr2)
    # print('arr1==',arr1,'arr2==',arr2)
    l=sorted(list(zipped))
    # print("l===",l)

    temp_list=[]#重新编号后邻接表,按数字升序编号
    for x in l:
        temp_list.append(x[1])
    # print('重新编号后的邻接表',temp_list)
    return temp_list

# 最大环路重新编号后,转为邻接矩阵
def largest_loop_to_matrix(init_adj_list, conv_arr, new_adj_list):
    l_arr=[]
    l_matrix=[]
    for x in conv_arr[:]:
        temp_l = []
        for i in range(len(init_adj_list)):
            temp_l.append(x.index(i) if i in x else len(init_adj_list)-1)
        l_arr.append(temp_l)
    # print('l_arr',l_arr)

    # 最大环路重新编号后邻接表
    largest_adj_list = []
    for i in range(len(l_arr)):
        largest_adj_list.append(sort_zip(l_arr[i], new_adj_list[i]))
    # print('largest_adj_list==', largest_adj_list)

    # 邻接表转邻接矩阵
    for x in largest_adj_list:
        l_matrix.append(list_to_matrix(x))

    return l_matrix


def slicing_list(loop_list):
    """
    将最大环路分为头部和尾部
    head_list 为第一个环路
    tail_list 为剩余环路
    """
    head_list = []
    tail_list = []
    flag = 0
    count = 0
    for x in loop_list:# 第一层
        if x[0] == 1:# 分组
            flag = flag^1
            print('flag==', flag)
        if flag == 1:
            count = count+1
            head_list.append(x[1])
        else:
            tail_list.append(x[1])
    print('head_list==', head_list)
    print('tail_list==', tail_list)
    return head_list, tail_list, count

def adapt(largest_loop_list):
    # 用于是否分割
    flag_s = 1
    count = 0
    while flag_s:
        head_list, tail_list, slice = slicing_list(largest_loop_list)
        print('count==', count)

        # 在尾部环路中查找和头部环路一致的环路
        k = 1
        if len(tail_list) == 0:
            print('没有找到')
            break
        for x in head_list:
            for y in tail_list:
                if x==y:
                    tail_index = tail_list.index(y)
                    head_index = count+k
                    print('head_index', head_index)
                    print('tail_index', tail_index)
                    return head_index, tail_index
            k=k+1

        if (len(largest_loop_list)-slice) == 0:
            flag_s = 0
        else:
            largest_loop_list = largest_loop_list[slice:]

        count = count + slice
    return 0


# 确定起始连杆
def find_start(adj_list):
    temp_list = []
    for x in adj_list:
        temp_list.append(len(x))

    print('temp_list==', temp_list)

    result=Counter(temp_list)
    print('result', result)
    new_tup = zip(result.values(), result.keys())
    min_num = min(new_tup)[1]
    print('min_num==',min_num)

    print('temp_list==', temp_list)
    count = 0
    index_list=[]
    for i in temp_list:
        if i == int(min_num):
            index_list.append(count)
        count = count+1
    print('index_list==', index_list)
    return index_list


def main_func():
    # 无向无权邻接表
    init_adj_list1=[
        # 10杆
        # [1, 6, 7, 8],
        # [0, 2],
        # [1, 3, 8],
        # [2, 4, 9],
        # [3, 5],
        # [4, 6, 7],
        # [0, 5],
        # [0, 5],
        # [0, 2, 9],
        # [3, 8]

        # [1,4,5,9],
        # [0,2,6],
        # [1,3,7,8],
        # [2,4],
        # [0,3,8],
        # [0,6],
        # [1,5,7,10],
        # [2,6,10],
        # [2,4,9,10],
        # [0,8,10],
        # [6,7,8,9]

        # 21杆
        # [3,19],
        # [2,10],
        # [1,3,14],
        # [0,2,4,20],
        # [3,5,17],
        # [4,6],
        # [5,7],
        # [6,13],
        # [9,20],
        # [8,16],
        # [1,11],
        # [10,12],
        # [11,18],
        # [7,14],
        # [2,13,15],
        # [14,16],
        # [9,15,17],
        # [4,16],
        # [12,19],
        # [0,18],
        # [3,8]

        #28杆
        [1,13,25],#1
        [0,2,8],#2
        [1,3,26],#3
        [2,4,16],#4
        [3,5,23],#5
        [4,6,12],#6
        [5,7,19],#7
        [6,8,27],#8
        [1,7,9],#9
        [8,10,22],#10
        [9,11,17],#11
        [10,12],#12
        [5,11,13],#13
        [0,12,14],#14
        [13,15,21],#15
        [27,14,16],#16
        [3,15,17],#17
        [10,16,18],#18
        [17,19,25],#19
        [6,18,20],#20
        [19,21,26],#21
        [14,20,22],#22
        [9,21,23],#23
        [4,22,24],#24
        [23,25],#25
        [0,18,24],#26
        [2,20],#27
        [7,15]#28
    ]

    init_adj_list2=[
        # [1,4,5,9],
        # [0,2,6],
        # [1,3,7,8],
        # [2,4],
        # [0,3,8],
        # [0,6],
        # [1,5,7,10],
        # [2,6,10],
        # [2,4,9,10],
        # [0,8,10],
        # [6,7,8,9]

        # [1,6,7,8],
        # [0,2,9],
        # [1,3],
        # [2,4,9],
        # [3,5],
        # [4,6,7],
        # [0,5],
        # [0,5],
        # [0,9],
        # [1,3,8]

        # 21杆
        # [3,20],
        # [2,10],
        # [1,3,14],
        # [0,2,4,19],
        # [3,5,18],
        # [4,6],
        # [5,7],
        # [6,13],
        # [9,19],
        # [8,16],
        # [1,11],
        # [10,12],
        # [11,17],
        # [7,14],
        # [2,13,15],
        # [14,16],
        # [9,15,18],
        # [12,20],
        # [4,16],
        # [3,8],
        # [0,17]

        #28杆
        [1,7,16],#1
        [0,2,21],#2
        [1,3],#3
        [2,4,20],#4
        [3,5,17],#5
        [4,6,24],#6
        [5,7,19],#7
        [0,6,22],#8
        [9,15,16],#9
        [8,10,24],#10
        [9,11],#11
        [10,12,22],#12
        [11,13,17],#13
        [12,14,21],#14
        [13,15,19],#15
        [8,14,20],#16
        [0,8,18],#17
        [4,12,18],#18
        [16,17,27],#19
        [6,14],#20
        [3,15,23],#21
        [1,13,25],#22
        [7,11,23],#23
        [20,22,26],#24
        [5,9,25],#25
        [21,24,26],#26
        [23,25,27],#27
        [18,26],#28
    ]
    largest_loop_list=[]
    global  arr_l4
    arr_l4=[]

    for i in range(1,3):
        if i ==1:
            init_adj_list=init_adj_list1
            # 找起始杆
            index_list = find_start(init_adj_list)

            print('原始邻接表',init_adj_list)
            # 邻接表转邻接矩阵
            adj_matrix = list_to_matrix(init_adj_list)
            print('原始邻接矩阵：')
            print(adj_matrix)

            # 计算排序后最大环路
            # 在opo函数中init_adj_list的元素被转成了set类型
            conv_arr = opo(init_adj_list,index_list[0])
            # print('conv_arr==',conv_arr)
            # 映射
            new_adj_list=arr_rc(init_adj_list, conv_arr)
            # print('new_adj_list',new_adj_list)

            #
            lh_list=lh(init_adj_list, conv_arr)
            for x in lh_list:
                largest_loop_list.append(x)

            # 最大环路重新编号后,转为邻接矩阵
            head_matrix=largest_loop_to_matrix(init_adj_list, conv_arr, new_adj_list)
            for x in head_matrix:
                print('最大环路重新编号后邻接矩阵')
                print(x)
        else:
            init_adj_list=init_adj_list2

            # 找起始杆
            index_list = find_start(init_adj_list)

            print('原始邻接表',init_adj_list)
            # 邻接表转邻接矩阵
            adj_matrix = list_to_matrix(init_adj_list)
            print('原始邻接矩阵：')
            print(adj_matrix)
            # 计算排序后最大环路
            # 在opo函数中init_adj_list的元素被转成了set类型
            for x in index_list:
                conv_arr = opo(init_adj_list, x)
                # print('conv_arr==',conv_arr)
                # 映射
                new_adj_list=arr_rc(init_adj_list, conv_arr)
                # print('new_adj_list',new_adj_list)

                lh_list=lh(init_adj_list, conv_arr)
                # if tgshenjing.best_lin==0:
                #     break
                for x in lh_list:
                    largest_loop_list.append(x)

                # 最大环路重新编号后,转为邻接矩阵
                tail_matrix=largest_loop_to_matrix(init_adj_list, conv_arr, new_adj_list)
                for x in tail_matrix:
                    print('最大环路重新编号后邻接矩阵')
                    print(x)
                print(largest_loop_list)


                head_index, tail_index = adapt(largest_loop_list)
                print('largest_loop_list==',largest_loop_list)
                print('head_index==', head_index)
                print('tail_index==', tail_index)
                print('arr_l4==', arr_l4)
                print('head_loop==',arr_l4[0][head_index])
                print('tail_loop==',arr_l4[-1][tail_index])
                # print('tail_loop==',init_adj_list2,tail_index)

                if head_index:
                    print('邻接矩阵1:')
                    print(head_matrix[head_index-1])
                    print('邻接矩阵2:')
                    print(tail_matrix[tail_index])
                    return head_matrix[head_index-1], tail_matrix[tail_index],len(largest_loop_list[0][1])
                else:
                    print('没有找到')


