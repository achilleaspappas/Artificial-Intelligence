import pytest
from Source_Code_For_Testing import *

'''----------------------------------------------------------------------------------------------------------------'''
''' Τεστ για DFS '''


def test_1_dfs():
    method = "DFS"
    spaces = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
    initial_state = [1, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True, "true"


def test_2_dfs():
    method = "DFS"
    spaces = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
    initial_state = [2, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_3_dfs():
    method = "DFS"
    spaces = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
    initial_state = [3, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_4_dfs():
    method = "DFS"
    spaces = {1: [2, 6], 2: [1, 5, 3], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [1, 5]}
    initial_state = [1, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_5_dfs():
    method = "DFS"
    spaces = {1: [2, 6], 2: [1, 5, 3], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [1, 5]}
    initial_state = [2, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_6_dfs():
    method = "DFS"
    spaces = {1: [2, 6], 2: [1, 5, 3], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [1, 5]}
    initial_state = [3, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_7_dfs():
    method = "DFS"
    spaces = {1: [2, 6], 2: [1, 5, 3], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [1, 5]}
    initial_state = [4, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_8_dfs():
    method = "DFS"
    spaces = {1: [2, 6], 2: [1, 3, 5], 3: [2, 4], 4: [3, 5, 7], 5: [2, 4, 6, 8], 6: [1, 5, 9], 7: [4, 8], 8: [5, 7, 9],
              9: [6, 8]}
    initial_state = [5, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO'], ['P6', 'NO'],
                     ['P7', 'NO'], ['P8', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


'''----------------------------------------------------------------------------------------------------------------'''
''' Τεστ για BFS '''


def test_1_bfs():
    method = "BFS"
    spaces = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
    initial_state = [1, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_2_bfs():
    method = "BFS"
    spaces = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
    initial_state = [2, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_3_bfs():
    method = "BFS"
    spaces = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
    initial_state = [3, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_4_bfs():
    method = "BFS"
    spaces = {1: [2, 6], 2: [1, 5, 3], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [1, 5]}
    initial_state = [1, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_5_bfs():
    method = "BFS"
    spaces = {1: [2, 6], 2: [1, 5, 3], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [1, 5]}
    initial_state = [2, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_6_bfs():
    method = "BFS"
    spaces = {1: [2, 6], 2: [1, 5, 3], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [1, 5]}
    initial_state = [3, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_7_bfs():
    method = "BFS"
    spaces = {1: [2, 6], 2: [1, 5, 3], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [1, 5]}
    initial_state = [4, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_8_bfs():
    method = "BFS"
    spaces = {1: [2, 6], 2: [1, 3, 5], 3: [2, 4], 4: [3, 5, 7], 5: [2, 4, 6, 8], 6: [1, 5, 9], 7: [4, 8], 8: [5, 7, 9],
              9: [6, 8]}
    initial_state = [5, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO'], ['P6', 'NO'],
                     ['P7', 'NO'], ['P8', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


'''----------------------------------------------------------------------------------------------------------------'''
''' Τεστ για BestFS '''


def test_1_bestfs():
    method = "BestFS"
    spaces = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
    initial_state = [1, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_2_bestfs():
    method = "BestFS"
    spaces = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
    initial_state = [2, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_3_bestfs():
    method = "BestFS"
    spaces = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
    initial_state = [3, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_4_bestfs():
    method = "BestFS"
    spaces = {1: [2, 6], 2: [1, 5, 3], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [1, 5]}
    initial_state = [1, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_5_bestfs():
    method = "BestFS"
    spaces = {1: [2, 6], 2: [1, 5, 3], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [1, 5]}
    initial_state = [2, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_6_bestfs():
    method = "BestFS"
    spaces = {1: [2, 6], 2: [1, 5, 3], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [1, 5]}
    initial_state = [3, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_7_bestfs():
    method = "BestFS"
    spaces = {1: [2, 6], 2: [1, 5, 3], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [1, 5]}
    initial_state = [4, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


def test_8_bestfs():
    method = "BestFS"
    spaces = {1: [2, 6], 2: [1, 3, 5], 3: [2, 4], 4: [3, 5, 7], 5: [2, 4, 6, 8], 6: [1, 5, 9], 7: [4, 8], 8: [5, 7, 9],
              9: [6, 8]}
    initial_state = [5, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO'], ['P6', 'NO'],
                     ['P7', 'NO'], ['P8', 'NO']]
    goal_state = testing(method, initial_state, spaces)
    assert goal_state == True


'''----------------------------------------------------------------------------------------------------------------'''
''' Δυνατότητα να τρέξουμε όλες τις δοκιμές μαζί '''
''' Ίσως παρουσιάσει ένας λάθος στην αρχή αλλά δεν έχει να κάνει με τις δοκιμές, μπορεί να επαληθευτεί με έλεγχο '''


def main():
        test_1_dfs()
        test_2_dfs()
        test_3_dfs()
        test_4_dfs()
        test_5_dfs()
        test_6_dfs()
        test_7_dfs()
        test_8_dfs()

        test_1_bfs()
        test_2_bfs()
        test_3_bfs()
        test_4_bfs()
        test_5_bfs()
        test_6_bfs()
        test_7_bfs()
        test_8_bfs()

        test_1_bestfs()
        test_2_bestfs()
        test_3_bestfs()
        test_4_bestfs()
        test_5_bestfs()
        test_6_bestfs()
        test_7_bestfs()
        test_8_bestfs()


'''--------------------------------------------------------------------------------------------------------------'''
''' Αρχή προγράμματος '''

if __name__ == "__main__":
    main()
