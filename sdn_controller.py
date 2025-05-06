import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import mininet as mn
import ryu as ryu

class node:
    #all node attributes
    node_id = node_id
    type = kwargs.get('type', 'host')
    ip = kwargs.get('ip', None)
    mac = kwargs.get('mac', None)
    port = kwargs.get('port', None)
    links = kwargs.get('links', [])
    active_flows = kwargs.get('active_flows', [])
    link_utilization = kwargs.get('link_utilization', {})

#-----------------------------------------------------------------
#main entry point and flow control for program
def main():
    pass
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#network topology and flow generation functions
def create_node(node_id, **kwargs):

    pass

def create_link(node1_id, node2_id, **kwargs):
    pass

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