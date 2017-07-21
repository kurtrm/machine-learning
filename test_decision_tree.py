"""Unit and functional tests for decision tree."""
import pytest
import pandas as pd
import numpy as np


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

golf = golf.DataFrame(golf)


@pytest.fixture
def decision_tree():
    """Traditional data set for ID3 algorithm."""
    from decision_tree import DecisionTree
    decision_tree = DecisionTree(data=golf)
    return decision_tree
