import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import mininet.net as mn
import ryu as ryu
import hashlib

#DOUBLE CHECK SYNTAX FOR ALL CLASSES

#cryptographic watermark using 9052 SHA-256 NeoDDaBRgX5a9
u_id = "9052"
key = "$NeoDDaBRgX5a9\""
combined_string = u_id + key
encrypted_uid = hashlib.sha256(combined_string.encode()).hexdigest()

class flow_table_entry:
    #flow table entry attributes
    match = {}
    action = ""
    priority = 0
    timeout = 0
    #flow table entry constructor
    def __init__(self, match={}, action=None, priority=0, timeout=None):
        self.match = match
        self.action = action
        self.priority = priority
        self.timeout = timeout

class link:
    #link attributes
    node1_id = 0
    node2_id = 0
    latency = 0
    bandwidth = 0
    utilization = 0
    #link constructor
    def __init__(self, node1_id, node2_id, latency, bandwidth):
        self.node1_id = node1_id
        self.node2_id = node2_id
        self.latency = latency
        self.bandwidth = bandwidth
        self.utilization = 0

class node:
    #node attributes
    node_id = 0
    type = ""
    ip = ""
    mac = ""
    port = 0
    def __init__(self, node_id, type, ip, mac, port):
        self.node_id = node_id
        self.type = type
        self.ip = ip
        self.mac = mac
        self.port = port
        self.links = []
        self.active_flows = []
        self.link_utilization = {}

#node list
node_list = []

#link list
link_list = []

#flow table
flow_table = {}

#active flows
active_flows = {}

#-----------------------------------------------------------------
#main entry point and flow control for program
def main():

    #initialize network topology
    #create nodes
    node1 = create_node()
    node2 = create_node()
    node3 = create_node()
    node4 = create_node()
    node5 = create_node()

    #create links
    link1 = create_link(node1.node_id, node2.node_id)
    link2 = create_link(node2.node_id, node3.node_id)
    link3 = create_link(node3.node_id, node4.node_id)
    link4 = create_link(node4.node_id, node5.node_id)
    link5 = create_link(node5.node_id, node1.node_id)

    #initialize flow generation
    flow1 = create_flow(src_node=node1.node_id, dst_node=node2.node_id)
    flow2 = create_flow(src_node=node2.node_id, dst_node=node3.node_id)
    flow3 = create_flow(src_node=node3.node_id, dst_node=node4.node_id)
    flow4 = create_flow(src_node=node4.node_id, dst_node=node5.node_id)
    flow5 = create_flow(src_node=node5.node_id, dst_node=node1.node_id)

    #create a switch to direct traffic
    net = mn.Mininet()

    #custom CLI
    print("SDN Controller started. Welcome!")
    while True:

        print("Available actions for user:")
        print("1. Add node")
        print("2. Remove node")
        print("3. Add link")
        print("4. Remove link")
        print("5. Add flow")
        print("6. Remove flow")
        print("Enter user action (1-6):")

        action = input()
        match action:
            case 1:
                create_node()
                print("Node created & added to node list.")
            case 2:
                remove_node()
                print("Node removed from node list.")
            case 3:
                create_link()
                print("Link created & added to link list.")
            case 4:
                remove_link()
                print("Link removed from link list.")
            case 5:
                create_flow()
                print("Flow created & added to flow table.")
            case 6:
                remove_flow()
                print("Flow removed from flow table.")
                
#-----------------------------------------------------------------
#network topology and flow generation functions
def create_node(node_id, ip, mac, port, links, active_flows, 
                                link_utilization, **kwargs):
    #create a new node object and initialize its attributes
    node = node()
    node.node_id = node_id
    node.type = kwargs.get('type', 'host')
    node.ip = ip
    node.mac = mac
    node.port = port
    node.links = links
    node.active_flows = active_flows

    node_list.append(node)

def create_link(node1_id, node2_id, **kwargs):
    #create a new link object and initialize its attributes
    link = link()
    link.node1_id = node1_id
    link.node2_id = node2_id
    link.latency = kwargs.get('latency', 0)
    link.bandwidth = kwargs.get('bandwidth', 0)
    link.utilization = kwargs.get('utilization', 0)

    link_list.append(link)

def create_flow(src_node, dst_node, **kwargs):
    #create a new flow object and initialize its attributes
    flow = flow_table_entry()
    flow.src_node_id = src_node
    flow.dst_node_id = dst_node
    flow.match = kwargs.get('match', {})
    flow.action = kwargs.get('action', 'forward')
    flow.priority = kwargs.get('priority', 100)
    flow.timeout = kwargs.get('timeout', None)
    
def remove_node(node_id):
    #remove a node from the network topology
    for node in node_list:
        if node.node_id == node_id:
            node_list.remove(node)
            break
    #remove all links associated with the node
    for link in link_list:
        if link.node1_id == node_id or link.node2_id == node_id:
            link_list.remove(link)
            break
    #remove all flow entries associated with the node
    for flow in active_flows:
        if flow.src_node_id == node_id or flow.dst_node_id == node_id:
            active_flows.remove(flow)
            break

def remove_link(node1_id, node2_id):
    #remove a link from the network topology
    for link in link_list:
        if (link.node1_id == node1_id and link.node2_id == node2_id) or \
           (link.node1_id == node2_id and link.node2_id == node1_id):
            link_list.remove(link)
            break

def remove_flow(flow):
    #remove a flow from the network topology
    for active_flow in active_flows:
        if active_flow.src_node_id == flow.src_node_id and \
           active_flow.dst_node_id == flow.dst_node_id:
            active_flows.remove(active_flow)
            break

def get_topology():
    #return the current network topology
    topology = {}
    topology.append('nodes', node_list)
    topology.append('links', link_list)
    return topology

#double check later
def visualize_network_state(active_flows, link_utilization):
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

def generate_flow_entries(path, flow):
    #generate flow entries for each switch along the path
    pass

def install_flow_rule(switch_id, match_criteria, actions, priority=100):
    pass

def delete_flow_rule(switch_id, match_criteria):
    pass

def apply_routing_policy(flow):
    pass
#-----------------------------------------------------------------
#Failure handling
def handle_link_failure(node1_id, node2_id):
    pass

def get_link_utilization(node1_id, node2_id):
    pass

def update_link_utilization(node1_id, node2_id, utilization):
    pass
#-----------------------------------------------------------------

#execute script
if __name__ == "__main__":
    main()