import copy
import sys
import time
import numpy as np

sys.setrecursionlimit(10 ** 6)

# The Parking Spaces Diagram
# Διάγραμμα των Χώρων του Πάρκινγκ
#
#   +-------+-------+-------+
#   |   6   |   5   |   4   |
#   +-------+-------+-------+
#   |   1   |   2   |   3   |
#   +-------+-------+-------+
#       ^
#    Entrance
#    Είσοδος


''' Ορίζουμε τα διαθέσιμα πάρκινγκ και τους γείτονές τους. '''
''' Δεκτές τιμές από είσοδος + 1 πάρκινγκ έως είσοδος + όσα πάρκινγκ επιθυμούμε '''


spaces = {}


# The Parking Initial State Diagram
# Διάγραμμα Αρχικής Κατάστασης του Πάρκινγκ
#
#   +-------+-------+-------+
#   | P5 NO | P4 NO | P3 NO |
#   +-------+-------+-------+
#   |   E   | P1 NO | P2 NO |
#   +-------+-------+-------+
#       ^
#   5 vehicles waiting
#   3 οχήματα σε αναμονή


'''--------------------------------------------------------------------------------------------------------------'''
''' Ελέγχουμε εάν υπάρχει άδεια πλατηφόρμα στην είσοδο '''
''' Εάν υπάρχει φορτώνουμε ένα αμάξι '''


def enter(state):
    if state[0] != 0 and state[1][0][0] == 'P' and state[1][1] == 'NO':
        new_state = [state[0] - 1] + [[state[1][0], 'YES']] + state[2:]
        return new_state


'''--------------------------------------------------------------------------------------------------------------'''
''' Ανταλάσουμε τις θέσεις '''


def swap(state_l, i, j):
    state_l[i], state_l[j] = state_l[j], state_l[i]
    return state_l


'''--------------------------------------------------------------------------------------------------------------'''
''' Πρώτος γείτονας. Ελέγχει στο λεξικό (spaces) και διαλέγει τον πρώτο γείτονα '''


def neighbour1(state):
    elem = ['E', 'NO']
    i = state.index(elem) if elem in state else -1
    if i >= 0:
        swap(state, i, spaces[i][0])  # Διαλέγουμε από το λεξικό (spaces) τον πρώτο γείτονα (αυτόν στην θέση 0)
        return state


'''--------------------------------------------------------------------------------------------------------------'''
''' Δεύτερος γείτονας. Ελέγχει στο λεξικό (spaces) και διαλέγει τον δεύτερο γείτονα '''


def neighbour2(state):
    elem = ['E', 'NO']
    i = state.index(elem) if elem in state else -1
    if i >= 0 and len(spaces[i]) == 2:  # Ελέγχουμε αν υπάρχει δεύτερος γείτονας
        swap(state, i, spaces[i][1])  # Διαλέγουμε από το λεξικό (spaces) τον πρώτο γείτονα (αυτόν στην θέση 2)
        return state


'''--------------------------------------------------------------------------------------------------------------'''
''' Τρίτος γείτονας. Ελέγχει στο λεξικό (spaces) και διαλέγει τον τρίτο γείτονα '''


def neighbour3(state):
    elem = ['E', 'NO']
    i = state.index(elem) if elem in state else -1
    if i >= 0 and len(spaces[i]) == 3:  # Ελέγχουμε αν υπάρχει τρίτος γείτονας
        swap(state, i, spaces[i][2])  # Διαλέγουμε από το λεξικό (spaces) τον πρώτο γείτονα (αυτόν στην θέση 3)
        return state


'''--------------------------------------------------------------------------------------------------------------'''
''' Τέταρτος γείτονας. Ελέγχει στο λεξικό (spaces) και διαλέγει τον τέταρτο γείτονα '''


def neighbour4(state):
    elem = ['E', 'NO']
    i = state.index(elem) if elem in state else -1
    if i >= 0 and len(spaces[i]) == 4:  # Ελέγχουμε αν υπάρχει τέταρτος γείτονας
        swap(state, i, spaces[i][3])  # Διαλέγουμε από το λεξικό (spaces) τον πρώτο γείτονα (αυτόν στην θέση 4)
        return state  # Ο μεγαλύτερος αριθμός γειτόνων σε έναν όροφο πάρκιγνκ είναι 4)


'''--------------------------------------------------------------------------------------------------------------'''
''' Εύρεση κόμβων - παιδιών '''


