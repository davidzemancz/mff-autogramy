import os
os.environ["PATH"] += os.pathsep + "C:/Program Files (x86)/Graphviz/bin/"

from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from IPython.display import Image, display

nfa = NFA(
    states={'A','B','C','D','X'},
    input_symbols={'a','b','c'},
    transitions={
        'X':{'':{'A','D'}}, # Vsutpni stav, lambda vedou z nej do A,D a do nej z A,D
        'A':{'':{'B','C','X'},'b':{'B'},'c':{'C'}},
        'B':{'a':{'A'},'b':{'C'},'c':{'A','B'}},
        'C':{'':{'D'},'a':{'A'}},
        'D':{'':{'A','X'},'a':{'C','D'}},
        
    },
    initial_state='X',
    final_states={'B','C'}
)

dfa = DFA.from_nfa(nfa)
print(dfa.show_diagram(path="./dfa.png"))

