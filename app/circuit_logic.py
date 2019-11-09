class Circuit:

    def __init__(self, components):
        """ Assign electrical components
            to the circuit.

            :param components:
            list of Resistor; Capacitor; ... Objects,
            electrical components in circuit

            :return: Boolean,
            True if succeeded
        """

        self.branches = []

        # at least one source component has
        # to exist.
        source_exists = False

        # Create a new list of branches.
        # Each branch is a dictionary that
        # represents one electrical component
        # with its corresponding voltage and
        # current.
        for comp in components:
            if type(comp) == Source:
                source_exists = True
            self.branches.append({
                'component': comp,
                'voltage': None,
                'current': None,
            })

        if not source_exists:
            self.branches = None
            raise Exception('No sour


class Component:

    connections = []

    def connect(self, component):

        # each component has max two connections
        if len(self.connections) < 3:
            self.connections.append(component)
        else: raise Exception('Only two connections per electrical component allowed.')


class Source(Component):
    pass


class Resistor(Component):

    def __init__(self, resistance):
        self.resistance = resistance


class Capacitor(Component):

    def __init__(self, capacitance):
        self.capacitance = capacitance


class Simulation:

    def __init__(self, circuit):
        self.circuit = circuit

    def simulate(self):
        source_index = self.find_source()

    def find_source(self):
        for i, branch in enumerate(self.circuit.branches):
            if type(branch['component']) == Source:
                return i


