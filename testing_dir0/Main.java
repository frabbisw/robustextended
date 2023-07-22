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
	public static <K, V> Map<K, V> createMap(List<K> keys, List<V> values) {
        if (keys.size() != values.size()) {
            throw new IllegalArgumentException("The sizes of the input lists must be the same.");
        }

        Map<K, V> map = new HashMap<>();
        for (int i = 0; i < keys.size(); i++) {
            K key = keys.get(i);
            V value = values.get(i);
            map.put(key, value);
        }
        return map;
    }
	public static void test0()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.isEqualToSumEven(20) == s2.isEqualToSumEven(20),
			s.isEqualToSumEven(22) == s2.isEqualToSumEven(22),
			s.isEqualToSumEven(24) == s2.isEqualToSumEven(24),
			s.isEqualToSumEven(30) == s2.isEqualToSumEven(30),
			s.isEqualToSumEven(36) == s2.isEqualToSumEven(36),
			s.isEqualToSumEven(40) == s2.isEqualToSumEven(40),
			s.isEqualToSumEven(42) == s2.isEqualToSumEven(42),
			s.isEqualToSumEven(48) == s2.isEqualToSumEven(48),
			s.isEqualToSumEven(50) == s2.isEqualToSumEven(50),
			s.isEqualToSumEven(28) == s2.isEqualToSumEven(28),
			s.isEqualToSumEven(41) == s2.isEqualToSumEven(41),
			s.isEqualToSumEven(21) == s2.isEqualToSumEven(21),
			s.isEqualToSumEven(39) == s2.isEqualToSumEven(39),
			s.isEqualToSumEven(23) == s2.isEqualToSumEven(23),
			s.isEqualToSumEven(25) == s2.isEqualToSumEven(25),
			s.isEqualToSumEven(35) == s2.isEqualToSumEven(35),
			s.isEqualToSumEven(19) == s2.isEqualToSumEven(19),
			s.isEqualToSumEven(49) == s2.isEqualToSumEven(49),
			s.isEqualToSumEven(51) == s2.isEqualToSumEven(51),
			s.isEqualToSumEven(52) == s2.isEqualToSumEven(52),
			s.isEqualToSumEven(47) == s2.isEqualToSumEven(47),
			s.isEqualToSumEven(37) == s2.isEqualToSumEven(37),
			s.isEqualToSumEven(34) == s2.isEqualToSumEven(34),
			s.isEqualToSumEven(-79) == s2.isEqualToSumEven(-79),
			s.isEqualToSumEven(29) == s2.isEqualToSumEven(29),
			s.isEqualToSumEven(53) == s2.isEqualToSumEven(53),
			s.isEqualToSumEven(57) == s2.isEqualToSumEven(57),
			s.isEqualToSumEven(56) == s2.isEqualToSumEven(56),
			s.isEqualToSumEven(-2) == s2.isEqualToSumEven(-2),
			s.isEqualToSumEven(0) == s2.isEqualToSumEven(0),
			s.isEqualToSumEven(2) == s2.isEqualToSumEven(2),
			s.isEqualToSumEven(5) == s2.isEqualToSumEven(5),
			s.isEqualToSumEven(9) == s2.isEqualToSumEven(9),
			s.isEqualToSumEven(15) == s2.isEqualToSumEven(15),
			s.isEqualToSumEven(27) == s2.isEqualToSumEven(27),
			s.isEqualToSumEven(100) == s2.isEqualToSumEven(100),
			s.isEqualToSumEven(105) == s2.isEqualToSumEven(105),
			s.isEqualToSumEven(8) == s2.isEqualToSumEven(8),
			s.isEqualToSumEven(-3) == s2.isEqualToSumEven(-3),
			s.isEqualToSumEven(76) == s2.isEqualToSumEven(76),
			s.isEqualToSumEven(101) == s2.isEqualToSumEven(101),
			s.isEqualToSumEven(98) == s2.isEqualToSumEven(98),
			s.isEqualToSumEven(3) == s2.isEqualToSumEven(3),
			s.isEqualToSumEven(97) == s2.isEqualToSumEven(97),
			s.isEqualToSumEven(7) == s2.isEqualToSumEven(7),
			s.isEqualToSumEven(1) == s2.isEqualToSumEven(1),
			s.isEqualToSumEven(6) == s2.isEqualToSumEven(6),
			s.isEqualToSumEven(99) == s2.isEqualToSumEven(99),
			s.isEqualToSumEven(-50) == s2.isEqualToSumEven(-50),
			s.isEqualToSumEven(102) == s2.isEqualToSumEven(102)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test1()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.isEqualToSumEven(-71) == s2.isEqualToSumEven(-71),
			s.isEqualToSumEven(-1) == s2.isEqualToSumEven(-1),
			s.isEqualToSumEven(-72) == s2.isEqualToSumEven(-72),
			s.isEqualToSumEven(-27) == s2.isEqualToSumEven(-27),
			s.isEqualToSumEven(104) == s2.isEqualToSumEven(104),
			s.isEqualToSumEven(96) == s2.isEqualToSumEven(96),
			s.isEqualToSumEven(10) == s2.isEqualToSumEven(10),
			s.isEqualToSumEven(-26) == s2.isEqualToSumEven(-26),
			s.isEqualToSumEven(-39) == s2.isEqualToSumEven(-39),
			s.isEqualToSumEven(-55) == s2.isEqualToSumEven(-55),
			s.isEqualToSumEven(-29) == s2.isEqualToSumEven(-29),
			s.isEqualToSumEven(-66) == s2.isEqualToSumEven(-66),
			s.isEqualToSumEven(11) == s2.isEqualToSumEven(11),
			s.isEqualToSumEven(14) == s2.isEqualToSumEven(14),
			s.isEqualToSumEven(-42) == s2.isEqualToSumEven(-42),
			s.isEqualToSumEven(4) == s2.isEqualToSumEven(4),
			s.isEqualToSumEven(77) == s2.isEqualToSumEven(77),
			s.isEqualToSumEven(-38) == s2.isEqualToSumEven(-38),
			s.isEqualToSumEven(-30) == s2.isEqualToSumEven(-30),
			s.isEqualToSumEven(-25) == s2.isEqualToSumEven(-25),
			s.isEqualToSumEven(-34) == s2.isEqualToSumEven(-34),
			s.isEqualToSumEven(78) == s2.isEqualToSumEven(78),
			s.isEqualToSumEven(103) == s2.isEqualToSumEven(103),
			s.isEqualToSumEven(-65) == s2.isEqualToSumEven(-65),
			s.isEqualToSumEven(-49) == s2.isEqualToSumEven(-49),
			s.isEqualToSumEven(-18) == s2.isEqualToSumEven(-18),
			s.isEqualToSumEven(-7) == s2.isEqualToSumEven(-7),
			s.isEqualToSumEven(75) == s2.isEqualToSumEven(75),
			s.isEqualToSumEven(-37) == s2.isEqualToSumEven(-37),
			s.isEqualToSumEven(-73) == s2.isEqualToSumEven(-73),
			s.isEqualToSumEven(-51) == s2.isEqualToSumEven(-51),
			s.isEqualToSumEven(106) == s2.isEqualToSumEven(106),
			s.isEqualToSumEven(64) == s2.isEqualToSumEven(64),
			s.isEqualToSumEven(-52) == s2.isEqualToSumEven(-52),
			s.isEqualToSumEven(-8) == s2.isEqualToSumEven(-8),
			s.isEqualToSumEven(-6) == s2.isEqualToSumEven(-6),
			s.isEqualToSumEven(-10) == s2.isEqualToSumEven(-10),
			s.isEqualToSumEven(16) == s2.isEqualToSumEven(16),
			s.isEqualToSumEven(12) == s2.isEqualToSumEven(12),
			s.isEqualToSumEven(107) == s2.isEqualToSumEven(107),
			s.isEqualToSumEven(26) == s2.isEqualToSumEven(26),
			s.isEqualToSumEven(18) == s2.isEqualToSumEven(18),
			s.isEqualToSumEven(108) == s2.isEqualToSumEven(108),
			s.isEqualToSumEven(109) == s2.isEqualToSumEven(109),
			s.isEqualToSumEven(17) == s2.isEqualToSumEven(17),
			s.isEqualToSumEven(110) == s2.isEqualToSumEven(110),
			s.isEqualToSumEven(31) == s2.isEqualToSumEven(31),
			s.isEqualToSumEven(-98) == s2.isEqualToSumEven(-98),
			s.isEqualToSumEven(-87) == s2.isEqualToSumEven(-87),
			s.isEqualToSumEven(-5) == s2.isEqualToSumEven(-5)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test2()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.isEqualToSumEven(-40) == s2.isEqualToSumEven(-40),
			s.isEqualToSumEven(-88) == s2.isEqualToSumEven(-88),
			s.isEqualToSumEven(-4) == s2.isEqualToSumEven(-4),
			s.isEqualToSumEven(55) == s2.isEqualToSumEven(55),
			s.isEqualToSumEven(-86) == s2.isEqualToSumEven(-86),
			s.isEqualToSumEven(13) == s2.isEqualToSumEven(13),
			s.isEqualToSumEven(32) == s2.isEqualToSumEven(32),
			s.isEqualToSumEven(54) == s2.isEqualToSumEven(54),
			s.isEqualToSumEven(-68) == s2.isEqualToSumEven(-68),
			s.isEqualToSumEven(-90) == s2.isEqualToSumEven(-90),
			s.isEqualToSumEven(-91) == s2.isEqualToSumEven(-91),
			s.isEqualToSumEven(-78) == s2.isEqualToSumEven(-78),
			s.isEqualToSumEven(-80) == s2.isEqualToSumEven(-80)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void main(String[] args) throws NoSuchAlgorithmException {
		test0();
		test1();
		test2();
	}
}
