import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import mininet as mn
import ryu as ryu

#DOUBLE CHECK SYNTAX FOR ALL CLASSES

class flow_table_entry:
    #flow table entry attributes
    def __init__(self, match={}, action=None, priority=0, timeout=None):
        self.match = match
        self.action = action
        self.priority = priority
        self.timeout = timeout

class link:
    #link attributes
    def __init__(self, node1_id, node2_id, latency, bandwidth):
        self.node1_id = node1_id
        self.node2_id = node2_id
        self.latency = latency
        self.bandwidth = bandwidth
        self.utilization = 0
class node:
    #node attributes
    def __init__(self, node_id, type, ip, mac, port):
        self.node_id = node_id
        self.type = type
        self.ip = ip
        self.mac = mac
        self.port = port
        self.links = []
        self.active_flows = []
        self.link_utilization = {}
        
class packet:
    #packet attributes
    def __init__(self, src_ip=None, dst_ip=None, src_mac=None, dst_mac=None, protocol=None, payload=None):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.protocol = protocol
        self.payload = payload

#-----------------------------------------------------------------
#main entry point and flow control for program
def main():
    #parse command line arguments

    #initialize network topology

    #create nodes and links

    #initialize flow generation

    #start the network controller

    #pass in test nodes
    pass
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#network topology and flow generation functions
def create_node(node_id, ip, mac, port, links, active_flows, link_utilization, **kwargs):
    #create a new node object and initialize its attributes
    node = node()
    node.node_id = node_id
    node.type = kwargs.get('type', 'host')
    node.ip = ip
    node.mac = mac
    node.port = port
    node.links = links
    node.active_flows = active_flows

def create_link(node1_id, node2_id, **kwargs):
    #create a new link object and initialize its attributes
    link = link()
    link.node1_id = node1_id
    link.node2_id = node2_id
    link.latency = kwargs.get('latency', 0)
    link.bandwidth = kwargs.get('bandwidth', 0)
    link.utilization = kwargs.get('utilization', 0)
    return link

def remove_node(node_id):
    pass

def remove_link(node1_id, node2_id):
    pass

def get_topology():
    pass

def visualize_network_state(active_flows, link_utilization):
    pass
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#Pathfinding computation and routing
def compute_shortest_path(src_node_id, dst_node_id, weight='latency'):
    pass

def generate_flow_entries(path, flow):
    pass

def install_flow_rule(switch_id, match_criteria, actions, priority=100):
    pass

def delete_flow_rule(switch_id, match_criteria):
    pass

def apply_routing_policy(flow):
    pass
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#Failure handling
def handle_link_failure(node1_id, node2_id):
    pass

def get_link_utilization(node1_id, node2_id):
    pass

def update_link_utilization(node1_id, node2_id, utilization):
    pass
#-----------------------------------------------------------------

if __name__ == "__main__":
    main()