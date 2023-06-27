import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.Map;
import java.util.Random;
import java.util.HashMap;
import java.util.Optional;
import java.security.NoSuchAlgorithmException;
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                s.count_upper("10") == 10,
                s.count_upper("14.5") == 15,
                s.count_upper("-15.5") == -16,
                s.count_upper("15.3") == 15,
                s.count_upper("0") == 0
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}