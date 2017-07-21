"""Unit and functional tests for decision tree."""
import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def golf():
    """Data frame for testing."""
    golf = [{"outlook": "Rainy", "temp": "Hot", "humidity": "High",
            "windy": False, "golf": False},
            {"outlook": "Rainy", "temp": "Hot", "humidity": "High",
            "windy": True, "golf": False},
            {"outlook": "Overcast", "temp": "Hot", "humidity": "High",
            "windy": False, "golf": True},
            {"outlook": "Sunny", "temp": "mild", "humidity": "High",
            "windy": False, "golf": True},
            {"outlook": "Sunny", "temp": "Cool", "humidity": "Normal",
            "windy": False, "golf": True},
            {"outlook": "Sunny", "temp": "Cool", "humidity": "Normal",
            "windy": True, "golf": False},
            {"outlook": "Overcast", "temp": "Cool", "humidity": "Normal",
            "windy": True, "golf": True},
            {"outlook": "Rainy", "temp": "mild", "humidity": "High",
            "windy": False, "golf": False},
            {"outlook": "Rainy", "temp": "Cool", "humidity": "Normal",
            "windy": False, "golf": True},
            {"outlook": "Sunny", "temp": "mild", "humidity": "Normal",
            "windy": False, "golf": True},
            {"outlook": "Rainy", "temp": "mild", "humidity": "Normal",
            "windy": True, "golf": True},
            {"outlook": "Overcast", "temp": "mild", "humidity": "High",
            "windy": True, "golf": True},
            {"outlook": "Overcast", "temp": "Hot", "humidity": "Normal",
            "windy": False, "golf": True},
            {"outlook": "Sunny", "temp": "mild", "humidity": "High",
            "windy": True, "golf": False}
            ]

    return pd.DataFrame(golf)


@pytest.fixture
def golf_list_form():
    """Data frame for testing."""
    golf = [{"outlook": "Rainy", "temp": "Hot", "humidity": "High",
            "windy": False, "golf": False},
            {"outlook": "Rainy", "temp": "Hot", "humidity": "High",
            "windy": True, "golf": False},
            {"outlook": "Overcast", "temp": "Hot", "humidity": "High",
            "windy": False, "golf": True},
            {"outlook": "Sunny", "temp": "mild", "humidity": "High",
            "windy": False, "golf": True},
            {"outlook": "Sunny", "temp": "Cool", "humidity": "Normal",
            "windy": False, "golf": True},
            {"outlook": "Sunny", "temp": "Cool", "humidity": "Normal",
            "windy": True, "golf": False},
            {"outlook": "Overcast", "temp": "Cool", "humidity": "Normal",
            "windy": True, "golf": True},
            {"outlook": "Rainy", "temp": "mild", "humidity": "High",
            "windy": False, "golf": False},
            {"outlook": "Rainy", "temp": "Cool", "humidity": "Normal",
            "windy": False, "golf": True},
            {"outlook": "Sunny", "temp": "mild", "humidity": "Normal",
            "windy": False, "golf": True},
            {"outlook": "Rainy", "temp": "mild", "humidity": "Normal",
            "windy": True, "golf": True},
            {"outlook": "Overcast", "temp": "mild", "humidity": "High",
            "windy": True, "golf": True},
            {"outlook": "Overcast", "temp": "Hot", "humidity": "Normal",
            "windy": False, "golf": True},
            {"outlook": "Sunny", "temp": "mild", "humidity": "High",
            "windy": True, "golf": False}
            ]

    return golf


def test_init_decision_tree(golf):
    """Test the basic initialization logic."""
    from decision_tree import DecisionTree
    tree = DecisionTree(data=golf)
    assert (tree.max_depth,
            tree.min_leaf_size,
            tree.data) == (None, None, tree.data)


@pytest.fixture
def decision_tree(golf):
    """Traditional data set for ID3 algorithm."""
    from decision_tree import DecisionTree
    decision_tree = DecisionTree(data=golf)
    return decision_tree


def test_init_types_one():
    """Test the type logic in init."""
    from decision_tree import DecisionTree
    with pytest.raises(TypeError):
        tree = DecisionTree(data='1234')


def test_init_types_converts_to_data_frame(golf_list_form, decision_tree):
    """Test that if given a tuple or list, converts to data frame."""
    from decision_tree import DecisionTree
    tree = DecisionTree(data=golf_list_form)
    assert isinstance(tree.data, pd.DataFrame)


def test_class_probabilities_no_target(decision_tree):
    """Test that probability function works."""
    golf_probabilities = [np.array([0.64285714, 0.35714286]),
                          np.array([0.5, 0.5]),
                          np.array([0.35714286, 0.35714286, 0.28571429]),
                          np.array([0.42857143, 0.28571429, 0.28571429]),
                          np.array([0.57142857, 0.42857143])]

    for idx, column in enumerate(decision_tree.data):
        array_of_probs = decision_tree.class_probabilities(column)
        np.testing.assert_array_almost_equal(array_of_probs, golf_probabilities[idx])


def test_entropy_using_class_probabilities(decision_tree):
    """Test that entropy returns the desired value using the probabiliteis."""
    class_probs = [decision_tree.class_probabilities(column)
                   for column in decision_tree.data]
    entropies = [0.94028595867063092,
                 1.0,
                 1.5774062828523454,
                 1.5566567074628228,
                 0.98522813603425152]
    for idx, prob in enumerate(class_probs):
        attribute_entropy = decision_tree.entropy(prob)
        np.testing.assert_equal(attribute_entropy, entropies[idx])


def test_class_probabilities_with_target(decision_tree):
    """Test that this returns the correct values with a target."""
    class_probs = [decision_tree.class_probabilities(column)
                   for column in decision_tree.data]
    list_of_subset_probs = [decision_tree.class_probabilities(column, 'golf')
                            for column in decision_tree.data
                            if not column == decision_tree.data.golf]

    
    # entropies = [decision_tree.entropy(prob) for prob in class_probs]
