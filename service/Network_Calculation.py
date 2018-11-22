class Network_Calculation:
    def apply_forward_propagation(nodes, weights, instance):
        for j in range(len(nodes)):
            if nodes[j].get_is_bias_unit() == True:
                nodes.set_net_value(1)

        # instance = [0, 0, 0]
        for j in range(len(instance) - 1):
            var = instance[j]


        return nodes