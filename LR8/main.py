import networkx as nx
from solution import find_routes
from data import C


def main() -> None:
    print(find_routes(C))

    G = nx.DiGraph(C)
    nx.draw(G, with_labels=True, node_size=300, arrows=True)
    #plt.show()


if __name__ == '__main__':
    main()
