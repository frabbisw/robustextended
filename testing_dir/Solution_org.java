import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
     */
    public int countUpper(String value) {
        int count = 0;
        int i = 0;
        int j = value.length() - 1;
        while (i <= j) {
            if (value.charAt(i) == '9' && value.charAt(j) == '9') {
                count++;
                i++;
                j--;
            } else if (value.charAt(i) == '9') {
                i++;
            } else if (value.charAt(j) == '9') {
                j--;
            } else if (value.charAt(i) < value.charAt(j)) {
                i++;
            } else {
                j--;
            }
        }
        return count;
    }
}