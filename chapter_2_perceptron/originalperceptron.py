import numpy as np

def sign(x,y,w,b):
    return y*(np.dot(x,w)+b)
def random_descend(x_train,y_train,w=np.array([0,0]),b=0,iter=1):
    while True:
         index = 0
         for i in range(len(x_train)):
             if sign(x_train[i],y_train[i],w,b)<=0:
                 w = w + iter*y_train[i]*x_train[i]
                 b = b + iter*y_train[i]
                 index += 1

                #绘图


         if index == 0:
            print(w,b)
            break

if __name__ == '__main__':
    x_train = np.array([[3,3],[4,3],[1,1]])
    y_train = np.array([1,1,-1])

    random_descend(x_train,y_train)
   
