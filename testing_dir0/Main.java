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
			s.willItFly(new ArrayList<>(Arrays.asList(0)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(0)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 4)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 4)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 4)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 4)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 4, 4)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 4, 4)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 0)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 0)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 0)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 0)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(7, 2, 3)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(7, 2, 3)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 10, 1)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 10, 1)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 1, 2, 3)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 1, 2, 3)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 4, 4)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 4, 4)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(1)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 1, 1)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 1, 1)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(3, 2, 1, 2, 4)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(3, 2, 1, 2, 4)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(1)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(1)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 10, 1)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 10, 1)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(6)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(6)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 13, 1, 0)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 13, 1, 0)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1, 1, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1, 1, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 0, 1)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 0, 1)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList()), 0) == s2.willItFly(new ArrayList<>(Arrays.asList()), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 13)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 13)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 1, 2, 4, 4)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 1, 2, 4, 4)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(3, 2, 1, 2, 4)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(3, 2, 1, 2, 4)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(3, 2, 1, 2, 4)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(3, 2, 1, 2, 4)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(-15, 13, 83, 8)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(-15, 13, 83, 8)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1, 1, 2, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1, 1, 2, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 8, 4)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 8, 4)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(1)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 13)), 83) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 13)), 83),
			s.willItFly(new ArrayList<>(Arrays.asList(1, -1, 0)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, -1, 0)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 1)), 83) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 1)), 83)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test1()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 13, 1)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 13, 1)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(3, 1, 2, 1, 2, 4)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(3, 1, 2, 1, 2, 4)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 8, 4, 1)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 8, 4, 1)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 1, 2, 3)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 1, 2, 3)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 13, 1, 0)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 13, 1, 0)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList()), 2) == s2.willItFly(new ArrayList<>(Arrays.asList()), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(3)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(3)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(13, 83, 8)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(13, 83, 8)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 2)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 2)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 13, 1, 0)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 13, 1, 0)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(2)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(2)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(0)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(0)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(13, 2, 1)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(13, 2, 1)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 10, 1, 1)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 10, 1, 1)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(48, -3, -48)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(48, -3, -48)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 1, 2, 8, 4)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 1, 2, 8, 4)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(13, 1)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(13, 1)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(48, -48, -3, -48)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(48, -48, -3, -48)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 0, 0)), -15) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 0, 0)), -15),
			s.willItFly(new ArrayList<>(Arrays.asList(1)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 1, 2, 3)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 1, 2, 3)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 10, 1, 1)), 83) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 10, 1, 1)), 83),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(12, 13, 83, 8)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(12, 13, 83, 8)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(7, 2, 2)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(7, 2, 2)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 4, 4)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 1, 2, 4, 4)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(3, 1, 2, 1, 2, 4, 2)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(3, 1, 2, 1, 2, 4, 2)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(13, 83, 8)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(13, 83, 8)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 1, 13, 1, 0)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 1, 13, 1, 0)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(3)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(3)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 13, 13)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 13, 13)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 1)), 82) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 1)), 82),
			s.willItFly(new ArrayList<>(Arrays.asList(6)), -15) == s2.willItFly(new ArrayList<>(Arrays.asList(6)), -15),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 13, 1, 0)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 13, 1, 0)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1, 1, 1, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1, 1, 1, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 0)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 0)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(7, 2)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(7, 2)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 1, 2, 3)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 1, 2, 3)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2)), -2) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2)), -2),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1)), 7)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test2()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(7)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(7)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 18, 20, 12)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 18, 20, 12)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 6, 1)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 6, 1)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 6, 1, 2)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 6, 1, 2)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 2)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 2)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 0)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 0)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 2, 3, 4, 5, 6)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 2, 3, 4, 5, 6)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 3, 2, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 3, 2, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 0, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 0, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 1, 5, 7, 9, 7, 5, 3, 1, 5)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 1, 5, 7, 9, 7, 5, 3, 1, 5)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 2)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 2)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 2, 3, 2, 1, 0, 2)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 2, 3, 2, 1, 0, 2)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 17, 20, 12)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 17, 20, 12)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 0)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 0)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 7)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 7)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 3)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 3)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 5, 6)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 5, 6)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 0, 2, 2)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 0, 2, 2)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1, 5)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1, 5)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 1)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test3()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 0)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 0)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 17, 20, 12)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 17, 20, 12)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 1, 0)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 1, 0)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 0)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 0)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 4)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 4)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 7, 2, 3, 4, 5, 6)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 7, 2, 3, 4, 5, 6)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0, 1)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0, 1)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 14, 2, 3, 4, 4, 5)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 14, 2, 3, 4, 4, 5)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(7, 7)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(7, 7)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 1, 1, 1)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 1, 1, 1)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 0)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 0)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 1, 3, 2, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 1, 3, 2, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 16, 18, 20)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 16, 18, 20)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 17) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 17),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 1, 14, 3, 2, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 1, 14, 3, 2, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 7, 2, 3, 4, 5, 6)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 7, 2, 3, 4, 5, 6)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 0)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 0)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 2, 16)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 2, 16)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 1, 4, 2, 5, 1, 3, 2, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 1, 4, 2, 5, 1, 3, 2, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 1)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 1)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 16, 18, 20)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 16, 18, 20)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 2, 3, 5, 6)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 2, 3, 5, 6)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 5)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 5)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 1, 2, 5, 1, 3, 2, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 1, 2, 5, 1, 3, 2, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 1, 2, 1, 0, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 1, 2, 1, 0, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 7, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 7, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 1, 2, 3, 2, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 1, 2, 3, 2, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1, 1)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1, 1)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 0, 2, 2)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 0, 2, 2)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6, 5)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6, 5)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 7, 2, 1, 0, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 7, 2, 1, 0, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 0, 1, 1)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 0, 1, 1)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(3, 3, 3, 2, 1, 0, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(3, 3, 3, 2, 1, 0, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 3, 2, 1, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 3, 2, 1, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 0, 2)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 0, 2)), 8)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test4()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 30, 3, 2, 1, 0, 2)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 30, 3, 2, 1, 0, 2)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 5)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 5)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 12, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 12, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 16) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 16),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 6)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 6)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 6, 8, 10, 16, 18, 31, 20)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 6, 8, 10, 16, 18, 31, 20)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0, 1)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0, 1)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 12, 1, 1, 1, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 12, 1, 1, 1, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 1, 2, 5, 1, 31, 3, 2, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 1, 2, 5, 1, 31, 3, 2, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 2, 1, 0, 2)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 2, 1, 0, 2)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 1, 0)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 1, 0)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 14, 2, 4, 4, 5)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 14, 2, 4, 4, 5)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 3)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 3)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 2, 16)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 2, 16)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 3, 1, 5)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 3, 1, 5)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 30, 3, 1, 5, 7, 9, 7, 5, 3, 1, 5)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 30, 3, 1, 5, 7, 9, 7, 5, 3, 1, 5)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 0)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 0)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 6, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 6, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 18, 20, 12, 6)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 18, 20, 12, 6)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 7, 2, 1, 0, 1)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 7, 2, 1, 0, 1)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 5, 0)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 5, 0)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 16, 18, 20)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 16, 18, 20)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 3, 2, 1, 1, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 3, 2, 1, 1, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 31, 3, 3, 2, 2, 1, 1, 1)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 31, 3, 3, 2, 2, 1, 1, 1)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 3, 1, 5)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 3, 1, 5)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6, 5, 5)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6, 5, 5)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(7, 2, 4, 5, 5)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(7, 2, 4, 5, 5)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 3, 2, 0, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 3, 2, 0, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 0, 2)), 17) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 0, 2)), 17),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 14, 17, 17, 20, 12)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 14, 17, 17, 20, 12)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 1)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 1)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 11, 17, 17, 20, 12)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 11, 17, 17, 20, 12)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 1, 4, 2, 5, 1, 3, 2, 1, 1)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 1, 4, 2, 5, 1, 3, 2, 1, 1)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 1, 5)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 1, 5)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 2, 3, 2, 1, 0, 1, 1, 1)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 2, 3, 2, 1, 0, 1, 1, 1)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 17, 20, 12)), 11) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 17, 20, 12)), 11)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test5()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 2, 3, 4, 5, 6)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 2, 3, 4, 5, 6)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 17) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 17),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 11, 4, 5, 6)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 11, 4, 5, 6)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 1)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 1)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList()), 6) == s2.willItFly(new ArrayList<>(Arrays.asList()), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 3, 1)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 3, 1)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 3)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 3)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 18, 3)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 18, 3)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 10, 3, 1, 2, 1, 0, 1)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 10, 3, 1, 2, 1, 0, 1)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 4, 5)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 4, 5)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 1, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 1, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 0)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 0)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 30, 3, 5, 7, 9, 7, 5, 3, 1, 5)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 30, 3, 5, 7, 9, 7, 5, 3, 1, 5)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 10, 7, 5, 3, 1, 5)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 10, 7, 5, 3, 1, 5)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 0)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 0)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 18, 4, 1, 0)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 18, 4, 1, 0)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 0)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 0)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 31, 3, 3, 2, 2, 1, 1, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 31, 3, 3, 2, 2, 1, 1, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 1, 0, 1, 1)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 1, 0, 1, 1)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 4, 5, 6)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 4, 5, 6)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 3, 4, 5, 7)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 3, 4, 5, 7)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1, 0, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1, 0, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 14, 17, 17, 20, 12, 10)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 14, 17, 17, 20, 12, 10)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 4)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 4)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 3)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 3)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 42) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 42),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 8, 10, 12, 14, 16, 18, 21)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 8, 10, 12, 14, 16, 18, 21)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 11, 4, 5, 6)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 11, 4, 5, 6)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 21, 3)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 21, 3)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, -1, 4, 5, 0)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, -1, 4, 5, 0)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 4, 5, 6)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 4, 5, 6)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 31, 1, -1, 0)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 31, 1, -1, 0)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 8, 2, 1, 0, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 8, 2, 1, 0, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 4, 5, 3)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 4, 5, 3)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 4)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 4)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0, 1, 2)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0, 1, 2)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 1, 0)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 1, 0)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 5, 6)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 5, 6)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1, 4)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1, 4)), 2)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test6()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 30, 1, 3, 2, 3, 2, 1, 7, 2, 2)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 30, 1, 3, 2, 3, 2, 1, 7, 2, 2)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 0, 0)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 0, 0)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 0)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 0)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 1)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 1)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 14, 2, 4, 5)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 14, 2, 4, 5)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 3, 2, 0, 1)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 3, 2, 0, 1)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 4, 6, 5)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 4, 6, 5)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 1, 9, 2, 5, 1, 3, 2, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 1, 9, 2, 5, 1, 3, 2, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 2, 2, 3, 2, 2, 2)), 17) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 2, 2, 3, 2, 2, 2)), 17),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 14, 2, 3, 4, 4, 5)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 14, 2, 3, 4, 4, 5)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 11, 6, 8, 10, 12, 14, 17, 18, 20, 12, 6)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 11, 6, 8, 10, 12, 14, 17, 18, 20, 12, 6)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 1, 1, 1, 1)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 1, 1, 1, 1)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 5, 1, 2, 0, 4, 5, 6)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 5, 1, 2, 0, 4, 5, 6)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 3, 5, 6, 5)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 3, 5, 6, 5)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 0, 2)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 0, 2)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 3)), 16) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 3)), 16),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 16) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 16),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 11, 17, 17, 20, 12)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 11, 17, 17, 20, 12)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 3, 2, 1, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 3, 2, 1, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 6)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 6)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 2, 16)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 2, 16)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 2, 3, 1, 0, 1, 1)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 2, 3, 1, 0, 1, 1)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 0, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 0, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0, 1, 2)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0, 1, 2)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 9, 3, 2, 1, 0, 9, 1)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 9, 3, 2, 1, 0, 9, 1)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 2, 2, 3)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 2, 2, 3)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 2)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 2)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, -1, 4, 5, 0)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, -1, 4, 5, 0)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 4, 5, 3, 3)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 4, 5, 3, 3)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 3)), 16) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 3)), 16),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 1)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 1)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 4)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 4)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(7)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(7)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 21, 5, 6, 4)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 21, 5, 6, 4)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 14, 17, 17, 20, 12, 8)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 14, 17, 17, 20, 12, 8)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 1, 0, 4)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 1, 0, 4)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 5, 0)), 15) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 5, 0)), 15),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, -1, 2, 1, 2, 0, 1)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, -1, 2, 1, 2, 0, 1)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 1, 16)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 1, 16)), 31)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test7()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 20, 2, 3, 2, 2, 3, 3)), 16) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 20, 2, 3, 2, 2, 3, 3)), 16),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 12, 1, 1, 1, 1)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 12, 1, 1, 1, 1)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 30, 1, 3, 2, 3, 4, 2, 1, 7, 2, 2)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 30, 1, 3, 2, 3, 4, 2, 1, 7, 2, 2)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(7)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(7)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2, 1, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2, 1, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 1, 2, 5, 1, 31, 3, 2, 1)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 1, 2, 5, 1, 31, 3, 2, 1)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 1, 15, 5, 1, 3, 2, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 1, 15, 5, 1, 3, 2, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(6, 8, 10, 16, 19, 31, 20)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(6, 8, 10, 16, 19, 31, 20)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 14)), 16) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 14)), 16),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 4, 6, 5, 3)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 4, 6, 5, 3)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 42, 3, 4)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 42, 3, 4)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 1, 2)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 1, 2)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1, 0)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1, 0)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 22)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 22)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 2, 1)), 15) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 2, 1)), 15),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 6, 3, 5, 7, 9, 7, 5, 3, 1)), 17) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 6, 3, 5, 7, 9, 7, 5, 3, 1)), 17),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 4, 5, 6)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 4, 5, 6)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 2, 1, 2, 3, 2, 1, 2, 2, 2, 3)), 15) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 2, 1, 2, 3, 2, 1, 2, 2, 2, 3)), 15),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 4, 4)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 4, 4)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12, 12)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12, 12)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(6, 8, 10, 16, 19, 31, 20, 20)), 42) == s2.willItFly(new ArrayList<>(Arrays.asList(6, 8, 10, 16, 19, 31, 20, 20)), 42),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 7, 17, 18, 20, 12, 6)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 7, 17, 18, 20, 12, 6)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 3, 3)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 3, 3)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 1, 0)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 1, 0)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 3)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 3)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 0, 2, 2)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 0, 2, 2)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 2, 1, 2, 3, 1, 2, 3, 2, 2, 3)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 2, 1, 2, 3, 1, 2, 3, 2, 2, 3)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 1, 4, 5, 6)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 1, 4, 5, 6)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 1, 2)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 1, 2)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 1, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 1, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 1)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 1)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 7, 2, 3, 4, 5, 6)), 16) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 7, 2, 3, 4, 5, 6)), 16),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 21, 7, 5, 1, 5)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 21, 7, 5, 1, 5)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 11, 2, 3, 2, 1, 7, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 11, 2, 3, 2, 1, 7, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 4, 4, 4)), 16) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 4, 4, 4)), 16),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 0, 2, 2)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 0, 2, 2)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 3, 1, 5, 5)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 3, 1, 5, 5)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 2, 1, 1, 2, 1)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 2, 1, 1, 2, 1)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(10, 2, 2, 1, 0, 2)), 17) == s2.willItFly(new ArrayList<>(Arrays.asList(10, 2, 2, 1, 0, 2)), 17),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1, 7)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1, 7)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 7, 2, 3, 4, 5, 6)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 7, 2, 3, 4, 5, 6)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(13, 2, 3, 4, 5, 3)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(13, 2, 3, 4, 5, 3)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 2, 1, 1, 2, 1, 1)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 2, 1, 1, 2, 1, 1)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 31, 1, 2, 3, 1, 0, 1, 1)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 31, 1, 2, 3, 1, 0, 1, 1)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 30, 1, 3, 2, 3, 2, 1, 7, 3, 2)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 30, 1, 3, 2, 3, 2, 1, 7, 3, 2)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 2, 1, 2, 3, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 2, 3, 2, 2, 1, 2, 3, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(3, 3, 2, 1, 1, 1)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(3, 3, 2, 1, 1, 1)), 21)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test8()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 30, 3, 1, 0, 1, 1, 1)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 30, 3, 1, 0, 1, 1, 1)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 0)), 29) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 0)), 29),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 4, 5, 6, 2)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 4, 5, 6, 2)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2, 1, 2, 3, 1, 2, 3, 2, 1)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2, 1, 2, 3, 1, 2, 3, 2, 1)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 10, 31, 3, 1, 2, 1, 0, 1)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 10, 31, 3, 1, 2, 1, 0, 1)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(7, 1, 2, 1, 0, 0)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(7, 1, 2, 1, 0, 0)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 1, 2, 3, -1, 2, 1, 2, 0, 1)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 1, 2, 3, -1, 2, 1, 2, 0, 1)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 1, 4, 5, 6)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 1, 4, 5, 6)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 0)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 0)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1, 0, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1, 0, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 5, 6)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 5, 6)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 2, 1, 1, 2, 1, 1)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 2, 1, 1, 2, 1, 1)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 7, 2, 3, 4, 5, 6)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 7, 2, 3, 4, 5, 6)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1, 3)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1, 3)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 18, 16, 7, 0)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 18, 16, 7, 0)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 4)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 4)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 15, 3, 2, 1, 0, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 15, 3, 2, 1, 0, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 5, 6, 1)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 5, 6, 1)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 17, 10, 12, 13, 17, 20, 12)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 17, 10, 12, 13, 17, 20, 12)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 2, 1, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 2, 1, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 1, 3, 3, 2, 1, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 1, 3, 3, 2, 1, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 4)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 4)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 29, 1, 2, 1, 0, 4, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 29, 1, 2, 1, 0, 4, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 5, 6)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 5, 6)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 2, 2, 3, 2, 16)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 2, 2, 3, 2, 16)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2, 2)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2, 2)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 20, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 7, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 20, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 7, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 6, 2, 1, 1, 3, 2, 2, 3, 2, 2, 3, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 6, 2, 1, 1, 3, 2, 2, 3, 2, 2, 3, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1, 3)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1, 3)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 1, 1, 1)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 1, 1, 1)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 0, 2)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 0, 2)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(13, 3, 4, 5, 3, 3)), 42) == s2.willItFly(new ArrayList<>(Arrays.asList(13, 3, 4, 5, 3, 3)), 42),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 2, 1, 2, 3, 1, 2, 3, 2, 3)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 2, 1, 2, 3, 1, 2, 3, 2, 3)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 3, 2, 2, 3, 2, 16)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 3, 2, 2, 3, 2, 16)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 3)), 29) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 3)), 29),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 13, 17, 20, 12)), 2) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 13, 17, 20, 12)), 2),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 29, 1, 2, 1, 17, 4, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 29, 1, 2, 1, 17, 4, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 3, 2, 1, 0, 9, 1)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 3, 2, 1, 0, 9, 1)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 1, 3, 3, 2, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 1, 3, 3, 2, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 0, 2, 2)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 0, 2, 2)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 0, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 0, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 16, 3, 2, 1, 2, 3, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 16, 3, 2, 1, 2, 3, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 2, 3, 2, 0, 1)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 2, 3, 2, 0, 1)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 31, 1, 2, 3, 1, 1, 1)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 31, 1, 2, 3, 1, 1, 1)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(3, 3, 2, 1, 1, 1, 1)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(3, 3, 2, 1, 1, 1, 1)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1, 4)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 2, 1, 1, 4)), 31)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test9()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 3, 2, 0, 1, 2)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 3, 2, 0, 1, 2)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(3, 3, 3, 2, 1, 0, 7)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(3, 3, 3, 2, 1, 0, 7)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 4, 4, 4)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 4, 4, 4)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 4, 5, 6)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 4, 5, 6)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 5, 6)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 5, 6)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 11, 17, 17, 20, 12)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 11, 17, 17, 20, 12)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 1, 0, 9, 1)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 1, 0, 9, 1)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 1, 2, 3, 2, 1, 2, 3, 2, 16)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 1, 2, 3, 2, 1, 2, 3, 2, 16)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(6, 8, 10, 19, 3, 31, 20)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(6, 8, 10, 19, 3, 31, 20)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(6, 16, 8, 10, 19, 3, 31, 20)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(6, 16, 8, 10, 19, 3, 31, 20)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 1, 3, 2, 1, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 1, 3, 2, 1, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 0, 2, 5, 3, 4, 5, 6)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 0, 2, 5, 3, 4, 5, 6)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 2, 1, 1, 2, 1, 1, 1)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 2, 1, 1, 2, 1, 1, 1)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(17, 3, 1, 4, 5, 6)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(17, 3, 1, 4, 5, 6)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 1, 5)), 16) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 1, 5)), 16),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 30, 5, 7, 9, 7, 5, 3, 1, 5)), 29) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 30, 5, 7, 9, 7, 5, 3, 1, 5)), 29),
			s.willItFly(new ArrayList<>(Arrays.asList(13, 3, 4, 5, 3)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(13, 3, 4, 5, 3)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 5, 2, 1)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 5, 2, 1)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 18, 20, 12)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 18, 20, 12)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 2, 3, 2, 1, 2, 2, 2, 2)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 2, 3, 2, 1, 2, 2, 2, 2)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 7, 3, 5, 7, 9, 7, 5, 3, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 7, 3, 5, 7, 9, 7, 5, 3, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(7, 2, 5, 5, 5)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(7, 2, 5, 5, 5)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 31, 3, 2, 1, 0, 1)), 18) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 31, 3, 2, 1, 0, 1)), 18),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 5, 8, 10, 12, 16, 18, 20)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 5, 8, 10, 12, 16, 18, 20)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(7)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(7)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 3, 6, 5, 1)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 3, 6, 5, 1)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 1)), 42) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 1)), 42),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 2, 3, 5, 6, 3)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 2, 3, 5, 6, 3)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(15, 3, -1, 4, 5, 0)), 13) == s2.willItFly(new ArrayList<>(Arrays.asList(15, 3, -1, 4, 5, 0)), 13),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, -1, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, -1, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 14, 3, 4, 1)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 14, 3, 4, 1)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 5, 3, 4, 5, 6)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 5, 3, 4, 5, 6)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 3, 1, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 3, 1, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 5, 4)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 5, 4)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 1, 15, 5, 1, 3, 2, 1, 0)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 1, 15, 5, 1, 3, 2, 1, 0)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1)), 29) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1)), 29),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 0, 1, 0)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 0, 1, 0)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 1, 0)), 29) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 1, 0)), 29),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6, 5)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6, 5)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 0, 2)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 0, 2)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 2, 3, 4, 5, 3)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 2, 3, 4, 5, 3)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 1)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 1)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 6)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 6)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 31, 1, 0)), 16) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 31, 1, 0)), 16),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 1, 0)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 1, 0)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 2, 2)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 2, 2)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 13, 1, 0, 1)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 13, 1, 0, 1)), 30)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test10()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 3, 1, 5, 5, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 3, 1, 5, 5, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 1, 3, 2, 1, 0)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 1, 3, 2, 1, 0)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 1, 16)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 1, 16)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 4, 5, 30)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 14, 4, 4, 5, 30)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(3, 4, 16, 6, 10, 14, 17, 17, 20, 12)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(3, 4, 16, 6, 10, 14, 17, 17, 20, 12)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 5, 7, 9, 7, 5, 3, 13, 1, 5)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 5, 7, 9, 7, 5, 3, 13, 1, 5)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 4, 6, 5, 3)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 4, 6, 5, 3)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 5, 6, 5)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 5, 6, 5)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 1, 5)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 1, 5)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 2, 4, 5, 6)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 2, 4, 5, 6)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 3, 2, 2, 3, 2, 16)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 3, 2, 2, 3, 2, 16)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 30, 1, 3, 2, 3, 2, 1, 7, 3, 2)), 18) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 30, 1, 3, 2, 3, 2, 1, 7, 3, 2)), 18),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 30, 3, 7, 9, 7, 5, 3, 1, 5)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 30, 3, 7, 9, 7, 5, 3, 1, 5)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 7, 3, 2, 1, 1, 1)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 7, 3, 2, 1, 1, 1)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(7, 1, 2, 1, 0, 0, 0)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(7, 1, 2, 1, 0, 0, 0)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 0, 2, 18)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 0, 2, 18)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 1)), 15) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1, 1)), 15),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, -1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, -1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(7, 2, 5, 5, 5, 5)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(7, 2, 5, 5, 5, 5)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 3)), 29) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 3)), 29),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 1, 1, 3, 2, 1, 0)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 1, 1, 3, 2, 1, 0)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 1)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 1)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(6, 8, 10, 16, 19, 31, 20)), 15) == s2.willItFly(new ArrayList<>(Arrays.asList(6, 8, 10, 16, 19, 31, 20)), 15),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 5, 6, 1)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 5, 6, 1)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 17) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1)), 17),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 5, 8, 10, 12, 16, 18, 20)), 15) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 5, 8, 10, 12, 16, 18, 20)), 15),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 5)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 5)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 4, 5, 6, 2)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 4, 5, 6, 2)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 0, 1)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 0, 1)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 1, 2, 5, 1, 31, 3, 2, 1, 31)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 1, 2, 5, 1, 31, 3, 2, 1, 31)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 6, 1, 2, 2)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 6, 1, 2, 2)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 6, 2, 1, 1, 3, 2, 2, 3, 2, 2, 3, 2)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 6, 2, 1, 1, 3, 2, 2, 3, 2, 2, 3, 2)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 1, 2)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 1, 2)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 15, 3, 2, 1, 0, 1)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 15, 3, 2, 1, 0, 1)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 13, 1)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 13, 1)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 1, 4, 5, 6, 2)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 1, 4, 5, 6, 2)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 7, 0)), 15) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4, 7, 0)), 15),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 3, 2, 1, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 3, 2, 1, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 19, 0)), 42) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 18, 19, 0)), 42),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 2, 2, 1, 1)), 15) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 2, 2, 1, 1)), 15),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 18, 16, 7, 0, 16)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 18, 16, 7, 0, 16)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 0, 1)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 0, 1)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 30, 3, 7, 9, 7, 5, 3, 5)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 30, 3, 7, 9, 7, 5, 3, 5)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 2, 16)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 2, 16)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 1, 3, 2, 1, 1)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 1, 3, 2, 1, 1)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 0, 2)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 0, 2)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 1, 0)), 18) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 1, 0)), 18),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 8, 10, 12, 14, 16, 18, 21, 16)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 8, 10, 12, 14, 16, 18, 21, 16)), 20)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test11()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 4, 5, 5, 3)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 4, 5, 5, 3)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 1, 1, 1)), 42) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 1, 1, 1)), 42),
			s.willItFly(new ArrayList<>(Arrays.asList(10, 2, 2, 1, 0, 2)), 11) == s2.willItFly(new ArrayList<>(Arrays.asList(10, 2, 2, 1, 0, 2)), 11),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 4, 29, 2, 1, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 3, 3, 4, 29, 2, 1, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 1, 1, 1)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 1, 1, 1)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 6, 4, 6, 8, 10, 12, 16, 18, 20)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 6, 4, 6, 8, 10, 12, 16, 18, 20)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 1, 3, 2, 5, 1, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 1, 1, 3, 2, 5, 1, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6, -1)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 5, 3, 4, 5, 6, -1)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 3)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 3, 4, 5, 3)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 15, 2, 11, 2, 1, -1)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 15, 2, 11, 2, 1, -1)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 1, 16, 3)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 1, 16, 3)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 4, 4, 5, 6)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 4, 4, 5, 6)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 7, 2, 3, 4, 5, 6)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 7, 2, 3, 4, 5, 6)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(20, 2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12, 2)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(20, 2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12, 2)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 30, 2, 1, 0, 1, 0, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 30, 2, 1, 0, 1, 0, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 1, 0)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 1, 1, 0)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 5, 6, 8, 10, 30, 14, 17, 17, 20, 12, 10)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 5, 6, 8, 10, 30, 14, 17, 17, 20, 12, 10)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 2, 0, 2, 18)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 2, 0, 2, 18)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 1, 2, 5, 1, 31, 3, 2, 1, 31, 2)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 1, 2, 5, 1, 31, 3, 2, 1, 31, 2)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 7, 2, 0, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 7, 2, 0, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 2)), 17) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 2)), 17),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1, 2, 1, 0)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 0, 1)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 0, 1)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 6, 18, 8, 10, 16, 18, 31, 20)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 6, 18, 8, 10, 16, 18, 31, 20)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 2, 3, 2, 1, -1, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 2, 3, 2, 1, -1, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 3, 1, 1, 4)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 3, 1, 1, 4)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(7, 2, 4, 5, 5, 2)), 16) == s2.willItFly(new ArrayList<>(Arrays.asList(7, 2, 4, 5, 5, 2)), 16),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 0, 1, 2)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 2, 3, 2, 0, 1, 2)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(19, 4, 8, 10, 12, 14, 16, 18, 21, 16)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(19, 4, 8, 10, 12, 14, 16, 18, 21, 16)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(6, 3, 3, 2, 1, 0, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(6, 3, 3, 2, 1, 0, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 14, 15, 4, 4, 5)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 14, 15, 4, 4, 5)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1, 3, 5)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 5, 3, 1, 3, 5)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 17, 20)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 17, 20)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 18, 12)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 17, 18, 12)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 2, 1)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1, 1, 2, 1)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 31, 1, 2, 3, 1, 0, 1, 1, 2)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 31, 1, 2, 3, 1, 0, 1, 1, 2)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 2)), 17) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 2)), 17),
			s.willItFly(new ArrayList<>(Arrays.asList(14, 2, 4, 5, 3, 3, 3)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(14, 2, 4, 5, 3, 3, 3)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 9, 1)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 6, 2, 3, 4, 5, 6, 2)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 6, 2, 3, 4, 5, 6, 2)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 1, 2)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 1, 2)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 1, 3, 2, 1, 0)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 1, 3, 2, 1, 0)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(3, 3, 3, 15, 1, 0, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(3, 3, 3, 15, 1, 0, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2, 1, 0)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2, 1, 0)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 4, 2, 5, 3, 2, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 11, 17, 17, 10, 20, 12)), 22) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 11, 17, 17, 10, 20, 12)), 22),
			s.willItFly(new ArrayList<>(Arrays.asList(7, 2, 5, 5, 5)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(7, 2, 5, 5, 5)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 17, 1, 2, 1, 16, 3, 2, 1, 2, 3, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 17, 1, 2, 1, 16, 3, 2, 1, 2, 3, 2, 2)), 20)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test12()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 15) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 1)), 15),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 5, 2, 1, 0, 2, 2, 2, 2)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 5, 2, 1, 0, 2, 2, 2, 2)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(0, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 3, 2)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(0, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 3, 2)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 9, 1, 16, 1)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 9, 1, 16, 1)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 18, 16, 7, 12, 16, 16)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 18, 16, 7, 12, 16, 16)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 31, 1, 2, 3, 1, 1, 1)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 31, 1, 2, 3, 1, 1, 1)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList()), 10) == s2.willItFly(new ArrayList<>(Arrays.asList()), 10),
			s.willItFly(new ArrayList<>(Arrays.asList()), 8) == s2.willItFly(new ArrayList<>(Arrays.asList()), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(3)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(3)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)), 100) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)), 100),
			s.willItFly(new ArrayList<>(Arrays.asList(10)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(10)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList()), 1) == s2.willItFly(new ArrayList<>(Arrays.asList()), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(2)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(2)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(2)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(2)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 5, 2)), 10) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 5, 2)), 10),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 4, 7, 9, 7, 5, 3, 1, 5)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 4, 7, 9, 7, 5, 3, 1, 5)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 2)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 2)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 3, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 3, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 0, 0)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0, 0, 0)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 18) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 18),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 3, 2, 2)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 3, 2, 2)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 1)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 0)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 10, 2, 4, 3, 2, 1, 4)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 10, 2, 4, 3, 2, 1, 4)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 2, 3)), 1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 2, 3)), 1),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 6, 8, 10, 12, 14, 16, 18, 20)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 6, 8, 10, 12, 14, 16, 18, 20)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 14, 4)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 14, 4)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 4, 3, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 4, 3, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 2, 2)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 2, 2)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 14, 3, 2, 1, 2, 3, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 14, 3, 2, 1, 2, 3, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 4)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 4)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 4)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 2, 3, 4, 4)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 2, 3, 4, 4)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1, 0)), 8) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 3, 2, 1, 0)), 8),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 3, 2, 2, 2)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 3, 2, 2, 2)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 14)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 14)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 2, 3, 4, 4)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 2, 3, 4, 4)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 3, 1)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 3, 1)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 6, 8, 10, 12, 14, 16, 18, 20)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 6, 8, 10, 12, 14, 16, 18, 20)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(6, 1, 3, 5, 4, 7, 9, 7, 5, 3, 1, 5)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(6, 1, 3, 5, 4, 7, 9, 7, 5, 3, 1, 5)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 3, 3, 4, 4)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 3, 3, 4, 4)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3)), 5)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test13()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 18, 3, 2, 1, 4, 3, 2, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 18, 3, 2, 1, 4, 3, 2, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 2, 3, 2, 4, 4)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 2, 3, 2, 4, 4)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(8, 1, 3, 5, 7, 4, 9, 7, 5, 3, 1, 5)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(8, 1, 3, 5, 7, 4, 9, 7, 5, 3, 1, 5)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 3, 3, 4, 4)), 11) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 3, 3, 4, 4)), 11),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 2, 3, 2, 4, 4)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 2, 3, 2, 4, 4)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 3, 1, 5)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 3, 1, 5)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 6, 8, 10, 12, 14, 16, 18, 20)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 6, 8, 10, 12, 14, 16, 18, 20)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 12, 2, 3, 2, 4, 4)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 12, 2, 3, 2, 4, 4)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 2)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 2)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 1)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 1)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 6, 8, 10, 12, 14, 18, 11)), 5) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 6, 8, 10, 12, 14, 18, 11)), 5),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 1)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 1)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 4, 5, 6, 2)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 4, 5, 6, 2)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 18, 3, 3, 2, 1, 2, 3, 2, 2)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 18, 3, 3, 2, 1, 2, 3, 2, 2)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 3)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 3)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 3, 1)), 30) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 5, 7, 9, 7, 5, 3, 1)), 30),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 4, 2, 2)), -1) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 4, 2, 2)), -1),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1)), 31) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1)), 31),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 4, 5, 6, 2)), 20) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 4, 5, 6, 2)), 20),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 3, 3, 4, 4)), 18) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 3, 3, 4, 4)), 18),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 19, 2, 3)), 3) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 2, 1, 2, 3, 2, 1, 2, 19, 2, 3)), 3),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3)), 4) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3)), 4),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1)), 6) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1)), 6),
			s.willItFly(new ArrayList<>(Arrays.asList(4, 6, 8, 10, 12, 14, 16, 18, 20, 12)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(4, 6, 8, 10, 12, 14, 16, 18, 20, 12)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 2)), 0) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 2)), 0),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 19) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)), 19),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 30)), 14) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 30)), 14),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 4, 5, 6, 2)), 21) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 4, 5, 6, 2)), 21),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 3, 1, 5)), 9) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 3, 5, 7, 4, 9, 7, 5, 3, 1, 5)), 9),
			s.willItFly(new ArrayList<>(Arrays.asList(30, 2, 3, 2, 4, 4)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(30, 2, 3, 2, 4, 4)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 14)), 7) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 14)), 7),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 7, 2, 3, 2, 1, 2, 2, 2, 2)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 2, 3, 2, 7, 2, 3, 2, 1, 2, 2, 2, 2)), 12),
			s.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 3, 2, 2, 1, 2, 3, 2, 1)), 12) == s2.willItFly(new ArrayList<>(Arrays.asList(1, 8, 2, 3, 2, 1, 3, 2, 2, 1, 2, 3, 2, 1)), 12)
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void main(String[] args) throws NoSuchAlgorithmException {
		test0();
		test1();
		test2();
		test3();
		test4();
		test5();
		test6();
		test7();
		test8();
		test9();
		test10();
		test11();
		test12();
		test13();
	}
}
