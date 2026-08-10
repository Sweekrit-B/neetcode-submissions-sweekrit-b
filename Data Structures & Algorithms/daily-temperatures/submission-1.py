class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # pattern: monotonic stack

        # [30,38,30,36,35,40,28]
        # 30 has 1 value -> 38
        # 38 has 4 values -> 30, 36, 35, 40
        # 30 has 1 value -> 36
        # 36 has 2 values -> 35, 40
        # 35 has 1 value -> 40
        # 40 has 0 values
        # 28 has 0 values

        # initial idea: work backwards
        # res = [], storage = []

        # core algo: 
            # for i, currVal in temperatures:
                # while currVal > storage[-1][0]:
                    # storage.pop()
                # if storage:
                    # res.append(storage[-1][1] - i)
                # else:
                    # res.append(0)
                # storage.append((currVal, i))
        
        # initialize: res = [0], storage = [(28, 6)]
        # adding (40, 5)
            # clear -> storage = []
            # add 0 to res -> [0, 0]
            # add currVal to storage -> storage = [(40, 5)]
        # adding (35, 4)
            # clear -> storage = [(40, 5)]
            # add 1 to res -> [1, 0, 0]
            # add currVal to storage -> storage = [(40, 5), (35, 4)]
        # adding (36, 3)
            # clear -> storage = [(40, 5)]
            # add 2 to res -> [2, 1, 0, 0]
            # add currVal to storage -> storage = [(40, 5), (36, 3)]
        # adding (30, 2)
            # clear -> storage = [(40, 5), (36, 3)]
            # add 1 to res -> [1, 2, 1, 0, 0]
            # add currVal to storage -> storage = [(40, 5), (36, 3), (30, 2)]
        # adding (38, 1)
            # clear -> storage = [(40, 5)]
            # add 4 to res -> [4, 1, 2, 1, 0, 0]
            # add currVal to storage -> storage = [(40, 5), (38, 1)]
        # adding (30, 0)
            # clear -> storage = [(40, 5), (38, 1)]
            # add 1 to res -> [1, 4, 1, 2, 1, 0, 0]
            # add currVal to storage -> storage = [(40, 5), (38, 1), (30, 0)]

        res = [0] * len(temperatures)
        storage = []

        for i in range(len(temperatures)-1, -1, -1):
            currVal = temperatures[i]
            while storage and currVal >= storage[-1][0]:
                storage.pop()

            if storage:
                res[i] = storage[-1][1] - i
            else:
                res[i] = 0

            storage.append((currVal, i))
            # print(f"Results: {res}, storage: {storage}")

        return res