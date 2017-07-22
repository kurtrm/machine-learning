"""Implementation of a decision tree.
Preliminary studying, learning, and notes
are contained in the Jupyter Notebook.
"""
import numpy as np
import pandas as pd


class DecisionTree():
    """My implementation of a decision tree using
       entropy and information gain.
    """

    def __init__(self, max_depth=None, min_leaf_size=None, data=None):
        """Initialization parameters."""
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        if type(data) not in [tuple, list, pd.core.frame.DataFrame]:
            raise TypeError('Data must be a list/tuple'
                            'of records or a Pandas DataFrame.')
        elif type(data) in [tuple, list]:
            # import pdb; pdb.set_trace()
            self.data = pd.DataFrame(data)
        else:
            self.data = data

    def fit(self, target):
        """Construct decision tree with the data set."""
        pass

    def predict(self):
        """Return labels for test data."""
        pass

    def class_probabilities(self, column, target=None):
        """Calculate the proportions of classes within a column
        to the length of the entire data set.
        """
        if not target:
            return self.data[column].value_counts(normalize=True)
        classes = self.data[column].unique()
        return [self.data[target]
                .where(self.data[column] == one_class)
                .value_counts(normalize=True)
                for one_class in classes]

    def entropy(self, probabilities):
        """Given a probability, calculate class probabilities 
        for a given attribute.
        """
        return sum(-p * np.log2(p) for p in probabilities if p)

    def information_gain(self, column, target):
        """Calculate the information gain for a given subset
        of data.
        """
        set_entropy = self.entropy(target)
        attribute_proportion = self.class_probabilities(column)
        class_proportion = self.class_probabilities(column, target)
        return set_entropy - sum(attribute_proportion * self.entropy(prop)
                                 for prop in class_proportion)
