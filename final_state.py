"""
Predicts the class of a dataframe inserted in the predict() function. Use fit(*your_dataset*, *your_classes*) to 
build the tree and insert the tree into predict() as my_tree parameter.
"""
import numpy as np

class Node:
    
    def __init__(self, X, y, add_params):
        self.X = X
        self.y = y
        self.gini = add_params[2]
        self.feature_index = add_params[0]
        self.threshold = add_params[1]
        self.left = add_params[3][0], add_params[3][1]
        self.right = add_params[4][0], add_params[4][1]
        self.left_node=None
        self.right_node=None


class MyDecisionTreeClassifier:

    def __init__(self, max_depth):
        self.max_depth = max_depth
    
    def gini(self, groups, classes):
        '''
        A Gini score gives an idea of how good a split is by how mixed the
        classes are in the two groups created by the split.
        
        A perfect separation results in a Gini score of 0,
        whereas the worst case split that results in 50/50
        classes in each group result in a Gini score of 0.5
        (for a 2 class problem).
        '''
        ginis=[]
        class_count=[]
        for splt in range(2):
            class_count.append([])
            for i in range(max(classes)+1):
                class_count[splt].append(len([x for x in groups[splt] if x == i]))
        for i in class_count:
            to_minus=0
            for j in i:
                try:
                    to_minus+=pow(j/sum(i), 2)
                except ZeroDivisionError:
                    pass
            ginis.append(1-to_minus)
        return ginis

    def split_data(self, X, y):
        """
        Defines the best split of dataset to calculate gini for groups created. Use the gini() function 
        to define gini.
        """
        best_sep={"gini":[1,1], "leftsplit": [], "thres":0, "id":0}
        columns=[]
        for i in range(len(X[0])):
            columns.append([])
        for row in X:
            for i in range(len(row)):
                columns[i].append(row[i])
        thresholds_to_check=[]
        for i in columns:
            thresholds_to_check.append(set(i))
        for i in range(len(thresholds_to_check)):
            for thres in thresholds_to_check[i]:
                try :
                    left=[y[X.tolist().index(x)] for x in X.tolist() if x[i]<=thres]
                    right=[y[X.tolist().index(x)] for x in X.tolist() if x[i]>thres]
                except AttributeError:
                    left=[y[X.index(x)] for x in X if x[i]<=thres]
                    right=[y[X.index(x)] for x in X if x[i]>thres]
                gini_got=self.gini([left, right], list(range(max(y)+1)))

                if (gini_got[0]==0) or (gini_got[0] < best_sep["gini"][0] and gini_got[1] < best_sep["gini"][1]):
                    best_sep["gini"]=gini_got
                    try :
                        best_sep["leftsplit"]=[[x for x in X.tolist() if x[i]<=thres]]
                        best_sep["leftsplit"].append([y[X.tolist().index(x)] for x in best_sep["leftsplit"][0]])
                        best_sep["rightsplit"]=[[x for x in X.tolist() if x[i]>thres]]
                        best_sep["rightsplit"].append([y[X.tolist().index(x)] for x in best_sep["rightsplit"][0]])
                    except AttributeError:
                        best_sep["leftsplit"]=[[x for x in X if x[i]<=thres]]
                        best_sep["leftsplit"].append([y[X.index(x)] for x in best_sep["leftsplit"][0]])
                        best_sep["rightsplit"]=[[x for x in X if x[i]>thres]]
                        best_sep["rightsplit"].append([y[X.index(x)] for x in best_sep["rightsplit"][0]])
                    best_sep["thres"]=thres
                    best_sep["id"]=i
        return best_sep["id"], best_sep["thres"], best_sep["gini"],  best_sep["leftsplit"], best_sep["rightsplit"]

    def build_tree(self, X, y, depth = 0):
        """
        A recursive function to create the tree to be traversed. Uses class Node to recursively
        create class containing the classes of a binary tree. 
        """
        if depth == 0:
            params=self.split_data(X, y)
            root=Node(X, y, params)
            root.left_node=self.build_tree(root.left[0], root.left[1], depth+1)
            root.right_node=self.build_tree(root.right[0], root.right[1], depth+1)
            return root
        if depth < self.max_depth:
            if len(set(y)) == 0:
                return None
            elif len(set(y))>1:
                params=self.split_data(X, y)
                branch=Node(X, y, params)
                leftnode = self.build_tree(branch.left[0], branch.left[1], depth+1)
                rightnode = self.build_tree(branch.right[0], branch.right[1], depth+1)
                branch.right_node = rightnode
                branch.left_node = leftnode
                return branch
            else :
                params=self.split_data(X, y)
                branch=Node(X, y, params)
                return branch
        
    
    def fit(self, X, y):
        """
        Casts the build_tree() function to get it ready for traversing by predict() function. 
        """
        return self.build_tree(X, y)
    
    def predict(self, X_test, my_tree):
        """
        Takes an example of a dataset to predict its class by recursive traversing the tree 
        supported by fit() function. Takes my_tree parameter as a representation of a created binary
        tree, returns the predicted class of a dataframe.
        """
        if type(X_test)==np.ndarray:
            X_test=X_test.tolist()
        for i in X_test:
            if i in my_tree.left[0] and my_tree.gini[0]==0:
                return "The class of the item you look for is rather : " + str(my_tree.left[1][0])
            elif  i in my_tree.right[0] and my_tree.gini[1]==0:
                return "The class of the item you look for is rather : " + str(my_tree.left[1][0])
            else :
                if i in my_tree.left[0]:
                    self.predict(self, i, my_tree.left_node)
                elif i in my_tree.right[0]:
                    self.predict(i, my_tree.right_node)
            return "Unable to find the element in the tree"
