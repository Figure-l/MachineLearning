import numpy as np
import matplotlib.pyplot as plt 


def gram_matrix(x_train):
    return np.dot(x_train,x_train.T)

def sign(alphs,y_train,gram,b,index):
    factor = np.array([alphs[i]*y_train[i] for i in range(len(alphs))])
    return y_train[index]*(np.dot(factor,gram[index].T)+b)

def random_descend(x_train,y_train,b=0,alphs=np.array([0,0,0])):
    while True:
        count = 0
        for i in range(len(alphs)):
             if sign(alphs,y_train,gram_matrix(x_train),b,i)<=0:
                 alphs[i] += 1
                 b += y_train[i]
                 count += 1
                 
        if count == 0:
            factor = np.array([alphs[i]*y_train[i] for i in range(len(alphs))])
            w = np.dot(factor,x_train)
            
            #绘图
            plt.figure()
            x1 = np.arange(1,5)
            x2 = (-b-w[0]*x1)/w[1]
            plt.plot(x1,x2)
            plt.xlabel('x1')
            plt.ylabel('x2')

            for i in range(len(x_train)):
                plt.scatter(x_train[i][0],x_train[i][1],color='r',marker='+')
            plt.show()
           
            break
                     
if __name__ == '__main__':
    x_train = np.array([[3,3],[4,3],[1,1]])
    y_train = np.array([1,1,-1])
    random_descend(x_train,y_train)