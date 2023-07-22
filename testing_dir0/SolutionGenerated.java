import java.util.*;
import java.lang.*;

class SolutionGenerated {
    /**
    Evaluate whether the gives number n can is written as the sums of exactly 4 positive even numbers
    Example
    isEqualToSumEven(4) == false
    isEqualToSumEven(6) == false
    isEqualToSumEven(8) == true
     */
    public boolean isEqualToSumEven(int n) {
        if (n == 0) return true;
        if (n == 1) return false;
        if (n % 2 == 0) return false;
        if (n % 3 == 0) return false;
        if (n % 4 == 0) return false;
        
        int sum = 0;
        
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        
        if (sum == 4) {
            return true;
        }
        
        return false;
    }
}
