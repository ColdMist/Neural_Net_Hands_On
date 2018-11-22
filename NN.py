from service.NetworkStructure import NetworkStructure
from service.NetworkConnection import Network_Connection

instances = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]
dump = True
num_of_features = len(instances[0]) - 1

hidden_nodes = [3]

nodes = NetworkStructure.create_nodes(num_of_features, hidden_nodes)
#print(type(nodes))
weights = Network_Connection.create_weights(dump, nodes, num_of_features, hidden_nodes)