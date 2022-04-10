
from math import dist
from create_kdtree import *
import numpy as np

def search_closest(aim,kd_root):
    nearest_dist = np.inf
    nearest_node = None
    
    def visit(node):
        nonlocal nearest_dist
        nonlocal nearest_node
        if node:
            flag = aim[node.current_dim] - node.data[node.current_dim]
            visit(node.left if flag < 0 else node.right)
            current_dist = np.linalg.norm(aim-node.data,2)
            if current_dist < nearest_dist:
                nearest_dist = current_dist
                nearest_node = node
            #判断另一边的结点是否需要访问
            #当前最短路径大于到当前划分超平面的距离，则要到另一边去找
            if nearest_dist > abs(flag):
                visit(node.left if flag > 0 else node.right)
    visit(kd_root)   

    return nearest_node,nearest_dist


if __name__ == '__main__':
    aim = np.array([2.1,3.1])
    data = [[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
    root = create_kd_tree(data)
    
    node,dist = search_closest(aim,root)
    print(node.data,dist)