def find_children(state):
    children = []

    enter_state = copy.deepcopy(state)
    enter_child = enter(enter_state)  # Ελέγχουμε αν παράγεται παιδί από την εισαγή αυτοκινήτου στο πάρκινγκ

    tr1_state = copy.deepcopy(state)
    tr1_child = neighbour1(tr1_state)  # Ελέγχουμε αν παράγεται παιδί από τον πρώτο γείτονα

    tr2_state = copy.deepcopy(state)
    tr2_child = neighbour2(tr2_state)  # Ελέγχουμε αν παράγεται παιδί από τον δεύτερο γείτονα

    tr3_state = copy.deepcopy(state)
    tr3_child = neighbour3(tr3_state)  # Ελέγχουμε αν παράγεται παιδί από τον τρίτο γείτονα

    tr4_state = copy.deepcopy(state)
    tr4_child = neighbour4(tr4_state)  # Ελέγχουμε αν παράγεται παιδί από τον τέταρτο γείτονα

    # Για κάθε παιδί που παράχθηκε το τοποθετούμε στο τέλος της children

    if tr1_child is not None:
        children.append(tr1_child)

    if tr2_child is not None:
        children.append(tr2_child)

    if tr3_child is not None:
        children.append(tr3_child)

    if tr4_child is not None:
        children.append(tr4_child)

    if enter_child is not None:
        children.append(enter_child)

    return children


'''--------------------------------------------------------------------------------------------------------------'''
''' Δημιουργία Μετώπου '''


def make_front(state):
    return [state]


'''--------------------------------------------------------------------------------------------------------------'''
''' Επέκταση Μετώπου '''


def expand_front(front, method):
    if method == 'DFS':  # Εκτελείται αν έχουμε επιλέξει την μέθοδο DFS (Depth First Search)
        if front:
            # print("Front:")
            # print(front)
            node = front.pop(0)  # Βγάζει τον πατρικό κόμβο απο το μέτωπο και τον βάζει στο node
            for child in find_children(node):  # Η find_children επιστρέφει τα παιδιά και ένα ένα μπαίνουν στην
                front.insert(0, child)  # αρχή του μετώπου

    elif method == 'BFS':  # Εκτελείται αν έχουμε επιλέξει την μέθοδο DFS (Breath First Search)
        if front:
            # print("Front:")
            # print(front)
            node = front.pop(0)  # Αφαιρούμε τον πατρικό κόμβο και τον βάζουμε στο node για να παράγουμε παιδιά
            for child in find_children(node):  # Η find_children επιστρέφει τα παιδιά και ένα ένα μπαίνουν στο
                front.append(child)  # τέλος του μετώπου

    elif method == 'BestFS':  # Εκτελείται αν έχουμε επιλέξει την μέθοδο BestFS (Best First Search)
        if front:
            # print("Front:")
            # print(front)
            node = front.pop(0)  # Αφαιρούμε τον πατρικό κόμβο και τον βάζουμε στο node για να παράγουμε παιδιά
            for child in find_children(node):  # Η find_children επιστρέφει τα παιδιά και ένα ένα μπαίνουν στο
                front.insert(0, child)  # τέλος του μετώπου
            # Στην συνέχεια ταξινομούμε τους κόμβους που βρίσκονται στο μέτωπο σύμφωνα με το ευριστικό κριτήριο
            front = sort_front(front, node)

    return front


'''--------------------------------------------------------------------------------------------------------------'''
''' Ταξινόμηση μετώπου '''


def sort_front(front, node):
    distances = []  # Απόσταση από τον στόχο κάθε κόμβου - παιδιού
    sorted_front = []  # Εδώ θα αποθηκέυσουμε το ταξινομημένο μέτωπο

    # Ελέγχουμε αν στην είσοδο υπάρχει πλατηφόρμα και αν αυτή έχει αυτοκίνητο
    for count in range(len(front)):  # Για κάθε κόμβο του μετώπου
        platform = bool(front[count][1][0][0] == 'P')  # Ελέγχουμε αν υπάρχει πλατηφόρμα στην είσοδο
        parked = bool(front[count][1][1] == 'YES')  # Ελέγχουμε αν υπάρχει αμάξι στην πλατηφόρμα
        node_check = bool(node[1][1] == 'YES')  # Ελέγχουμε αν ο πατρικός κόμβος είχε πλατηφόρμα και αμάξι

        # Το παρακάτω ευριστικό κριτήριο αντιστοιχεί σε κάθε παιδί μια απόσταση.
        # Η απόσταση υπολογίζεται σύμφωνα με το πόσο κοντά είναι μια πλατηφόρμα στο να έχει μόλις φορτώσει αμάξι
        # Εξετάζουμε αν το παιδί που παράχθηκε έχει στην είσοδο:
        # 1. Πλατηφόρμα με αμάξι, δηλαδή μόλις φόρτωσε ένα αμάξι
        # 2. Κενό
        # 3. Πλατηφόρμα χωρίς αμάξι

        if platform and parked:
            if node_check:
                distances.append(4)  # Αν ο πατρικός κόμβος είχε φορτώσει παιδί και στο επόμενο βήμα εξακολουθεί
                # να μην έχει μετακινηθεί η γεμάτη πλατηφόρμα τότε της δίνουμε την μεγαλύτερη
                # δυνατή προτεραιότητα
            else:
                distances.append(1)  # Δίνουμε την μικρότερη απόσταση στο παιδί που προέκυψε από φόρτωση αμαξιού
        elif not platform:
            distances.append(2)  # Την αμέσως μεγαλύτερη αν υπάρχει κενό
        elif platform and not parked:
            distances.append(3)  # Και μεγαλύτερη από όλες στο να έχει πλατοφόρμα χωρίς αμάξι

    temp_array = np.array(distances)  # Δημιουγρούμε έναν numpy array με όλες τις αποστάσεις που υπολογίσαμε
    sorted_distances_indexes = np.argsort(temp_array)  # Το np.argsort μας επιστρέφει ένα array που περιέχει
    # ταξινομημένα τα indexes των αποστάσεων.

    for i in sorted_distances_indexes:
        sorted_front.append(front[i])  # Σύμφωνα με τα indexes ταξινομούμε και το μέτωπο.

    return sorted_front


