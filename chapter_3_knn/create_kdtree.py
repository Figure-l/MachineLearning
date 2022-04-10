"""
根据数据划分k维空间，构建kdtree
"""

#current_time作为该数据点在当前维度上划分的依据

class node():
    def __init__(self,data,current_dim,left,right) -> None:
        self.data = data
        self.current_dim = current_dim
        self.left = left
        self.right = right

#返回构建好的kd树的根节点
def create_kd_tree(x_train):
    #记录k维空间大小
    k = len(x_train[0])
    #选择dim为切分的坐标轴
    def create_node(dim,arr):
        if not arr:
            return None
        #sort或sorted
        # 按照制定的dim维去排列数据    
        arr.sort(key=lambda content:content[dim])
        # / 为浮点数除  // 为整除 3.0//2 == 1.0
        mid = len(arr) // 2
        mid_data = arr[mid]
        dim_next = (dim + 1) % k

        #recurse
        return node(mid_data,dim,create_node(dim_next,arr[:mid]),create_node(dim_next,arr[mid+1:]))
    return create_node(0,x_train)


def pre_order(root):
    print (root.data)
    if root.left:
        pre_order(root.left)
    if root.right:
        pre_order(root.right)   


    



# if __name__ == '__main__':
#     data = [[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
#     kd = create_kd_tree(data)
#     pre_order(kd)
