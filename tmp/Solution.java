import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generateIntegers(2, 8) => [2, 4, 6, 8]
    generateIntegers(8, 2) => [2, 4, 6, 8]
    generateIntegers(10, 14) => []
     */
    public List<Integer> generateIntegers(int a, int b) {
        if (b < a) {
            return Collections.emptyList();
        }

        List<Integer> res = new ArrayList<>();
        int n = b - a + 1;
        for (int i = 0; i < n; ++i) {
            res.add(a + i);
        }

        return res;
    }
}