'''--------------------------------------------------------------------------------------------------------------'''
''' Δημιουργία Ουράς '''


def make_queue(state):
    return [[state]]


'''--------------------------------------------------------------------------------------------------------------'''
''' Επέκταση Ουράς '''


def extend_queue(queue, method):
    if method == 'DFS':  # Εκτελείται αν έχουμε επιλέξει την μέθοδο DFS (Depth First Search)
        # print("Queue:")
        # print(queue)
        node = queue.pop(0)  # Βγάζει την διαδρομή καθώς και τον πατρικό κόμβο από την ουρά και τα βάζει στο node
        queue_copy = copy.deepcopy(queue)
        children = find_children(node[-1])  # Η find_children επιστρέφει τα παιδιά και τα path αυτών μπάινουν
        for child in children:  # στην αρχή της ουράς
            path = copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0, path)

    elif method == 'BFS':  # Εκτελείται αν έχουμε επιλέξει την μέθοδο ΒFS (Breath First Search)
        # print("Queue:")
        # print(queue)
        node = queue.pop(0)
        queue_copy = copy.deepcopy(queue)
        children = find_children(node[-1])  # Η find_children επιστρέφει τα παιδιά και τα path αυτών μπάινουν
        for child in children:  # στο τέλος της ουράς
            path = copy.deepcopy(node)
            path.append(child)
            queue_copy.append(path)

    elif method == 'BestFS':  # Εκτελείται αν έχουμε επιλέξει την μέθοδο BestFS (Best First Search)
        # print("Queue:")
        # print(queue)
        node = queue.pop(0)
        queue_copy = copy.deepcopy(queue)
        children = find_children(node[-1])  # Η find_children επιστρέφει τα παιδιά και τα path αυτών μπάινουν
        for child in children:  # στην αρχή της ουράς
            path = copy.deepcopy(node)
            path.append(child)
            queue_copy.append(path)
    # Στην συνέχεια ταξινομούμε την ουρά μέτωπο σύμφωνα με το ευριστικό κριτήριο
    queue_copy = sort_queue(queue_copy, node)

    return queue_copy


'''--------------------------------------------------------------------------------------------------------------'''
''' Ταξινόμηση ουράς '''


