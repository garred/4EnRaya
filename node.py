# -*- coding: utf-8 -*-

from queue import *

class Node(object):
    """Simple implementation of a tree, with differents traversals.
    """
    
    def __init__(self, parent=None, **data):
        """Create a node with a set of attributes.
        """
        self.user_data = [] #Holds all the initial keys 
        for key in data:
            setattr(self, key, data[key])
            self.user_data.append(key)
        self.children = []
        if parent!=None: parent.new_son(self)

    def __repr__(self):
        data = ["{}={}".format(key, self.__dict__[key]) for key in self.user_data]
        return "Node({})".format(data)

    def __str__(self):
        data = ["{}={}".format(key, self.__dict__[key]) for key in self.user_data]
        return "{}".format(data)
    
    def new_son(self, child):
        """Add a child node to a list of children of a node.
        Precondition: child must be a Node.
        """
        self.children.append(child)
        self.children[-1].parent = self
    
    def pre_order(self):
        """Returns a list with the nodes of the tree, ordered by a pre-order
        traversal.
        """
        pre_ordered_list = [self]
        for child in self.children:
            pre_ordered_list = pre_ordered_list + child.pre_order()
        return pre_ordered_list
    
    def in_order(self):
        """Returns a list with the nodes of the tree, ordered by an in-order
        traversal.
        """
        in_ordered_list = []
        for child in self.children:
            in_ordered_list = in_ordered_list + child.in_order()
        if in_ordered_list:
            in_ordered_list = in_ordered_list[:1] +[self]+ in_ordered_list[1:]
        else:
            in_ordered_list = [self]            
        return in_ordered_list

    def post_order(self):
        """Returns a list with the nodes of the tree, ordered by an post-order
        traversal.
        """
        post_ordered_list = []
        for child in self.children:
            post_ordered_list = post_ordered_list + child.post_order()
        post_ordered_list = post_ordered_list + [self]
        return post_ordered_list
    
    def level_order(self):
        """Returns a list with the tree's nodes, ordered by a level-order
        traversal.
        Precondition: self it's considered a root, with no siblings.
        """
        level_ordered_list = []
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            next_node = queue.get()
            level_ordered_list.append(next_node)

            for child in next_node.children:
                queue.put(child)

        return level_ordered_list

def print_tree(node, depth=0):
    """Prints a tree from *node*.
    """
    if depth==0:
        print str(node)
    else:
        print "|  "*(depth)
        print "|  "*(depth-1) + "|--" + str(node)
    for child in node.children:
        print_tree(child, depth+1)


inf = float("inf")


def minimax(node, depth=-1, maximizingPlayer=True, default_value=0.0):
    """A minimax exploration function.
    Notes: Some leaf nodes should have the attribute *heuristic_value*. If it 
    doesn't, *default_value* is used.
    Reference: http://en.wikipedia.org/wiki/Minimax#Pseudocode
    """
    if hasattr(node, 'heuristic_value'):
        return node.heuristic_value
    elif depth==0 or not node.children:
        return default_value

    if maximizingPlayer:
        best_value = -inf
        for child in node.children:
            value = minimax(child, depth-1, False)
            best_value = max(best_value, value)
        return best_value

    else:
        best_value = inf
        for child in node.children:
            value = minimax(child, depth-1, True)
            best_value = min(best_value, value)
        return best_value


def alpha_beta(
    node, depth=-1, 
    alpha=-inf, beta=inf,
    maximizingPlayer=True,
    default_value=0.0
    ):
    """
    Reference: http://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#Pseudocode
    """
    if hasattr(node, 'heuristic_value'):
        return node.heuristic_value
    elif depth==0 or not node.children:
        return default_value

    if maximizingPlayer:
        v = -inf
        for child in node.children:
            v = max(v, alpha_beta(child, depth-1, alpha, beta, False, default_value))
            alpha = max(alpha, v)
            if alpha > beta:
                break
        return v

    else:
        v = inf
        for child in node.children:
            v = min(v, alpha_beta(child, depth-1, alpha, beta, True, default_value))
            beta = min(beta, v)
            if alpha > beta:
                break
        return v


