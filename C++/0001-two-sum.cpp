#include<math.h>

class Solution {
public:
    int arrangeCoins(long long n) {
        return long(sqrt(2 * n + 0.25) -0.5);
    }
};
