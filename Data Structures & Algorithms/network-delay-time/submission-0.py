class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency_list = defaultdict(list)
        edge_weights = defaultdict(int)

        for time in times:
            u, v, t = time
            adjacency_list[u].append(v)
            edge_weights[(u, v)] = t
        
        print(adjacency_list)
        print(edge_weights)

        # djikstra's algorithm
        distance_to_node = [float('inf')] * (n+1)
        priority_queue = []
        heapq.heappush(priority_queue, (0, k))
        distance_to_node[k] = 0

        while priority_queue:
            curr_distance, curr_node = heapq.heappop(priority_queue)
            # if we are not looking at the current smallest value, skip
            if curr_distance > distance_to_node[curr_node]:
                continue
            # for each adjacent itme, update
            for neighbor in adjacency_list[curr_node]:
                if (distance_to_node[curr_node] + edge_weights[(curr_node, neighbor)]) < distance_to_node[neighbor]:
                    distance_to_node[neighbor] = distance_to_node[curr_node] + edge_weights[(curr_node, neighbor)]
                    heapq.heappush(priority_queue, (distance_to_node[neighbor], neighbor))
        
        distance_to_node = distance_to_node[1:]
        return -1 if max(distance_to_node) == float('inf') else max(distance_to_node)