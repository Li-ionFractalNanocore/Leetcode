from collections import defaultdict


class Solution:
    def waysToReachStair(self, k: int) -> int:
        all_states = defaultdict(int)
        all_states[1] = 1
        i = 0
        state = defaultdict(int)
        state[1] = 1
        while (1 << i) <= k + i + 1:
            back_state = defaultdict(int)
            for key, v in state.items():
                if key - 1 >= 0:
                    back_state[key - 1] += v
            for key, v in back_state.items():
                state[key] += v
            new_state = defaultdict(int)
            for key, v in state.items():
                new_state[key + (1 << i)] += v
            state = new_state
            for key, v in back_state.items():
                all_states[key] += v
            for key, v in state.items():
                all_states[key] += v
            i += 1
        for key, v in state.items():
            all_states[key-1] += v
        return all_states[k]


if __name__ == '__main__':
    solution = Solution()
    print(solution.waysToReachStair(0)) # 2
    print(solution.waysToReachStair(1)) # 4
