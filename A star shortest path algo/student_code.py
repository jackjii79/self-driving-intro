import math
import collections

#idx -- vertex index; heap_idx -- position index in the heap; distance -- path that have been explored so far; parent -- parent vertex #index; overallcost -- path cost + heuristic cost
class Node:
    def __init__(self, idx, distance, heap_idx, overallcost):
        self.idx, self.heap_idx, self.distance, self.parent, self.overallcost = idx, heap_idx, distance, None, overallcost       
        
#MIN_heap will be used whenever we need to find the minimum overallcost vertex
class MIN_heap:
    def __init__(self):
        self.min_heap, self.size = [], 0
    
    def pop(self):
        if len(self.min_heap) > 0:
            result = self.min_heap[0]
            #here we switch the node position in the heap as well as its heap_idx
            self.min_heap[0].heap_idx, self.min_heap[-1].heap_idx = len(self.min_heap)-1, 0
            self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
            self.min_heap.pop()
            self.sift_down(0)
            self.size -= 1
            return result
        
    def push(self, node):
        self.min_heap.append(node)
        self.sift_up(len(self.min_heap)-1)
        self.size += 1
        
    def sift_down(self, idx):
        while idx < len(self.min_heap):
            min_idx = idx
            if idx*2+1 < len(self.min_heap) and self.min_heap[idx*2+1].overallcost < self.min_heap[idx].overallcost:
                min_idx = idx*2+1
            if idx*2+2 < len(self.min_heap) and self.min_heap[idx*2+2].overallcost < self.min_heap[min_idx].overallcost:
                min_idx = idx*2+2
            if idx == min_idx:
                break
            else:
                self.min_heap[idx].heap_idx, self.min_heap[min_idx].heap_idx = min_idx, idx
                self.min_heap[idx], self.min_heap[min_idx] = self.min_heap[min_idx], self.min_heap[idx]
                idx = min_idx
                
    def sift_up(self, idx):
        while idx != 0 and self.min_heap[int((idx-1)/2)].overallcost > self.min_heap[idx].overallcost:
            self.min_heap[idx].heap_idx, self.min_heap[int((idx-1)/2)].heap_idx = int((idx-1)/2), idx
            self.min_heap[idx], self.min_heap[int((idx-1)/2)] = self.min_heap[int((idx-1)/2)], self.min_heap[idx]
            idx = int((idx-1)/2)
            
    def is_empty(self):
        return self.size == 0
    
    def maintenance(self, idx):
        self.sift_up(idx)
        self.sift_down(idx)
    
#Graph class will perform A start algorithm 
#adjacent_list -- neighbor vertex list for each vertex; coordinate_map -- vertex coordinate; source -- start vertex index;
#goal -- destination vertex index; explored_list -- set used to maintain explored vertex list; vertices -- number of vertex in graph;
#result_list -- shortest path; MIN_heap -- priority queue; node_list -- vertex node stored in heap, so that we can easily access node #from the priority queue
class Graph:
    def __init__(self, M, start, goal):
        self.adjacent_list, self.coordinate_map, self.source, self.goal = M.roads, M.intersections, start, goal
        self.explored_list, self.vertices, self.result_list = set(), len(self.coordinate_map.keys()), collections.deque()
        self.MIN_heap, self.node_list = MIN_heap(), [None for i in range(self.vertices)]

    #compute straight line distance between two vertex
    def compute_distance(self, start, end):
        return math.sqrt(pow(self.coordinate_map[start][0]-self.coordinate_map[end][0], 2) + pow(self.coordinate_map[start][1]-self.coordinate_map[end][1], 2))

    #compute straight distance between vertex and goal as heuristic cost
    def heuristic_function(self, idx):
        return self.compute_distance(idx, self.goal)
    
    #length for each edge connecting two vertex
    def edge_function(self, sour, dest):
        return self.compute_distance(sour, dest)
    
    #relax overall cost and path cost distance
    def relax_path_cost(self, dest, sour):
        origin = self.node_list[dest].overallcost
        self.node_list[dest].overallcost = min(origin, self.node_list[sour].distance + self.edge_function(sour, dest) + self.heuristic_function(dest))
        if origin != self.node_list[dest].overallcost:
            self.node_list[dest].distance = self.node_list[sour].distance + self.edge_function(sour, dest)
            self.MIN_heap.maintenance(self.node_list[dest].heap_idx)
            self.node_list[dest].parent = sour
    
    #construct MIN_heap
    def init_data_structure(self):
        for idx in range(self.vertices):
            if idx != self.source:
                self.node_list[idx] = Node(idx, math.inf, idx, math.inf)
            else:
                self.node_list[idx] = Node(idx, 0, idx, self.heuristic_function(idx))
            self.MIN_heap.push(self.node_list[idx])
        
    #generate shortest path list
    def reconstruct_shortest_path(self):
        idx = self.goal
        self.result_list.appendleft(idx)
        while self.node_list[idx].parent != None and self.node_list[idx].parent != self.source:
            idx = self.node_list[idx].parent
            self.result_list.appendleft(idx)
        if self.node_list[idx].parent != None:
            self.result_list.appendleft(self.source)
        
    def compute_shortest_path(self):
        while self.MIN_heap.is_empty() == False:
            current_node = self.MIN_heap.pop()
            self.explored_list.add(current_node.idx)
            if current_node.idx == self.goal:
                break
            for neighbor_idx in self.adjacent_list[current_node.idx]:
                if neighbor_idx not in self.explored_list:
                    self.relax_path_cost(neighbor_idx, current_node.idx)
        self.reconstruct_shortest_path()
        return list(self.result_list)
       

def shortest_path(M,start,goal):
    print("shortest path called")
    if start != goal:
        MyGraph = Graph(M, start, goal)
        MyGraph.init_data_structure()
        return MyGraph.compute_shortest_path()
    else:
        return [start]