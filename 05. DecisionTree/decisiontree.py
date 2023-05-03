import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from io import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

# ------DEFINE------
filename = "diabetes.csv"
col_names = ['pregnant', 'glucose', 'bp', 'skin',
             'insulin', 'bmi', 'pedigree', 'age', 'label']
feature_cols = ['pregnant', 'glucose', 'bp',
                'skin', 'insulin', 'bmi', 'pedigree', 'age']
# -----------------
# -----------------


def _read_data(showData: bool = False):
    '''
    read all data from file "diabetes.csv" and split this to input data and output data
    '''

    global filename, col_names, feature_cols

    df = pd.read_csv(filename, names=col_names).iloc[1:]
    df.head()  # head 0 -> end

    if showData:  # show infor data and some line of dataset
        print("Dataset Length: ", len(df))
        print("Dataset Shape: ", df.shape)
        print("Dataset: ", df.head())

    # split data => [features] and [target values]
    X = df[feature_cols]
    Y = df.label
    return X, Y


def _split_train_and_test(X, Y, rand_test_size: float):
    '''
    split dataset into training set and test set
    '''
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=rand_test_size, random_state=1)  # 70% training and 30% test
    return X_train, X_test, Y_train, Y_test


def _train_using_gini(X_train, Y_train, max_depth: int = 3):
    '''
    Function to perform training with entropy
    '''

    # create decision tree
    clf_gini = DecisionTreeClassifier(
        criterion="gini", max_depth=max_depth, min_samples_leaf=5)
    # Train tree
    clf_gini.fit(X_train, Y_train)
    return clf_gini


def _train_using_entropy(X_train, Y_train, max_depth: int = 3):
    '''
    Function to perform training with entropy
    '''

    # create decision tree
    clf_entropy = DecisionTreeClassifier(
        criterion="entropy", max_depth=max_depth, min_samples_leaf=5)
    # Train tree
    clf_entropy = clf_entropy.fit(X_train, Y_train)
    return clf_entropy


def _prediction(X_test, clf_object: DecisionTreeClassifier, show: bool = False):
    '''
    Predicton on test with DecisionTree (entropy, gini)
    '''
    Y_pred = clf_object.predict(X_test)
    if show:
        print("Predicted values:")
        print(Y_pred)

    return Y_pred


def _calc_accuracy_model(Y_test, Y_pred, type: int = 1):
    if type == 1:
        print("Entropy Accuracy :", accuracy_score(Y_test, Y_pred)*100)
    elif type == 2:
        print("GiniIdx Accuracy :", accuracy_score(Y_test, Y_pred)*100)


def _image_DecisionTree(clf_object: DecisionTreeClassifier, type: int):
    global feature_cols
    dot_data = StringIO()
    export_graphviz(clf_object, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True,
                    feature_names=feature_cols,
                    class_names=['0', '1'])
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png('diabetes.png')
    Image(graph.create_png())


def _test_Tree(type: int, max_depth: int = 3):
    '''
    type = 1: use entropy to create decision tree
    type = 2: use gini index to create decision tree
    max_depth: depth of tree (default: max_depth = 3)
    '''
    X, Y = _read_data()
    X_train, X_test, Y_train, Y_test = _split_train_and_test(X, Y, 0.3)
    clf_object = None
    if type == 1:
        clf_object = _train_using_entropy(X_train, Y_train, max_depth)
        Y_pred = _prediction(X_test, clf_object=clf_object)
    elif type == 2:
        clf_object = _train_using_gini(X_train, Y_train, max_depth)
        Y_pred = _prediction(X_test, clf_object=clf_object)
    else:
        return
    _calc_accuracy_model(Y_test, Y_pred, type)
    # _image_DecisionTree(clf_object, type)


if __name__ == '__main__':
    _test_Tree(1, 4)
    _test_Tree(2, 5)
