import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import mininet.net as mn
from mininet.topo import Topo
import hashlib

#node list
node_list = []

#link list
link_list = []

#flow table
flow_table = []

#cryptographic watermark
u_id = "9052"
key = "$NeoDDaBRgX5a9"
uid_key = u_id + key
encrypted_uid = hashlib.sha256(uid_key.encode()).hexdigest()

path = None
class flow_table_entry:
    #flow table entry constructor
    def __init__(self, match=None, action=None, priority=100, timeout=None):
        self.match = match if match is not None else {}
        self.action = action
        self.priority = priority
        self.timeout = timeout
    
class Topology(Topo):
    def build(self):
        # Define your switches (5 in a ring)
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')

        # Define your hosts (5 hosts)
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')

        # Add links between switches to form a ring
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s5, s1)

        # Add links between hosts and switches (example: each host connected to a different switch)
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)
        self.addLink(h5, s5)
#-----------------------------------------------------------------
#main entry point and flow control for program
def main():
    #initialize network topology
    sdnc_topo = Topo.build()

    #create switches to direct traffic
    net = mn.Mininet(topo = sdnc_topo)
    
    #custom CLI
    print("SDN Controller started. Welcome! :)")
    print("Authored by Cooper Belala, Encrypted ID: " + encrypted_uid)
    while True:
        print("Available actions for user:")
        print("1. Add node")
        print("2. Remove node")
        print("3. Add link")
        print("4. Remove link")
        print("5. Add flow")
        print("6. Remove flow")
        print("7. Exit")
        print("Enter user action (1-7): ")
        action = input()
        match action:
            case 1:
                print("Enter node name to add: ")
                node_name = input()
                net.addHost(node_name)
                node_list.append(node_name)
                print("Node created & added to node list.")
            case 2:
                print("Enter node name to remove: ")
                node_name = input()
                for node in node_list:
                    if node == node_id:
                        node_list.remove(node)                        
                    else:
                        print("Node not found.")
                print("Node removed from node list.")
            case 3:
                print("Enter name of node to link: ")
                node1_name = input()
                print("Enter name of node to be linked: ")
                node2_name = input()
                net.addLink(node1_name, node2_name)
                print("Link created & added to link list.")
            case 4:
                print("Enter name of node to unlink: ")
                node1_name = input()
                print("Enter name of node to be unlinked: ")
                node2_name = input()
                for link in link_list:
                    if link.node1_id == node1_name and link.node2_id == node2_name:
                        link_list.remove(link)
                        break
                else:
                    print("Link not found.")
                print("Link removed from link list.")
            case 5:
                create_flow()
                print("Flow created & added to flow table.")
            case 6:
                remove_flow()
                print("Flow removed from flow table.")
            case 7:
                print("Exiting SDN Controller.")
                break
            case _:
                print("Invalid action. Please try again.")

    print("Controller closed. Goodbye! :(")
#-----------------------------------------------------------------
#network topology and flow generation functions
def create_flow(src_node, dst_node, **kwargs):
    #create a flow from src_node to dst_node
    flow = {
        'src': src_node,
        'dst': dst_node,
        'match': kwargs.get('match', {}),
        'action': kwargs.get('action', {}),
        'priority': kwargs.get('priority', 100),
        'timeout': kwargs.get('timeout', None)
    }
    flow_table[flow['src'] + flow['dst']] = flow
    flow_table.append(flow)

def remove_flow(flow):
    #remove a flow from the network topology
    for entry in flow_table:
        if entry['src'] == flow['src'] and entry['dst'] == flow['dst']:
            flow_table.remove(entry)
            break
    else:
        print("Flow not found.")

def visualize_network_state(active_flows):
    #create a visualization of the network state
    plt.figure(figsize=(10, 6))
    G = nx.Graph()
    for node in node_list:
        G.add_node(node.node_id, label=node.node_id)
    for link in link_list:
        G.add_edge(link.node1_id, link.node2_id, weight=link.latency)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title('Network Topology')
    plt.show()
#-----------------------------------------------------------------
#Pathfinding computation and routing
def compute_shortest_path(src_node_id, dst_node_id, weight='latency'):
    #compute the shortest path between two nodes using Dijkstra's algorithm
    G = nx.Graph()
    for link in link_list:
        G.add_edge(link.node1_id, link.node2_id, weight=link.latency)
    path = nx.dijkstra_path(G, src_node_id, dst_node_id, weight=weight)
    return path

def install_flow_rule(switch_id, match_criteria, actions, priority=100):
    #install a flow rule on the switch
    flow_rule = flow_table_entry(match=match_criteria, action=actions, priority=priority)
    flow_table.append(flow_rule)

def delete_flow_rule(switch_id, match_criteria):
    #delete a flow rule from the switch
    for entry in flow_table:
        if entry.match == match_criteria:
            flow_table.remove(entry)
            break
    else:
        print("Flow rule not found.")
#-----------------------------------------------------------------

#execute script
if __name__ == "__main__":
    main()