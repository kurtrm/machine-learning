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
        # First, find the greatest information gain between the attributes and
        # the set label.
        starting_columns = self.data.drop(target, axis=1)
        most_information_gain = 0
        most_column = ''
        for i, column in enumerate(starting_columns):
            self.information_gain(
        
        pass

    def predict(self, data):
        """Return labels for test data."""
        pass
    
    
    # This function needs a lot of work to be functional
    def class_probabilities(self, column, target=None):
        """Calculate the proportions of values within a column
        to the length of the entire data set.
        """
        if not target:
            return self.data[column].value_counts(normalize=True, sort=False)
        classes = self.data[column].unique()
        target_size = self.data[target].size
        target_classes = self.data[target].unique()
        attribute_target_groups = self.data.groupby([column, target]).size().to_dict()
        return [attribute_target_groups[one_class, another_class] / target_size
                for another_class in target_classes
                for one_class in classes
                if another_class]

    def entropy(self, probabilities):
        """Given a probability, calculate class probabilities 
        for a given attribute.
        """
        return sum(-p * np.log2(p) for p in probabilities if p)

    def information_gain(self, root_node, candidate_node, target):
        """Calculate the information gain for a given subset
        of data.
        """
        # import pdb; pdb.set_trace()
        set_entropy = self.entropy(self.class_probabilities(root_node))
        attribute_proportion = self.class_probabilities(candidate_node)
        class_proportion = self.class_probabilities(candidate_node, target)
        return set_entropy - sum(attribute_proportion * self.entropy(prop.values)
                                 for prop in class_proportion)
