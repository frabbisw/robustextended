import java.util.*;
import java.lang.*;

class SolutionGenerated {
    /**
    In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange(Arrays.asList(1, 2, 3, 4), Arrays.asList(1, 2, 3, 4)) => "YES"
    exchange(Arrays.asList(1, 2, 3, 4), Arrays.asList(1, 5, 3, 4)) => "NO"
    It is assumed that the input lists will be non-empty.
     */
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        int oddCount1 = 0;
        int oddCount2 = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                oddCount1++;
            }
        }
        for (int num : lst2) {
            if (num % 2 != 0) {
                oddCount2++;
            }
        }
        if (oddCount1 <= oddCount2) {
            return "YES";
        } else {
            return "NO";
        }
    }
}