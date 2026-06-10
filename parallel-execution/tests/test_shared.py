shared_state = []

def test_shared_1():
    shared_state.append("test 1")
    assert len(shared_state) == 1
    
def test_shared_2():
    shared_state.append("test 2")
    assert len(shared_state) == 1
    
def test_shared_3():
    shared_state.append("test 3")
    assert len(shared_state) == 1
    
def test_shared_4():
    shared_state.append("test 4")
    assert len(shared_state) == 1