/*package Java;

import java.util.*;

class original {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        int res = Solution.countPrimes(n);
        System.out.println(res);
    }
}
*/
class Solution {
    public static int countPrimes(int n) {
        boolean[] seen = new boolean[n];
        int ans = 0;
        for (int num = 2; num < n; num++) {
            if (seen[num])
                continue;
            ans += 1;
            for (long mult = (long) num * num; mult < n; mult += num)
                seen[(int) mult] = true;
            // System.out.printf("%d %d\n", num, ans);
        }
        return (ans);
    }
}