def sort_queue(queue, node):
    distances = []  # Απόσταση από το στόχο κάθε κόμβου - παιδιού
    sorted_queue = []  # Εδώ θα αποθηκέυσουμε την ταξινομημένη ουρά

    # Ελέγχουμε αν στην είσοδο υπάρχει πλατηφόρμα και αν αυτή έχει αυτοκίνητο
    for count in range(len(queue)):  # Για κάθε κόμβο του μετώπου
        platform = bool(queue[count][-1][1][0][0] == 'P')  # Ελέγχουμε αν υπάρχει πλατηφόρμα στην είσοδο
        parked = bool(queue[count][-1][1][1] == 'YES')  # Ελέγχουμε αν υπάρχει αμάξι στην πλατηφόρμα
        node_check = bool(node[0][1][1] == 'YES')  # Ελέγχουμε αν ο πατρικός κόμβος είχε πλατηφόρμα και αμάξι

        # Το παρακάτω ευριστικό κριτήριο αντιστοιχεί σε κάθε παιδί μια απόσταση.
        # Η απόσταση υπολογίζεται σύμφωνα με το πόσο κοντά είναι μια πλατηφόρμα στο να έχει μόλις φορτώσει αμάξι
        # Εξετάζουμε αν το παιδί που παράχθηκε έχει στην είσοδο:
        # 1. Πλατηφόρμα με αμάξι, δηλαδή μόλις φόρτωσε ένα αμάξι
        # 2. Κενό
        # 3. Πλατηφόρμα χωρίς αμάξι

        if platform and parked:
            if node_check:
                distances.append(4)  # Αν ο πατρικός κόμβος είχε φορτώσει παιδί και στο επόμενο βήμα εξακολουθεί
                # να μην έχει μετακινηθεί η γεμάτη πλατηφόρμα τότε της δίνουμε την μεγαλύτερη
                # δυνατή προτεραιότητα
            else:
                distances.append(1)  # Δίνουμε την μικρότερη απόσταση στο παιδί που προέκυψε από φόρτωση αμαξιού
        elif not platform:
            distances.append(2)  # Την αμέσως μεγαλύτερη αν υπάρχει κενό
        elif platform and not parked:
            distances.append(3)  # Και μεγαλύτερη από όλες στο να έχει πλατοφόρμα χωρίς αμάξι

    temp_array = np.array(distances)  # Δημιουγρούμε έναν numpy array με όλες τις αποστάσεις που υπολογίσαμε
    sorted_distances_indexes = np.argsort(temp_array)  # Το np.argsort μας επιστρέφει ένα array που περιέχει
    # ταξινομημένα τα indexes των αποστάσεων.

    for i in sorted_distances_indexes:
        sorted_queue.append(queue[i])  # Σύμφωνα με τα indexes ταξινομούμε και το μέτωπο.

    return sorted_queue


'''--------------------------------------------------------------------------------------------------------------'''
''' Μέθοδος για την χρήση ελέγχων '''


def testing(method, initial_state, imported_spaces):
    global spaces
    spaces = imported_spaces
    return find_solution(make_front(initial_state), make_queue(initial_state), [], method)


'''--------------------------------------------------------------------------------------------------------------'''
''' Έλεγχος μετώπου για εύρεση λύσης, απόρριψη κόμβου, αδυναμία εύρεσης λύσης '''


def find_solution(front, queue, closed, method):
    if not front:  # Ελέγχει αν υπάρχουν κόμβοι στο μέτωπο
        print('_NO_SOLUTION_FOUND_')  # Αν είναι άδειο τότε δεν έχουμε λύση
        return False

    elif front[0] in closed:  # Ελέγχει αν το πρώτο στοιχείο του μετώπου βρίσκεται στο κλειστό σύνολο ώστε να απορριφθεί
        new_front = copy.deepcopy(front)
        new_front.pop(0)  # Αφαιρούμε τον κόμβο που έχουμε ήδη επισκεφθεί
        new_queue = copy.deepcopy(queue)
        new_queue.pop(0)  # Αφαιρούμε από την ουρά την διαδρομή του κόμβου που έχουμε ήδη επισκεφθεί
        goal = find_solution(new_front, new_queue, closed, method)

    elif is_goal_state(front[0]):  # Ελέγχει αν ο κόμβος είναι λύση
        # print('_GOAL_FOUND_')
        #print("Front:")
        #print(front[0])
        #print("Queue:")
        #print(queue)
        return True

    else:
        closed.append(front[0])  # Βάζουμε τον κόμβο που θα εξετάσουμε στον κλειστό σύνολο
        front_copy = copy.deepcopy(front)
        front_children = expand_front(front_copy, method)  # Κάνουμε επέκταση του μετώπου
        queue_copy = copy.deepcopy(queue)
        queue_children = extend_queue(queue_copy, method)  # Κάνουμε επέκταση της ουράς
        closed_copy = copy.deepcopy(closed)
        goal = find_solution(front_children, queue_children, closed_copy, method)
    return goal


'''--------------------------------------------------------------------------------------------------------------'''
''' Ελέγχει αν έχει βρεθεί λύση '''


def is_goal_state(front):
    return bool(front[0] == 0)  # Αν δεν περιμένουν αμάξια επιστρέφει true αλλίως false


'''--------------------------------------------------------------------------------------------------------------'''
''' Συνάρτηση main '''


def main():
    # Αρχική κατάσταση
    initial_state = [4, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]

    # Επιλογή μεθόδου χεροκίνητα
    method = "BestFS"

    # Έναρξη χρονόμετρου
    start_time = time.time()

    # Έναρξη αναζήτησης
    print('____BEGIN__SEARCHING____')
    find_solution(make_front(initial_state), make_queue(initial_state), [], method)

    # Εκτύπωση χρόνου εκτέλεσης
    print('____Time elapsed:____')
    print((time.time() - start_time), 'seconds')  # Χρόνος που χρειάστηκε για να ολοκληρωθεί η αναζήτηση


'''--------------------------------------------------------------------------------------------------------------'''
''' Αρχή προγράμματος '''

if __name__ == "__main__":
    main()