###############################################################################
##########################    ###    ##########################################
###############################################################################
##########################   #####   ##########################################
# TESTS #######################################################################
##############################   ##############################################
########################## ########## #########################################
###########################          ##########################################
###############################################################################

if __name__=="__main__":
    from depth_decorator import *
    import random

    random.seed(3)   


    def ejemplo_diccionario_ed():
        print "\nEjemplo diccionario ED:"

        root = Node(parent=None, data='_')
        Node(parent=root, data='a')
        Node(parent=root, data='b')
        Node(parent=root, data='c')
        
        Node(parent=root.children[0], data='m')
        
        Node(parent=root.children[0].children[0], data='a')
        Node(parent=root.children[0].children[0], data='o')

        Node(parent=root.children[0].children[0].children[0], data='r')
        Node(parent=root.children[0].children[0].children[1], data='r')

        Node(parent=root.children[1], data='a')
        Node(parent=root.children[1], data='o')

        Node(parent=root.children[1].children[0], data='r')
        Node(parent=root.children[1].children[0].children[0], data='i')

        Node(parent=root.children[1].children[1], data='a')

        Node(parent=root.children[2], data='a')
        Node(parent=root.children[2], data='o')

        Node(parent=root.children[2].children[0], data='l')
        Node(parent=root.children[2].children[1], data='l')
        Node(parent=root.children[2].children[1], data='z')

        print_tree(root)
        
        print "\nPreorden: ",
        for node in root.pre_order():
            print node.data,
        
        print "\nInorden: ",
        for node in root.in_order():
            print node.data,
        
        print "\nPostorden: ",
        for node in root.post_order():
            print node.data,
        
        print "\nPor niveles: ",
        for node in root.level_order():
            print node.data,
        print "\n"


    def ejemplo_minimax_ia():
        print "\nEjemplo minimax:"
        
        root = Node()
        
        ab = Node(parent=root)
        Node(parent=ab, heuristic_value=10)
        Node(parent=ab, heuristic_value=-3)

        cde = Node(parent=root)
        Node(parent=cde, heuristic_value=-4)
        Node(parent=cde, heuristic_value=9)
        Node(parent=cde, heuristic_value=99)

        f = Node(parent=root)
        Node(parent=f, heuristic_value=1)

        print_tree(root)

        print "Minimax: {}".format(minimax(root, depth=2, maximizingPlayer=True))


    def ejemplo_alfa_beta():
        print "\nEjemplo alfa-beta"

        def crear_subarbol_aleatorio(
            nodo, 
            anchura=3, 
            probabilidad_con_descendencia=1.0, 
            factor_probabilidad_descendencia=0.25):

            for i in xrange(anchura):
                hijo = None
                if random.random() < probabilidad_con_descendencia:
                    hijo = Node(parent=nodo)
                    crear_subarbol_aleatorio( 
                        hijo,
                        anchura,
                        probabilidad_con_descendencia*factor_probabilidad_descendencia,
                        factor_probabilidad_descendencia)
                else:
                    hijo = Node(
                        parent=nodo,
                        heuristic_value=random.randint(-100,100)
                        )

        raiz = Node()
        crear_subarbol_aleatorio(raiz)
        print_tree(raiz)
        print
        print "Alfa-beta: {}".format(alpha_beta(raiz))
        print "Minimax: {}".format(minimax(raiz))


        raiz = None
        for _ in xrange(1000):
            raiz = Node()
            crear_subarbol_aleatorio(raiz)
            # print "Alfa-beta: {}, Minimax: {}"\
            # .format(alpha_beta(raiz), minimax(raiz))
            assert(minimax(raiz)==alpha_beta(raiz))
        print "Todo correcto."



    # Se pueden decorar las funciones para estudiar su ejecuci´on
    #Node.pre_order = depth_decorator(Node.pre_order)
    #Node.in_order = depth_decorator(Node.in_order)
    #Node.post_order = depth_decorator(Node.post_order)
    #minimax = depth_decorator(minimax)
    #alpha_beta = depth_decorator(alpha_beta)

    # Ejemplo del diccionario de Rosa
    ejemplo_diccionario_ed()

    # Ejemplo de la relaci´on de problemas 3 de IA
    ejemplo_minimax_ia()

    # Ejemplo de la relaci´on de problemas 3 de IA
    ejemplo_alfa_beta()