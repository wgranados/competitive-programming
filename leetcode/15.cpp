#include <algorithm>
#include <chrono>
#include <cstdio>
#include <random>
#include <set>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> triplets;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int compliment = -(nums[i] + nums[j]);
                // only search to the right of j so i and j can't be reused
                auto it = lower_bound(nums.begin() + j + 1, nums.end(), compliment);
                if (it != nums.end() && *it == compliment) {
                    // nums is sorted and i < j < k, so the triplet is already in order
                    triplets.insert({nums[i], nums[j], *it});
                }
            }
        }
        return vector<vector<int>>(triplets.begin(), triplets.end());
    }
};

// order of triplets and of values within a triplet does not matter
vector<vector<int>> normalize(vector<vector<int>> triplets) {
    for (auto& t : triplets) sort(t.begin(), t.end());
    sort(triplets.begin(), triplets.end());
    return triplets;
}

void print(const vector<vector<int>>& triplets) {
    printf("[");
    for (size_t i = 0; i < triplets.size(); i++) {
        auto& t = triplets[i];
        printf("%s[%d,%d,%d]", i ? "," : "", t[0], t[1], t[2]);
    }
    printf("]");
}

int main() {
    Solution s;
    vector<pair<vector<int>, vector<vector<int>>>> testcases = {
        {{-1, 0, 1, 2, -1, -4}, {{-1, -1, 2}, {-1, 0, 1}}},
        {{0, 1, 1}, {}},
        {{0, 0, 0}, {{0, 0, 0}}},
    };
    for (size_t i = 0; i < testcases.size(); i++) {
        auto [nums, want] = testcases[i];
        auto got = s.threeSum(nums);
        if (normalize(got) != normalize(want)) {
            printf("Test %zu: got != want, ", i);
            print(got);
            printf(" != ");
            print(want);
            printf("\n");
        } else {
            printf("Test %zu: passed\n", i);
        }
    }

    // timing on max-size inputs (n = 3000)
    mt19937 rng(1);
    uniform_int_distribution<int> dist(-100000, 100000);
    vector<int> random_nums(3000);
    for (auto& x : random_nums) x = dist(rng);
    vector<pair<const char*, vector<int>>> big_inputs = {
        {"random", random_nums},
        {"all zeros", vector<int>(3000, 0)},
    };
    for (auto& [name, nums] : big_inputs) {
        auto start = chrono::steady_clock::now();
        s.threeSum(nums);
        chrono::duration<double> elapsed = chrono::steady_clock::now() - start;
        printf("threeSum on %s: %.3fs\n", name, elapsed.count());
    }
}
