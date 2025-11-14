import igraph as ig
import random
import math

def simulated_annealing_algorithm(G, k, T, n, theta, T0):
    # Randomly select k edges from the original graph
    Es = random.sample(G.es, k)
    # Set the initial temperature
    temp = T
    
    while temp > T0:
        for i in range(n):
            # Calculate the current communication robustness
            CR0 = G.transitivity_undirected()
            # Randomly change k edges from the original graph
            E_new = random.sample(G.es, k)
            # Calculate the new communication robustness
            G_new = G.copy()
            G_new.add_edges(E_new)
            CR1 = G_new.transitivity_undirected()
            # Calculate the change in communication robustness
            delta = CR1 - CR0
            if delta > 0:
                # Accept the new solution if it improves communication robustness
                Es = E_new
            else:
                # Accept the new solution with a certain probability
                if math.exp(delta / temp) > random.uniform(0, 1):
                    Es = E_new
        # Reduce the temperature
        temp *= theta
    # Return the set of newly added edges
    return Es