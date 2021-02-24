class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        adj_list = {}
        # Create adjacency list for creating graph
        for i, node in enumerate(intervals):
            overlapping_nodes = []
            for n, other_node in enumerate(intervals):
                if i != n: # ignore same node
                    if (node[0] < other_node[1] and node[0] > other_node[0])\
                        or (node[1] > other_node[0] and node[1] < other_node[1])\
                        or (node[0] <= other_node[0] and node[1] >= other_node[1]):
                        overlapping_nodes.append(n)
            adj_list[i] = overlapping_nodes
            
        count_removals = 0
        # "Traverse" graph by eliminating nodes with greatest connections until separate nodes
        # Break "ties" arbitrarily for now... (look into this later, likely works because we just count)
        # Done when adj list value lists are entirely empty
        
        # Sort adj_list by length of connections
        # Sort index of keys by same.
        
        overlaps = list(adj_list.values())
        sort_index = sorted(range(len(overlaps)), key=lambda k: len(overlaps[k]), reverse=True)
        
        print(overlaps)
        print(sort_index)
        print(all([len(overlap) > 0 for overlap in overlaps]))
        
        while not (all([len(overlap) == 0 for overlap in overlaps]) or len(overlaps) == 1):
            max_index = sorted(range(len(overlaps)), key=lambda k: len(overlaps[k]), reverse=True)[0]
            for ol in overlaps:     
                try:
                    ol.remove(max_index)
                except:
                    pass
            print("removing node: ", max_index)
            overlaps[max_index] = []
            print("overlaps is now: ", overlaps)
            count_removals += 1
        print("finished! final count: ", count_removals)
        return count_removals
