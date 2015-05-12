class Queue(object):
    def __init__(self):
        self.elements = []
    
    def put(self, element):
        self.elements.append(element)
    
    def get(self):
        element = self.elements[0]
        self.elements = self.elements[1:]
        return element
    
    def empty(self):
        return not self.elements

if __name__=='__main__':
    miCola = Queue()
    miPila = []

    for i in xrange(10):
        miCola.put(i)
        miPila.append(i)

    print "Cola\tPila"
    while not miCola.empty():
        print "{cola}\t\t{pila}".format(cola=miCola.get(), pila=miPila.pop())