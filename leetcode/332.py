from collections import defaultdict, deque

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj = defaultdict(list)
        tickets = sorted(tickets, reverse=True)
        for ticket in tickets:
            start, end = ticket[0], ticket[1]
            adj[start].append(end)
        # Hierholzer's algorithm for eulerian circuit
        itinarary = []
        def dfs(airport):
            while adj[airport]:
                next_airport = adj[airport].pop()
                dfs(next_airport)
            itinarary.append(airport)
        dfs("JFK")
        return itinarary[::-1]


if __name__ == '__main__':
    testcases = [
        ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
         ["JFK", "MUC", "LHR", "SFO", "SJC"]),
        ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
         ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
        # single ticket
        ([["JFK", "LGA"]], ["JFK", "LGA"]),
        # greedy smallest (KUL) is a dead end, must take NRT first
        ([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
         ["JFK", "NRT", "JFK", "KUL"]),
        # duplicate tickets must each be used
        ([["JFK", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"], ["ATL", "JFK"]],
         ["JFK", "ATL", "JFK", "ATL", "JFK"]),
        ([["JFK", "AAA"], ["AAA", "JFK"], ["JFK", "BBB"], ["BBB", "JFK"], ["JFK", "CCC"]],
         ["JFK", "AAA", "JFK", "BBB", "JFK", "CCC"]),
        ([["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"],
          ["TIA", "ANU"], ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]],
         ["JFK", "ANU", "EZE", "AXA", "TIA", "ANU", "JFK", "TIA", "ANU", "TIA", "JFK"]),
        # cycle that doesn't return to JFK
        ([["JFK", "AAA"], ["AAA", "BBB"], ["BBB", "AAA"], ["AAA", "JFK"]],
         ["JFK", "AAA", "BBB", "AAA", "JFK"]),
        # taking AAA first strands the BBB round trip
        ([["JFK", "BBB"], ["BBB", "JFK"], ["JFK", "AAA"], ["AAA", "CCC"], ["CCC", "AAA"]],
         ["JFK", "BBB", "JFK", "AAA", "CCC", "AAA"]),
    ]
    for i, (tickets, want) in enumerate(testcases):
        s = Solution()
        got = s.findItinerary([list(t) for t in tickets])
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
