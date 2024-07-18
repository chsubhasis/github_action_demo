import os, sys
sys.path.insert(0, os.getcwd())
from github_action_demo.script import addition

def test_data_type():
    subj = addition(2, 3)
    assert isinstance(subj, int)