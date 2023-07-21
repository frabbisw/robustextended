import java.util.*;
import java.lang.*;

class SolutionGenerated {
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
        if (value == null || value.length() == 0) {
            return 0;
        }
        int[] nums = value.split("\\.");
        int lower = Integer.parseInt(nums[0]);
        int upper = Integer.parseInt(nums[1]);
        int count = 0;
        for (int i = lower; i <= upper; i++) {
            if (i == lower) {
                count++;
            } else if (i == upper) {
                count++;
            }
        }
        return count;
    }
}
