
#include <bits/stdc++.h>
using namespace std;

int minSwaps(vector<int>& nums, vector<int>& forbidden) {
    int n = nums.size();
    vector<int> bad;

    // Step 1: collect bad indices
    for (int i = 0; i < n; i++) {
        if (nums[i] == forbidden[i]) {
            bad.push_back(i);
        }
    }

    int B = bad.size();
    if (B == 0) return 0;

    vector<bool> used(B, false);
    int pairs = 0;

    // Step 2: greedy pairing of bad indices
    for (int i = 0; i < B; i++) {
        if (used[i]) continue;

        for (int j = i + 1; j < B; j++) {
            if (used[j]) continue;

            int x = bad[i], y = bad[j];

            if (nums[x] != forbidden[y] &&
                nums[y] != forbidden[x]) {
                used[i] = used[j] = true;
                pairs++;
                break;
            }
        }
    }

    // Step 3: remaining bad indices must use good indices
    int remaining = B - 2 * pairs;

    // Count good indices
    int good = n - B;

    if (remaining > 0 && good == 0) return -1;

    return pairs + remaining;
}
