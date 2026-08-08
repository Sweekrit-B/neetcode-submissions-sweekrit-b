class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            if gas[0] >= cost[0]:
                return 0
            return -1

        net_cost = [gas[i] - cost[i] for i in range(len(gas))]
        # print(net_cost)
        # find index such that
            # after index i, net cost is never less than 0
        all_pos = [(nc, i) for i, nc in enumerate(net_cost) if nc > 0]
        # print(all_pos)

        def check_remaining(pos):
            # print(f"Starting check at {pos}")
            i = pos[1]
            net = pos[0]
            # print(f"Starting net: {net}")
            t = 1
            while t < len(net_cost):
                i += 1
                i %= len(net_cost)
                # print(f"Checking new value at {(net_cost[i], i)}")
                net += net_cost[i]
                # print(f"New net: {net}")
                if net < 0:
                    # print(f"Was not able to keep the net higher than 0: {net}")
                    return False
                t += 1
            return True

        for pos in all_pos:
            if check_remaining(pos):
                return pos[1]
        
        return -1

