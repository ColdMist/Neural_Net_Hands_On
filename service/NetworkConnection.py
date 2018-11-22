from entity.Weight import Weight
import math
import random

class Network_Connection:
    def create_weights(dump,nodes, num_of_features, hidden_nodes):
        weights = []
        total_layers = 1 + len(hidden_nodes) + 1
        weight_index = 0

        for  i in range (total_layers -1):
            for j in range (len(nodes)):
                if nodes[j].get_level() == i:
                    for k in range(len(nodes)):
                        if nodes[k].get_level() == i+1:
                            if nodes[k].get_is_bias_unit() == False:
                                #There should be connection from node j to node k
                                range_min = 0
                                range_max = 1
                                init_epsilon = math.sqrt(6)/(math.sqrt(num_of_features) + 1)
                                rand = range_min + (range_max - range_min)*random.random()
                                rand = rand * (2 * init_epsilon) - init_epsilon

                                weight = Weight()
                                weight.set_set_weight_index(weight_index)
                                weight.set_from_node_index(nodes[j].get_index())
                                weight.set_to_node_index(nodes[k].get_index())
                                weight.set_value(rand)
                                weight_index += 1

                                weights.append(weight)

                                print("from " + str(nodes[j].get_label()) + " to " + str(nodes[k].get_label()) + ": " + str(rand))
        return weights


