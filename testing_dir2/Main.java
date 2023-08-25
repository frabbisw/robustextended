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
			s.countUpper("-2.8") == s2.countUpper("-2.8"),
			s.countUpper("3.6") == s2.countUpper("3.6"),
			s.countUpper("5.5") == s2.countUpper("5.5"),
			s.countUpper("-6.5") == s2.countUpper("-6.5"),
			s.countUpper("0.5") == s2.countUpper("0.5"),
			s.countUpper("1.6") == s2.countUpper("1.6"),
			s.countUpper("-1.6") == s2.countUpper("-1.6"),
			s.countUpper("0.0003") == s2.countUpper("0.0003"),
			s.countUpper("99.99") == s2.countUpper("99.99"),
			s.countUpper("-99.99") == s2.countUpper("-99.99"),
			s.countUpper("0") == s2.countUpper("0"),
			s.countUpper("-99.9") == s2.countUpper("-99.9"),
			s.countUpper("00") == s2.countUpper("00"),
			s.countUpper("999.99") == s2.countUpper("999.99"),
			s.countUpper("99.9999") == s2.countUpper("99.9999"),
			s.countUpper("99.999") == s2.countUpper("99.999"),
			s.countUpper("9.999") == s2.countUpper("9.999"),
			s.countUpper("999.999") == s2.countUpper("999.999"),
			s.countUpper("000") == s2.countUpper("000"),
			s.countUpper("09.99900") == s2.countUpper("09.99900"),
			s.countUpper("-999.99") == s2.countUpper("-999.99"),
			s.countUpper("99.9") == s2.countUpper("99.9"),
			s.countUpper("-99") == s2.countUpper("-99"),
			s.countUpper("-6.") == s2.countUpper("-6."),
			s.countUpper("0900") == s2.countUpper("0900"),
			s.countUpper("0000") == s2.countUpper("0000"),
			s.countUpper("-6.00000") == s2.countUpper("-6.00000"),
			s.countUpper("6") == s2.countUpper("6"),
			s.countUpper("-999") == s2.countUpper("-999"),
			s.countUpper("999") == s2.countUpper("999"),
			s.countUpper("11.6") == s2.countUpper("11.6"),
			s.countUpper("-6.00099900") == s2.countUpper("-6.00099900"),
			s.countUpper("111.6") == s2.countUpper("111.6"),
			s.countUpper("00900") == s2.countUpper("00900"),
			s.countUpper("-66.") == s2.countUpper("-66."),
			s.countUpper("11.") == s2.countUpper("11."),
			s.countUpper("-9111.699") == s2.countUpper("-9111.699"),
			s.countUpper("-6.65") == s2.countUpper("-6.65"),
			s.countUpper("5") == s2.countUpper("5"),
			s.countUpper("0009000") == s2.countUpper("0009000"),
			s.countUpper("-99.") == s2.countUpper("-99."),
			s.countUpper("-9.") == s2.countUpper("-9."),
			s.countUpper("-99000") == s2.countUpper("-99000"),
			s.countUpper("-5") == s2.countUpper("-5"),
			s.countUpper("900.999") == s2.countUpper("900.999"),
			s.countUpper("911.600") == s2.countUpper("911.600"),
			s.countUpper("-66666.") == s2.countUpper("-66666."),
			s.countUpper("-9111.6919") == s2.countUpper("-9111.6919"),
			s.countUpper("999.9999") == s2.countUpper("999.9999"),
			s.countUpper("-090109111.6919") == s2.countUpper("-090109111.6919")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test1()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("-9111.19") == s2.countUpper("-9111.19"),
			s.countUpper("009090") == s2.countUpper("009090"),
			s.countUpper("-6.000999006") == s2.countUpper("-6.000999006"),
			s.countUpper("9999.99") == s2.countUpper("9999.99"),
			s.countUpper("0009000000") == s2.countUpper("0009000000"),
			s.countUpper("-91111.691") == s2.countUpper("-91111.691"),
			s.countUpper("999000.999") == s2.countUpper("999000.999"),
			s.countUpper("-6.00") == s2.countUpper("-6.00"),
			s.countUpper("-6.000999900") == s2.countUpper("-6.000999900"),
			s.countUpper("-090109111.6919999") == s2.countUpper("-090109111.6919999"),
			s.countUpper("-6.9096") == s2.countUpper("-6.9096"),
			s.countUpper("911") == s2.countUpper("911"),
			s.countUpper("-6.000000") == s2.countUpper("-6.000000"),
			s.countUpper("-666666.") == s2.countUpper("-666666."),
			s.countUpper("66666.") == s2.countUpper("66666."),
			s.countUpper("9999.9999") == s2.countUpper("9999.9999"),
			s.countUpper("9.9") == s2.countUpper("9.9"),
			s.countUpper("1") == s2.countUpper("1"),
			s.countUpper("999.99999") == s2.countUpper("999.99999"),
			s.countUpper("-699.990") == s2.countUpper("-699.990"),
			s.countUpper("-66.6000") == s2.countUpper("-66.6000"),
			s.countUpper("9999") == s2.countUpper("9999"),
			s.countUpper("00090000") == s2.countUpper("00090000"),
			s.countUpper("0099090") == s2.countUpper("0099090"),
			s.countUpper("00009000") == s2.countUpper("00009000"),
			s.countUpper("9") == s2.countUpper("9"),
			s.countUpper("-919") == s2.countUpper("-919"),
			s.countUpper("000600") == s2.countUpper("000600"),
			s.countUpper("-9900") == s2.countUpper("-9900"),
			s.countUpper("00090099990") == s2.countUpper("00090099990"),
			s.countUpper("-6666666.") == s2.countUpper("-6666666."),
			s.countUpper(".9096") == s2.countUpper(".9096"),
			s.countUpper("00090000000") == s2.countUpper("00090000000"),
			s.countUpper("00600") == s2.countUpper("00600"),
			s.countUpper("9.9999") == s2.countUpper("9.9999"),
			s.countUpper("111.") == s2.countUpper("111."),
			s.countUpper("99") == s2.countUpper("99"),
			s.countUpper("00090000009.999000") == s2.countUpper("00090000009.999000"),
			s.countUpper("-6999.99000") == s2.countUpper("-6999.99000"),
			s.countUpper("0.000") == s2.countUpper("0.000"),
			s.countUpper("000900") == s2.countUpper("000900"),
			s.countUpper("-66666666.") == s2.countUpper("-66666666."),
			s.countUpper("000900000000") == s2.countUpper("000900000000"),
			s.countUpper("-9111191.691") == s2.countUpper("-9111191.691"),
			s.countUpper("99990099090.99") == s2.countUpper("99990099090.99"),
			s.countUpper("99999") == s2.countUpper("99999"),
			s.countUpper("0090900") == s2.countUpper("0090900"),
			s.countUpper("-60.00099900") == s2.countUpper("-60.00099900"),
			s.countUpper("-66966666.") == s2.countUpper("-66966666."),
			s.countUpper("-111.900090099990900") == s2.countUpper("-111.900090099990900")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test2()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("-54.9999") == s2.countUpper("-54.9999"),
			s.countUpper("0.0001") == s2.countUpper("0.0001"),
			s.countUpper("12345678.54321") == s2.countUpper("12345678.54321"),
			s.countUpper("-87654321.12345") == s2.countUpper("-87654321.12345"),
			s.countUpper("0.0000000009") == s2.countUpper("0.0000000009"),
			s.countUpper("1.234567890000000001") == s2.countUpper("1.234567890000000001"),
			s.countUpper("-1.234567890000000001") == s2.countUpper("-1.234567890000000001"),
			s.countUpper("-5.5") == s2.countUpper("-5.5"),
			s.countUpper("1.2345678900040000001") == s2.countUpper("1.2345678900040000001"),
			s.countUpper("0.00000000009") == s2.countUpper("0.00000000009"),
			s.countUpper("0.000000000009") == s2.countUpper("0.000000000009"),
			s.countUpper("0.9") == s2.countUpper("0.9"),
			s.countUpper("-787654321.12345") == s2.countUpper("-787654321.12345"),
			s.countUpper("1.0001") == s2.countUpper("1.0001"),
			s.countUpper("1.01") == s2.countUpper("1.01"),
			s.countUpper("-87654321.123345") == s2.countUpper("-87654321.123345"),
			s.countUpper("4.9999") == s2.countUpper("4.9999"),
			s.countUpper("11") == s2.countUpper("11"),
			s.countUpper("10.2345678900000000001") == s2.countUpper("10.2345678900000000001"),
			s.countUpper("10.23456789000000000001") == s2.countUpper("10.23456789000000000001"),
			s.countUpper("1.0") == s2.countUpper("1.0"),
			s.countUpper("-187654321.123345") == s2.countUpper("-187654321.123345"),
			s.countUpper("1.") == s2.countUpper("1."),
			s.countUpper("-51.234567890000000001") == s2.countUpper("-51.234567890000000001"),
			s.countUpper("0.09") == s2.countUpper("0.09"),
			s.countUpper("-9") == s2.countUpper("-9"),
			s.countUpper("-51.2354567890000000001") == s2.countUpper("-51.2354567890000000001"),
			s.countUpper("0.") == s2.countUpper("0."),
			s.countUpper("1.001") == s2.countUpper("1.001"),
			s.countUpper("1.011") == s2.countUpper("1.011"),
			s.countUpper("-51.27890000000001") == s2.countUpper("-51.27890000000001"),
			s.countUpper("5.55") == s2.countUpper("5.55"),
			s.countUpper("-91.01") == s2.countUpper("-91.01"),
			s.countUpper("-87654321.212345") == s2.countUpper("-87654321.212345"),
			s.countUpper("-51.278900000000001") == s2.countUpper("-51.278900000000001"),
			s.countUpper("10.234567890000000000091") == s2.countUpper("10.234567890000000000091"),
			s.countUpper("0.000000000000") == s2.countUpper("0.000000000000"),
			s.countUpper("11.99") == s2.countUpper("11.99"),
			s.countUpper("55.5") == s2.countUpper("55.5"),
			s.countUpper("1.00001") == s2.countUpper("1.00001"),
			s.countUpper("-51.278590000000001") == s2.countUpper("-51.278590000000001"),
			s.countUpper("0.00000000") == s2.countUpper("0.00000000"),
			s.countUpper("1234567821") == s2.countUpper("1234567821"),
			s.countUpper("111") == s2.countUpper("111"),
			s.countUpper("01") == s2.countUpper("01"),
			s.countUpper("-51.1234567890000000001") == s2.countUpper("-51.1234567890000000001"),
			s.countUpper("11.9") == s2.countUpper("11.9"),
			s.countUpper("-5787654321.12345") == s2.countUpper("-5787654321.12345"),
			s.countUpper("1.00") == s2.countUpper("1.00"),
			s.countUpper("1111") == s2.countUpper("1111")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test3()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("00.0000000000000") == s2.countUpper("00.0000000000000"),
			s.countUpper("-599.5") == s2.countUpper("-599.5"),
			s.countUpper("001") == s2.countUpper("001"),
			s.countUpper("00.00000000000000") == s2.countUpper("00.00000000000000"),
			s.countUpper("11111") == s2.countUpper("11111"),
			s.countUpper("0.0000000010") == s2.countUpper("0.0000000010"),
			s.countUpper("10.23456789000000000011101") == s2.countUpper("10.23456789000000000011101"),
			s.countUpper("911.99") == s2.countUpper("911.99"),
			s.countUpper("10.23456789000000011111000091") == s2.countUpper("10.23456789000000011111000091"),
			s.countUpper("111111") == s2.countUpper("111111"),
			s.countUpper("10.00001") == s2.countUpper("10.00001"),
			s.countUpper("000.000000000000000") == s2.countUpper("000.000000000000000"),
			s.countUpper("-51.123456789001111100000001") == s2.countUpper("-51.123456789001111100000001"),
			s.countUpper("-91.") == s2.countUpper("-91."),
			s.countUpper("00000000") == s2.countUpper("00000000"),
			s.countUpper("0.0000000000000") == s2.countUpper("0.0000000000000"),
			s.countUpper("10001") == s2.countUpper("10001"),
			s.countUpper("-511.23545678900000500001") == s2.countUpper("-511.23545678900000500001"),
			s.countUpper("-687654321.12345") == s2.countUpper("-687654321.12345"),
			s.countUpper("-578000000007654321.12345") == s2.countUpper("-578000000007654321.12345"),
			s.countUpper("-51.1223456789001111100000001") == s2.countUpper("-51.1223456789001111100000001"),
			s.countUpper("-5780000000076254321.162345") == s2.countUpper("-5780000000076254321.162345"),
			s.countUpper("-01.234567890000000001") == s2.countUpper("-01.234567890000000001"),
			s.countUpper("0.0") == s2.countUpper("0.0"),
			s.countUpper("000.00000000000000000") == s2.countUpper("000.00000000000000000"),
			s.countUpper("-687654321.152345") == s2.countUpper("-687654321.152345"),
			s.countUpper("-5787.12345") == s2.countUpper("-5787.12345"),
			s.countUpper("10.2345678900000001") == s2.countUpper("10.2345678900000001"),
			s.countUpper("5.555") == s2.countUpper("5.555"),
			s.countUpper("1111.") == s2.countUpper("1111."),
			s.countUpper("00.0001") == s2.countUpper("00.0001"),
			s.countUpper("-54.99999") == s2.countUpper("-54.99999"),
			s.countUpper("1111111") == s2.countUpper("1111111"),
			s.countUpper("1.1001") == s2.countUpper("1.1001"),
			s.countUpper("-51.2345678900000002001") == s2.countUpper("-51.2345678900000002001"),
			s.countUpper("0.011111") == s2.countUpper("0.011111"),
			s.countUpper("12534567821") == s2.countUpper("12534567821"),
			s.countUpper("1.0000011") == s2.countUpper("1.0000011"),
			s.countUpper("9111.9900") == s2.countUpper("9111.9900"),
			s.countUpper("1000101") == s2.countUpper("1000101"),
			s.countUpper("12345678.521") == s2.countUpper("12345678.521"),
			s.countUpper("1.0111") == s2.countUpper("1.0111"),
			s.countUpper("10.234567890000001") == s2.countUpper("10.234567890000001"),
			s.countUpper("555.5") == s2.countUpper("555.5"),
			s.countUpper("-51.20000000001") == s2.countUpper("-51.20000000001"),
			s.countUpper("101.234567890000001") == s2.countUpper("101.234567890000001"),
			s.countUpper("1.0099") == s2.countUpper("1.0099"),
			s.countUpper("911001.99") == s2.countUpper("911001.99"),
			s.countUpper("-787654321.12") == s2.countUpper("-787654321.12"),
			s.countUpper("1.00111") == s2.countUpper("1.00111")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test4()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("-54.999") == s2.countUpper("-54.999"),
			s.countUpper("-191.01") == s2.countUpper("-191.01"),
			s.countUpper("-5780007.12345") == s2.countUpper("-5780007.12345"),
			s.countUpper("-7876521.12345") == s2.countUpper("-7876521.12345"),
			s.countUpper("-599") == s2.countUpper("-599"),
			s.countUpper("0010.234567890000000000091000000") == s2.countUpper("0010.234567890000000000091000000"),
			s.countUpper("1.000001") == s2.countUpper("1.000001"),
			s.countUpper("125345678221") == s2.countUpper("125345678221"),
			s.countUpper("10.0000000010") == s2.countUpper("10.0000000010"),
			s.countUpper("-687654321.122345") == s2.countUpper("-687654321.122345"),
			s.countUpper("-5780017.12345") == s2.countUpper("-5780017.12345"),
			s.countUpper("1.10001010") == s2.countUpper("1.10001010"),
			s.countUpper("100001") == s2.countUpper("100001"),
			s.countUpper("111.9") == s2.countUpper("111.9"),
			s.countUpper("-51.12340001") == s2.countUpper("-51.12340001"),
			s.countUpper("10.234567890000000001") == s2.countUpper("10.234567890000000001"),
			s.countUpper("91000000") == s2.countUpper("91000000"),
			s.countUpper("99.99999") == s2.countUpper("99.99999"),
			s.countUpper("10.21") == s2.countUpper("10.21"),
			s.countUpper("9911.99") == s2.countUpper("9911.99"),
			s.countUpper("-051.278900000000001") == s2.countUpper("-051.278900000000001"),
			s.countUpper("11100") == s2.countUpper("11100"),
			s.countUpper("-5787.122345") == s2.countUpper("-5787.122345"),
			s.countUpper("4.94999") == s2.countUpper("4.94999"),
			s.countUpper("-051.123456789001111100000001") == s2.countUpper("-051.123456789001111100000001"),
			s.countUpper("10.234556789000000000011101") == s2.countUpper("10.234556789000000000011101"),
			s.countUpper("1.1001010") == s2.countUpper("1.1001010"),
			s.countUpper("12534567") == s2.countUpper("12534567"),
			s.countUpper("000000000") == s2.countUpper("000000000"),
			s.countUpper("-511.235456789000005000001") == s2.countUpper("-511.235456789000005000001"),
			s.countUpper("00.") == s2.countUpper("00."),
			s.countUpper("-51.2789000") == s2.countUpper("-51.2789000"),
			s.countUpper("101") == s2.countUpper("101"),
			s.countUpper("0101") == s2.countUpper("0101"),
			s.countUpper("125345678.521") == s2.countUpper("125345678.521"),
			s.countUpper("123456782101.2345678900000011") == s2.countUpper("123456782101.2345678900000011"),
			s.countUpper("654321.12345") == s2.countUpper("654321.12345"),
			s.countUpper("-6876542345") == s2.countUpper("-6876542345"),
			s.countUpper("0111111101") == s2.countUpper("0111111101"),
			s.countUpper("-87654321.123485") == s2.countUpper("-87654321.123485"),
			s.countUpper("-0051.123456789001111100000001") == s2.countUpper("-0051.123456789001111100000001"),
			s.countUpper("1.000011011") == s2.countUpper("1.000011011"),
			s.countUpper("-51.1234001") == s2.countUpper("-51.1234001"),
			s.countUpper("-57008000000007654321.12345") == s2.countUpper("-57008000000007654321.12345"),
			s.countUpper("-5780000000076254654321.123452345") == s2.countUpper("-5780000000076254654321.123452345"),
			s.countUpper("11111111") == s2.countUpper("11111111"),
			s.countUpper("-876514321.212345") == s2.countUpper("-876514321.212345"),
			s.countUpper("9911.919") == s2.countUpper("9911.919"),
			s.countUpper("-00.55") == s2.countUpper("-00.55"),
			s.countUpper("94.9999") == s2.countUpper("94.9999")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test5()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("-570080000000076543221.12345") == s2.countUpper("-570080000000076543221.12345"),
			s.countUpper("55") == s2.countUpper("55"),
			s.countUpper("000.0000000000000000") == s2.countUpper("000.0000000000000000"),
			s.countUpper("-57817654321.12345") == s2.countUpper("-57817654321.12345"),
			s.countUpper("1.00111100015") == s2.countUpper("1.00111100015"),
			s.countUpper("-0000921.12345") == s2.countUpper("-0000921.12345"),
			s.countUpper("-5700800.12345") == s2.countUpper("-5700800.12345"),
			s.countUpper("00.000001") == s2.countUpper("00.000001"),
			s.countUpper("111111111") == s2.countUpper("111111111"),
			s.countUpper("9100") == s2.countUpper("9100"),
			s.countUpper("995") == s2.countUpper("995"),
			s.countUpper("-51.279989000") == s2.countUpper("-51.279989000"),
			s.countUpper("-0.000000000099599") == s2.countUpper("-0.000000000099599"),
			s.countUpper("10.2345567890000000000111091001") == s2.countUpper("10.2345567890000000000111091001"),
			s.countUpper("10.000001") == s2.countUpper("10.000001"),
			s.countUpper("-876543345") == s2.countUpper("-876543345"),
			s.countUpper("10.234556789000000011101") == s2.countUpper("10.234556789000000011101"),
			s.countUpper("-5787.123345") == s2.countUpper("-5787.123345"),
			s.countUpper("10.234567890001") == s2.countUpper("10.234567890001"),
			s.countUpper("10.2345567189000000000011101") == s2.countUpper("10.2345567189000000000011101"),
			s.countUpper("0000.0000") == s2.countUpper("0000.0000"),
			s.countUpper("3231.12345") == s2.countUpper("3231.12345"),
			s.countUpper("601111111101345") == s2.countUpper("601111111101345"),
			s.countUpper("-876000.000000000000000543345") == s2.countUpper("-876000.000000000000000543345"),
			s.countUpper("94999") == s2.countUpper("94999"),
			s.countUpper("00.000000000000011111") == s2.countUpper("00.000000000000011111"),
			s.countUpper("1111111111") == s2.countUpper("1111111111"),
			s.countUpper("0.1011111") == s2.countUpper("0.1011111"),
			s.countUpper("10.2345678900000011") == s2.countUpper("10.2345678900000011"),
			s.countUpper("10.23456789000000001") == s2.countUpper("10.23456789000000001"),
			s.countUpper("100011.0011110001501") == s2.countUpper("100011.0011110001501"),
			s.countUpper("12345678.543211") == s2.countUpper("12345678.543211"),
			s.countUpper("-55.5") == s2.countUpper("-55.5"),
			s.countUpper("011") == s2.countUpper("011"),
			s.countUpper("-27890000000001") == s2.countUpper("-27890000000001"),
			s.countUpper("0010.234567890000000601111111101345000091000000") == s2.countUpper("0010.234567890000000601111111101345000091000000"),
			s.countUpper("11.1011") == s2.countUpper("11.1011"),
			s.countUpper("-87654") == s2.countUpper("-87654"),
			s.countUpper("-26876542345") == s2.countUpper("-26876542345"),
			s.countUpper("-9599.5") == s2.countUpper("-9599.5"),
			s.countUpper("0101.234567890000001") == s2.countUpper("0101.234567890000001"),
			s.countUpper("109100") == s2.countUpper("109100"),
			s.countUpper("-5787.123") == s2.countUpper("-5787.123"),
			s.countUpper("10.23000091") == s2.countUpper("10.23000091"),
			s.countUpper("990.001") == s2.countUpper("990.001"),
			s.countUpper("-87654321.1213485") == s2.countUpper("-87654321.1213485"),
			s.countUpper("5125345678215") == s2.countUpper("5125345678215"),
			s.countUpper("111.10111") == s2.countUpper("111.10111"),
			s.countUpper("111.5510111") == s2.countUpper("111.5510111"),
			s.countUpper("125345678221111") == s2.countUpper("125345678221111")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test6()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("9955") == s2.countUpper("9955"),
			s.countUpper("-574321.12345") == s2.countUpper("-574321.12345"),
			s.countUpper("-51.02789000") == s2.countUpper("-51.02789000"),
			s.countUpper("-5.55") == s2.countUpper("-5.55"),
			s.countUpper("-8761.0154") == s2.countUpper("-8761.0154"),
			s.countUpper("1911.9925345678221") == s2.countUpper("1911.9925345678221"),
			s.countUpper("-68765424345") == s2.countUpper("-68765424345"),
			s.countUpper("11.00001000") == s2.countUpper("11.00001000"),
			s.countUpper("-51.2785900000000001") == s2.countUpper("-51.2785900000000001"),
			s.countUpper("9995100") == s2.countUpper("9995100"),
			s.countUpper("123475678.521") == s2.countUpper("123475678.521"),
			s.countUpper("0.000000") == s2.countUpper("0.000000"),
			s.countUpper("000.") == s2.countUpper("000."),
			s.countUpper("-59654321.12345") == s2.countUpper("-59654321.12345"),
			s.countUpper("-2687654245") == s2.countUpper("-2687654245"),
			s.countUpper("-278900000") == s2.countUpper("-278900000"),
			s.countUpper("1000.00000000000000001111") == s2.countUpper("1000.00000000000000001111"),
			s.countUpper("-26876540010.234567890000000010000002345") == s2.countUpper("-26876540010.234567890000000010000002345"),
			s.countUpper("-57101817654321.12345") == s2.countUpper("-57101817654321.12345"),
			s.countUpper("5.5125345678215555") == s2.countUpper("5.5125345678215555"),
			s.countUpper("1000012345678.5432111") == s2.countUpper("1000012345678.5432111"),
			s.countUpper("-51.1234567890011111000000") == s2.countUpper("-51.1234567890011111000000"),
			s.countUpper("4.994999") == s2.countUpper("4.994999"),
			s.countUpper("1.00111101") == s2.countUpper("1.00111101"),
			s.countUpper("494.9999") == s2.countUpper("494.9999"),
			s.countUpper("94.99999") == s2.countUpper("94.99999"),
			s.countUpper("654321.123345") == s2.countUpper("654321.123345"),
			s.countUpper(".12345") == s2.countUpper(".12345"),
			s.countUpper("-9999955") == s2.countUpper("-9999955"),
			s.countUpper("-57121.12345") == s2.countUpper("-57121.12345"),
			s.countUpper("-99999955") == s2.countUpper("-99999955"),
			s.countUpper("-51.23456789000000002001") == s2.countUpper("-51.23456789000000002001"),
			s.countUpper("654321.122345") == s2.countUpper("654321.122345"),
			s.countUpper("-51234567820.10111111") == s2.countUpper("-51234567820.10111111"),
			s.countUpper("111.1") == s2.countUpper("111.1"),
			s.countUpper("-57121.125345") == s2.countUpper("-57121.125345"),
			s.countUpper("604555.55") == s2.countUpper("604555.55"),
			s.countUpper("000.0001253456700000000000000") == s2.countUpper("000.0001253456700000000000000"),
			s.countUpper("-151.0279000") == s2.countUpper("-151.0279000"),
			s.countUpper("1001") == s2.countUpper("1001"),
			s.countUpper("10.001") == s2.countUpper("10.001"),
			s.countUpper("-9999995") == s2.countUpper("-9999995"),
			s.countUpper("0010.2345678900000000091000000") == s2.countUpper("0010.2345678900000000091000000"),
			s.countUpper("00125345678.521000000") == s2.countUpper("00125345678.521000000"),
			s.countUpper("-8769955543345") == s2.countUpper("-8769955543345"),
			s.countUpper("10.2300") == s2.countUpper("10.2300"),
			s.countUpper("-99999995") == s2.countUpper("-99999995"),
			s.countUpper("-51.12314567890011111000500001") == s2.countUpper("-51.12314567890011111000500001"),
			s.countUpper("0000.") == s2.countUpper("0000."),
			s.countUpper("1100010.234567890001") == s2.countUpper("1100010.234567890001")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test7()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("0.0111011") == s2.countUpper("0.0111011"),
			s.countUpper("-00009121.12345") == s2.countUpper("-00009121.12345"),
			s.countUpper("5.5551") == s2.countUpper("5.5551"),
			s.countUpper("-51.1234567890011511100000001") == s2.countUpper("-51.1234567890011511100000001"),
			s.countUpper("11001") == s2.countUpper("11001"),
			s.countUpper("10.234569100000078900000000001") == s2.countUpper("10.234569100000078900000000001"),
			s.countUpper("99501015") == s2.countUpper("99501015"),
			s.countUpper("0000.00000") == s2.countUpper("0000.00000"),
			s.countUpper("-51.27859000000001") == s2.countUpper("-51.27859000000001"),
			s.countUpper("-268555.576542345") == s2.countUpper("-268555.576542345"),
			s.countUpper("10.234100015678900000011") == s2.countUpper("10.234100015678900000011"),
			s.countUpper("1111.5510111") == s2.countUpper("1111.5510111"),
			s.countUpper("-0.00000099599") == s2.countUpper("-0.00000099599"),
			s.countUpper("00000.0000") == s2.countUpper("00000.0000"),
			s.countUpper("-.27859000000001") == s2.countUpper("-.27859000000001"),
			s.countUpper("-154.949990") == s2.countUpper("-154.949990"),
			s.countUpper("1.0011110") == s2.countUpper("1.0011110"),
			s.countUpper("1000.000125345670000000000000011111") == s2.countUpper("1000.000125345670000000000000011111"),
			s.countUpper("12345678.5251") == s2.countUpper("12345678.5251"),
			s.countUpper("1100010.2934567890001") == s2.countUpper("1100010.2934567890001"),
			s.countUpper("1111.11011") == s2.countUpper("1111.11011"),
			s.countUpper("5.51253345678215555") == s2.countUpper("5.51253345678215555"),
			s.countUpper("94.99991111119") == s2.countUpper("94.99991111119"),
			s.countUpper("111.511") == s2.countUpper("111.511"),
			s.countUpper("0.00000099550009") == s2.countUpper("0.00000099550009"),
			s.countUpper("00.00001") == s2.countUpper("00.00001"),
			s.countUpper("-876543211001.123345") == s2.countUpper("-876543211001.123345"),
			s.countUpper("99.001") == s2.countUpper("99.001"),
			s.countUpper("0.011") == s2.countUpper("0.011"),
			s.countUpper("110.00001") == s2.countUpper("110.00001"),
			s.countUpper("0.0000000000099") == s2.countUpper("0.0000000000099"),
			s.countUpper("10001011") == s2.countUpper("10001011"),
			s.countUpper("0.00000000010") == s2.countUpper("0.00000000010"),
			s.countUpper("-51.202789000") == s2.countUpper("-51.202789000"),
			s.countUpper("12345678.5431") == s2.countUpper("12345678.5431"),
			s.countUpper("111001") == s2.countUpper("111001"),
			s.countUpper("10.230") == s2.countUpper("10.230"),
			s.countUpper("-91.011") == s2.countUpper("-91.011"),
			s.countUpper("1911.99253452678221") == s2.countUpper("1911.99253452678221"),
			s.countUpper("-51.2729989000") == s2.countUpper("-51.2729989000"),
			s.countUpper("110010.9") == s2.countUpper("110010.9"),
			s.countUpper("9911.999") == s2.countUpper("9911.999"),
			s.countUpper("11.000001000") == s2.countUpper("11.000001000"),
			s.countUpper("9911999") == s2.countUpper("9911999"),
			s.countUpper("6045555.55") == s2.countUpper("6045555.55"),
			s.countUpper("01111111101") == s2.countUpper("01111111101"),
			s.countUpper("-51.2789000000001") == s2.countUpper("-51.2789000000001"),
			s.countUpper("-9991.011") == s2.countUpper("-9991.011"),
			s.countUpper("0.0000000") == s2.countUpper("0.0000000"),
			s.countUpper("-187654321.1345") == s2.countUpper("-187654321.1345")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test8()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("-268765410.000001245") == s2.countUpper("-268765410.000001245"),
			s.countUpper("1000101.0011110001501") == s2.countUpper("1000101.0011110001501"),
			s.countUpper("10.2341006015678900000011") == s2.countUpper("10.2341006015678900000011"),
			s.countUpper("1253456782211111.0") == s2.countUpper("1253456782211111.0"),
			s.countUpper("9499") == s2.countUpper("9499"),
			s.countUpper("5123475678.521") == s2.countUpper("5123475678.521"),
			s.countUpper("19111.99253452678221") == s2.countUpper("19111.99253452678221"),
			s.countUpper("10.12345678900000000001") == s2.countUpper("10.12345678900000000001"),
			s.countUpper("1111.50111") == s2.countUpper("1111.50111"),
			s.countUpper("-876514321.21234") == s2.countUpper("-876514321.21234"),
			s.countUpper("789000001.123345") == s2.countUpper("789000001.123345"),
			s.countUpper("-051.02789000") == s2.countUpper("-051.02789000"),
			s.countUpper("-2687654235") == s2.countUpper("-2687654235"),
			s.countUpper("10011") == s2.countUpper("10011"),
			s.countUpper("9911.9999") == s2.countUpper("9911.9999"),
			s.countUpper("-5787.1233") == s2.countUpper("-5787.1233"),
			s.countUpper("1909100") == s2.countUpper("1909100"),
			s.countUpper("-51.23001") == s2.countUpper("-51.23001"),
			s.countUpper("1000.000000000000000001111") == s2.countUpper("1000.000000000000000001111"),
			s.countUpper(".011") == s2.countUpper(".011"),
			s.countUpper("-51.027890000") == s2.countUpper("-51.027890000"),
			s.countUpper("-268765421.0000145") == s2.countUpper("-268765421.0000145"),
			s.countUpper("-999.011") == s2.countUpper("-999.011"),
			s.countUpper("100.001") == s2.countUpper("100.001"),
			s.countUpper("-999999955") == s2.countUpper("-999999955"),
			s.countUpper("0.000000000000000000000000000000000000000000000000000000000000000000000000000001") == s2.countUpper("0.000000000000000000000000000000000000000000000000000000000000000000000000000001"),
			s.countUpper("1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000") == s2.countUpper("1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"),
			s.countUpper("-1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000") == s2.countUpper("-1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"),
			s.countUpper("-0.000000000000000000000000000000000000000000000000000000000000000000000000000000001") == s2.countUpper("-0.000000000000000000000000000000000000000000000000000000000000000000000000000000001"),
			s.countUpper("-0") == s2.countUpper("-0"),
			s.countUpper("-0.5") == s2.countUpper("-0.5"),
			s.countUpper("9999999999999999999999999999999999999999999999999999999999999.5") == s2.countUpper("9999999999999999999999999999999999999999999999999999999999999.5"),
			s.countUpper("-9999999999999999999999999999999999999999999999999999999999999.5") == s2.countUpper("-9999999999999999999999999999999999999999999999999999999999999.5"),
			s.countUpper("0.00001") == s2.countUpper("0.00001"),
			s.countUpper("-1.23405678900000000001") == s2.countUpper("-1.23405678900000000001"),
			s.countUpper("-8761.12345") == s2.countUpper("-8761.12345"),
			s.countUpper("-1.2034567890000000001") == s2.countUpper("-1.2034567890000000001"),
			s.countUpper("-454.9999") == s2.countUpper("-454.9999"),
			s.countUpper("1.2345607890000000001") == s2.countUpper("1.2345607890000000001"),
			s.countUpper("-1.201345678900000000001") == s2.countUpper("-1.201345678900000000001"),
			s.countUpper("-1.2013456789000000000001") == s2.countUpper("-1.2013456789000000000001"),
			s.countUpper("-876544321.12345") == s2.countUpper("-876544321.12345"),
			s.countUpper("1.2345678900000000001") == s2.countUpper("1.2345678900000000001"),
			s.countUpper("-876654321.12345") == s2.countUpper("-876654321.12345"),
			s.countUpper("-1.20134560789000000000001") == s2.countUpper("-1.20134560789000000000001"),
			s.countUpper("1.23456078900000000001") == s2.countUpper("1.23456078900000000001"),
			s.countUpper("-8765421.12345") == s2.countUpper("-8765421.12345"),
			s.countUpper("-2345") == s2.countUpper("-2345"),
			s.countUpper("-234") == s2.countUpper("-234"),
			s.countUpper("-1.2345607890000000001") == s2.countUpper("-1.2345607890000000001")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test9()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("0.000001") == s2.countUpper("0.000001"),
			s.countUpper("-87654432.12345") == s2.countUpper("-87654432.12345"),
			s.countUpper("-1") == s2.countUpper("-1"),
			s.countUpper("-1.20134567890000000000001") == s2.countUpper("-1.20134567890000000000001"),
			s.countUpper("-54.9") == s2.countUpper("-54.9"),
			s.countUpper("-454.59999") == s2.countUpper("-454.59999"),
			s.countUpper("-1.234056789000000000001") == s2.countUpper("-1.234056789000000000001"),
			s.countUpper("-1.20134567899000000000001") == s2.countUpper("-1.20134567899000000000001"),
			s.countUpper("-1.2013945678900000000001") == s2.countUpper("-1.2013945678900000000001"),
			s.countUpper("-1.20345672890000000001") == s2.countUpper("-1.20345672890000000001"),
			s.countUpper("12678.54321") == s2.countUpper("12678.54321"),
			s.countUpper("-1.234055670001") == s2.countUpper("-1.234055670001"),
			s.countUpper(".5") == s2.countUpper(".5"),
			s.countUpper("-24345") == s2.countUpper("-24345"),
			s.countUpper("12678.254321") == s2.countUpper("12678.254321"),
			s.countUpper("12678.543251") == s2.countUpper("12678.543251"),
			s.countUpper("-2334") == s2.countUpper("-2334"),
			s.countUpper("-23") == s2.countUpper("-23"),
			s.countUpper("-1.2340567890000000001") == s2.countUpper("-1.2340567890000000001"),
			s.countUpper("-87565421.12345") == s2.countUpper("-87565421.12345"),
			s.countUpper("-1.20304567890000000001") == s2.countUpper("-1.20304567890000000001"),
			s.countUpper("-1.2034567890001") == s2.countUpper("-1.2034567890001"),
			s.countUpper("-1.201345678900000000000091") == s2.countUpper("-1.201345678900000000000091"),
			s.countUpper("-243545") == s2.countUpper("-243545"),
			s.countUpper("-11.234055670001") == s2.countUpper("-11.234055670001"),
			s.countUpper("1.230456789000000001") == s2.countUpper("1.230456789000000001"),
			s.countUpper("-1.230304567890000000001") == s2.countUpper("-1.230304567890000000001"),
			s.countUpper("-21.23456789000000000013") == s2.countUpper("-21.23456789000000000013"),
			s.countUpper("-1.201394567890000001") == s2.countUpper("-1.201394567890000001"),
			s.countUpper("-1.20134567899000000000") == s2.countUpper("-1.20134567899000000000"),
			s.countUpper("-454.") == s2.countUpper("-454."),
			s.countUpper("-1.23405567000") == s2.countUpper("-1.23405567000"),
			s.countUpper("-1.203045678900000000901") == s2.countUpper("-1.203045678900000000901"),
			s.countUpper("00.0000000009") == s2.countUpper("00.0000000009"),
			s.countUpper("-1.203456728900000000401") == s2.countUpper("-1.203456728900000000401"),
			s.countUpper("-234523") == s2.countUpper("-234523"),
			s.countUpper("126784.2544321") == s2.countUpper("126784.2544321"),
			s.countUpper("-1.234560789000000000010000000001") == s2.countUpper("-1.234560789000000000010000000001"),
			s.countUpper("-41.20134560789000000000001") == s2.countUpper("-41.20134560789000000000001"),
			s.countUpper("-245") == s2.countUpper("-245"),
			s.countUpper("-23412345678.54321") == s2.countUpper("-23412345678.54321"),
			s.countUpper("-2344") == s2.countUpper("-2344"),
			s.countUpper("1.237890000000001") == s2.countUpper("1.237890000000001"),
			s.countUpper("9999.99999") == s2.countUpper("9999.99999"),
			s.countUpper("-2234") == s2.countUpper("-2234"),
			s.countUpper("-87654321.121345") == s2.countUpper("-87654321.121345"),
			s.countUpper("1.234560789000000000091") == s2.countUpper("1.234560789000000000091"),
			s.countUpper("000001") == s2.countUpper("000001"),
			s.countUpper("-1.2013456780900000000001") == s2.countUpper("-1.2013456780900000000001"),
			s.countUpper("000000") == s2.countUpper("000000")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test10()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("-1.2013456078900000300") == s2.countUpper("-1.2013456078900000300"),
			s.countUpper("00.00000000009") == s2.countUpper("00.00000000009"),
			s.countUpper("-1.2303045678900000000001") == s2.countUpper("-1.2303045678900000000001"),
			s.countUpper("-875654221.12345") == s2.countUpper("-875654221.12345"),
			s.countUpper("12678.5432") == s2.countUpper("12678.5432"),
			s.countUpper("-2435545") == s2.countUpper("-2435545"),
			s.countUpper("0.0000001") == s2.countUpper("0.0000001"),
			s.countUpper("-22234") == s2.countUpper("-22234"),
			s.countUpper("-1.2345607890000000000100000700001") == s2.countUpper("-1.2345607890000000000100000700001"),
			s.countUpper("-1.2303045067890000000001") == s2.countUpper("-1.2303045067890000000001"),
			s.countUpper("-1.23456078900100000000100000700001") == s2.countUpper("-1.23456078900100000000100000700001"),
			s.countUpper("-222324") == s2.countUpper("-222324"),
			s.countUpper("-1.20134567809000000000001") == s2.countUpper("-1.20134567809000000000001"),
			s.countUpper("-1.230304501") == s2.countUpper("-1.230304501"),
			s.countUpper("-2") == s2.countUpper("-2"),
			s.countUpper("-1.2030456708900000000901") == s2.countUpper("-1.2030456708900000000901"),
			s.countUpper("-8235412345678.5") == s2.countUpper("-8235412345678.5"),
			s.countUpper("-87654321.123450000000") == s2.countUpper("-87654321.123450000000"),
			s.countUpper("-876654321.125345") == s2.countUpper("-876654321.125345"),
			s.countUpper("-2312678.54325134") == s2.countUpper("-2312678.54325134"),
			s.countUpper("-1.2345678900000050001") == s2.countUpper("-1.2345678900000050001"),
			s.countUpper("123456678.54321") == s2.countUpper("123456678.54321"),
			s.countUpper("-1.23405670001") == s2.countUpper("-1.23405670001"),
			s.countUpper("-1.203456724890000000001") == s2.countUpper("-1.203456724890000000001"),
			s.countUpper("-1.201345678900000000000000000001") == s2.countUpper("-1.201345678900000000000000000001"),
			s.countUpper("-2223224") == s2.countUpper("-2223224"),
			s.countUpper("99999.99999") == s2.countUpper("99999.99999"),
			s.countUpper("-200.00000000009") == s2.countUpper("-200.00000000009"),
			s.countUpper("-24") == s2.countUpper("-24"),
			s.countUpper("-1.23400000000000001") == s2.countUpper("-1.23400000000000001"),
			s.countUpper("-87654321.1213435") == s2.countUpper("-87654321.1213435"),
			s.countUpper("999999999") == s2.countUpper("999999999"),
			s.countUpper("-8745") == s2.countUpper("-8745"),
			s.countUpper("-23434") == s2.countUpper("-23434"),
			s.countUpper("-22324") == s2.countUpper("-22324"),
			s.countUpper("-323") == s2.countUpper("-323"),
			s.countUpper("-22434") == s2.countUpper("-22434"),
			s.countUpper("-1.20139456789000000050001") == s2.countUpper("-1.20139456789000000050001"),
			s.countUpper("0.000000009009") == s2.countUpper("0.000000009009"),
			s.countUpper("-541.234567890000000000199999") == s2.countUpper("-541.234567890000000000199999"),
			s.countUpper("-8745654221.12345") == s2.countUpper("-8745654221.12345"),
			s.countUpper("00005") == s2.countUpper("00005"),
			s.countUpper("-2312678.543251334") == s2.countUpper("-2312678.543251334"),
			s.countUpper("-24512345678.54321") == s2.countUpper("-24512345678.54321"),
			s.countUpper("999999.99999") == s2.countUpper("999999.99999"),
			s.countUpper("-10.00001") == s2.countUpper("-10.00001"),
			s.countUpper("-1.201") == s2.countUpper("-1.201"),
			s.countUpper("123456678.543221") == s2.countUpper("123456678.543221"),
			s.countUpper("-1.23456078900000050001") == s2.countUpper("-1.23456078900000050001"),
			s.countUpper("-8235412345678.25") == s2.countUpper("-8235412345678.25")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test11()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("-22") == s2.countUpper("-22"),
			s.countUpper("99.999999") == s2.countUpper("99.999999"),
			s.countUpper("-31.2303045067890000000001") == s2.countUpper("-31.2303045067890000000001"),
			s.countUpper("999999.999999") == s2.countUpper("999999.999999"),
			s.countUpper("00999.999990001") == s2.countUpper("00999.999990001"),
			s.countUpper("-1.20131") == s2.countUpper("-1.20131"),
			s.countUpper("1.234560789000000000001") == s2.countUpper("1.234560789000000000001"),
			s.countUpper("-87654432.1234") == s2.countUpper("-87654432.1234"),
			s.countUpper("1.2345607890000000000091") == s2.countUpper("1.2345607890000000000091"),
			s.countUpper("1234566678.543221") == s2.countUpper("1234566678.543221"),
			s.countUpper("-87654432.212345") == s2.countUpper("-87654432.212345"),
			s.countUpper("-1.234056711") == s2.countUpper("-1.234056711"),
			s.countUpper("-299.9999992434") == s2.countUpper("-299.9999992434"),
			s.countUpper("-1.23030450678900000030001") == s2.countUpper("-1.23030450678900000030001"),
			s.countUpper("-1.23456078900000000001") == s2.countUpper("-1.23456078900000000001"),
			s.countUpper("-454.59") == s2.countUpper("-454.59"),
			s.countUpper("-1.2034567289000200000401") == s2.countUpper("-1.2034567289000200000401"),
			s.countUpper("-1.234105678900000000001") == s2.countUpper("-1.234105678900000000001"),
			s.countUpper("-5.555") == s2.countUpper("-5.555"),
			s.countUpper("-87654321.12145") == s2.countUpper("-87654321.12145"),
			s.countUpper("-877654321.12345") == s2.countUpper("-877654321.12345"),
			s.countUpper("-2434123456738.54321") == s2.countUpper("-2434123456738.54321"),
			s.countUpper("39456789009000000001") == s2.countUpper("39456789009000000001"),
			s.countUpper("-1.201345670809000000000001") == s2.countUpper("-1.201345670809000000000001"),
			s.countUpper("-11.201") == s2.countUpper("-11.201"),
			s.countUpper("-224") == s2.countUpper("-224"),
			s.countUpper("-544.95999") == s2.countUpper("-544.95999"),
			s.countUpper("-1.2101") == s2.countUpper("-1.2101"),
			s.countUpper("-1.2013456708090008000000001") == s2.countUpper("-1.2013456708090008000000001"),
			s.countUpper("-243554500") == s2.countUpper("-243554500"),
			s.countUpper("-876754321.12134335") == s2.countUpper("-876754321.12134335"),
			s.countUpper("-5944.95999") == s2.countUpper("-5944.95999"),
			s.countUpper("1.23456078900000000000091") == s2.countUpper("1.23456078900000000000091"),
			s.countUpper("000.00000000009") == s2.countUpper("000.00000000009"),
			s.countUpper("-41.0000001") == s2.countUpper("-41.0000001"),
			s.countUpper("1.234560578900000000001") == s2.countUpper("1.234560578900000000001"),
			s.countUpper("-87456542121.12345") == s2.countUpper("-87456542121.12345"),
			s.countUpper("-24341") == s2.countUpper("-24341"),
			s.countUpper("1.234560789000000000000091") == s2.countUpper("1.234560789000000000000091"),
			s.countUpper("-1.23030567890000000001") == s2.countUpper("-1.23030567890000000001"),
			s.countUpper("1.2345060578900000000001") == s2.countUpper("1.2345060578900000000001"),
			s.countUpper("-1.2013435678900000000001") == s2.countUpper("-1.2013435678900000000001"),
			s.countUpper("-1.230305678890000000001") == s2.countUpper("-1.230305678890000000001"),
			s.countUpper("1.234500000") == s2.countUpper("1.234500000"),
			s.countUpper("-1.23900000000001") == s2.countUpper("-1.23900000000001"),
			s.countUpper("-875654221.123445") == s2.countUpper("-875654221.123445"),
			s.countUpper("-1.2341050678900000000001") == s2.countUpper("-1.2341050678900000000001"),
			s.countUpper("-8890090000000013435") == s2.countUpper("-8890090000000013435"),
			s.countUpper("-1.201394567890") == s2.countUpper("-1.201394567890"),
			s.countUpper("-1.2021345678900000000000000000001") == s2.countUpper("-1.2021345678900000000000000000001")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test12()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("1.23457890000000001") == s2.countUpper("1.23457890000000001"),
			s.countUpper("-1.2034567289") == s2.countUpper("-1.2034567289"),
			s.countUpper("-876543211.121345") == s2.countUpper("-876543211.121345"),
			s.countUpper("1.23435678900000000001") == s2.countUpper("1.23435678900000000001"),
			s.countUpper("-1.230405670001") == s2.countUpper("-1.230405670001"),
			s.countUpper("-5000054.99999") == s2.countUpper("-5000054.99999"),
			s.countUpper("-872654321.121345") == s2.countUpper("-872654321.121345"),
			s.countUpper("-1.203456728890000000001") == s2.countUpper("-1.203456728890000000001"),
			s.countUpper("-1.2013645678900000000001") == s2.countUpper("-1.2013645678900000000001"),
			s.countUpper("-88990090000000013435") == s2.countUpper("-88990090000000013435"),
			s.countUpper("-2222324") == s2.countUpper("-2222324"),
			s.countUpper("-5941.23450000095999") == s2.countUpper("-5941.23450000095999"),
			s.countUpper("1.2304567890000000901") == s2.countUpper("1.2304567890000000901"),
			s.countUpper("-13.234056789000000000001") == s2.countUpper("-13.234056789000000000001"),
			s.countUpper("01.23456078900000000") == s2.countUpper("01.23456078900000000"),
			s.countUpper("-45554.59") == s2.countUpper("-45554.59"),
			s.countUpper("12678.85432") == s2.countUpper("12678.85432"),
			s.countUpper("-2312678.5432511334") == s2.countUpper("-2312678.5432511334"),
			s.countUpper("-1.20345678900000000001") == s2.countUpper("-1.20345678900000000001"),
			s.countUpper("-88900900080000013435") == s2.countUpper("-88900900080000013435"),
			s.countUpper("-2424345") == s2.countUpper("-2424345"),
			s.countUpper("-1.2134560789000000000010000000001") == s2.countUpper("-1.2134560789000000000010000000001"),
			s.countUpper("0000000") == s2.countUpper("0000000"),
			s.countUpper("000001.234560789000000000000911") == s2.countUpper("000001.234560789000000000000911"),
			s.countUpper("-454.99") == s2.countUpper("-454.99"),
			s.countUpper("-1.23456001") == s2.countUpper("-1.23456001"),
			s.countUpper("-871.12345") == s2.countUpper("-871.12345"),
			s.countUpper("1.234560789000001") == s2.countUpper("1.234560789000001"),
			s.countUpper("-1.234560789001000000001000007600001") == s2.countUpper("-1.234560789001000000001000007600001"),
			s.countUpper("-1.23030456789000000001") == s2.countUpper("-1.23030456789000000001"),
			s.countUpper("-8765421.122345") == s2.countUpper("-8765421.122345"),
			s.countUpper("-1.201345678909000000000001") == s2.countUpper("-1.201345678909000000000001"),
			s.countUpper("-812345") == s2.countUpper("-812345"),
			s.countUpper("-1.203045607890000000001") == s2.countUpper("-1.203045607890000000001"),
			s.countUpper("-8776654321.12345") == s2.countUpper("-8776654321.12345"),
			s.countUpper("-594.9999") == s2.countUpper("-594.9999"),
			s.countUpper("3456789000000000001") == s2.countUpper("3456789000000000001"),
			s.countUpper("-001") == s2.countUpper("-001"),
			s.countUpper("-594.9") == s2.countUpper("-594.9"),
			s.countUpper("-876654321.142345") == s2.countUpper("-876654321.142345"),
			s.countUpper("-2435544500") == s2.countUpper("-2435544500"),
			s.countUpper("-1.23456078900000001") == s2.countUpper("-1.23456078900000001"),
			s.countUpper("9999999") == s2.countUpper("9999999"),
			s.countUpper("-871.125") == s2.countUpper("-871.125"),
			s.countUpper("-21.234567890000000003") == s2.countUpper("-21.234567890000000003"),
			s.countUpper("-24355450099.9999") == s2.countUpper("-24355450099.9999"),
			s.countUpper("-8765443241.12345") == s2.countUpper("-8765443241.12345"),
			s.countUpper("-8766543821.142345") == s2.countUpper("-8766543821.142345"),
			s.countUpper("-1.2013456789000000000000091") == s2.countUpper("-1.2013456789000000000000091"),
			s.countUpper("-5944.959999") == s2.countUpper("-5944.959999")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test13()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("1.2345300000") == s2.countUpper("1.2345300000"),
			s.countUpper("-11.2343055670001") == s2.countUpper("-11.2343055670001"),
			s.countUpper("-1.2034560728900000000401") == s2.countUpper("-1.2034560728900000000401"),
			s.countUpper("61.23435678900000000001") == s2.countUpper("61.23435678900000000001"),
			s.countUpper("-1.20134569078900000300") == s2.countUpper("-1.20134569078900000300"),
			s.countUpper("-1.2034567248900005000001") == s2.countUpper("-1.2034567248900005000001"),
			s.countUpper("999999") == s2.countUpper("999999"),
			s.countUpper("-0304567089000000901") == s2.countUpper("-0304567089000000901"),
			s.countUpper("-234123455678.54321") == s2.countUpper("-234123455678.54321"),
			s.countUpper("-1.20345672890000000000001") == s2.countUpper("-1.20345672890000000000001"),
			s.countUpper("012678.543210") == s2.countUpper("012678.543210"),
			s.countUpper("-1.203456789000000100001") == s2.countUpper("-1.203456789000000100001"),
			s.countUpper("-1.2034567248900000000001") == s2.countUpper("-1.2034567248900000000001"),
			s.countUpper("00.000000000009") == s2.countUpper("00.000000000009"),
			s.countUpper("-455554.59") == s2.countUpper("-455554.59"),
			s.countUpper("-876654342345") == s2.countUpper("-876654342345"),
			s.countUpper("-29999934") == s2.countUpper("-29999934"),
			s.countUpper("-244") == s2.countUpper("-244"),
			s.countUpper("-11.234305567004301") == s2.countUpper("-11.234305567004301"),
			s.countUpper("-1.234000000000000001") == s2.countUpper("-1.234000000000000001"),
			s.countUpper("-876543211.1215") == s2.countUpper("-876543211.1215"),
			s.countUpper("-1.201394567890000000000") == s2.countUpper("-1.201394567890000000000"),
			s.countUpper("0.00000010001") == s2.countUpper("0.00000010001"),
			s.countUpper("-1.201394567890000000050001") == s2.countUpper("-1.201394567890000000050001"),
			s.countUpper("-23126578.54325134") == s2.countUpper("-23126578.54325134"),
			s.countUpper("1234566178.54321") == s2.countUpper("1234566178.54321"),
			s.countUpper("-1.2013945678900000000050001") == s2.countUpper("-1.2013945678900000000050001"),
			s.countUpper("1234566781.543221") == s2.countUpper("1234566781.543221"),
			s.countUpper("-5944.995999") == s2.countUpper("-5944.995999"),
			s.countUpper("0000000001.2345607890000000001") == s2.countUpper("0000000001.2345607890000000001"),
			s.countUpper("991.23453000009999999") == s2.countUpper("991.23453000009999999"),
			s.countUpper("-000052") == s2.countUpper("-000052"),
			s.countUpper("4512345678.54321") == s2.countUpper("4512345678.54321"),
			s.countUpper("-82354123645") == s2.countUpper("-82354123645"),
			s.countUpper("1.23045678900000901") == s2.countUpper("1.23045678900000901"),
			s.countUpper("-594.99949") == s2.countUpper("-594.99949"),
			s.countUpper("-10.0000") == s2.countUpper("-10.0000"),
			s.countUpper("-23126781.543251334") == s2.countUpper("-23126781.543251334"),
			s.countUpper("-1.2013456789090000000900001") == s2.countUpper("-1.2013456789090000000900001"),
			s.countUpper("-1.23141050678900000000001") == s2.countUpper("-1.23141050678900000000001"),
			s.countUpper("-45.59") == s2.countUpper("-45.59"),
			s.countUpper("54.9") == s2.countUpper("54.9"),
			s.countUpper("00000") == s2.countUpper("00000"),
			s.countUpper("-1.2011") == s2.countUpper("-1.2011"),
			s.countUpper("-234123456728.54321") == s2.countUpper("-234123456728.54321"),
			s.countUpper("-22312678.543251334") == s2.countUpper("-22312678.543251334"),
			s.countUpper("-5954.9999") == s2.countUpper("-5954.9999"),
			s.countUpper("0.0009") == s2.countUpper("0.0009"),
			s.countUpper("-991.23453000009999999001") == s2.countUpper("-991.23453000009999999001"),
			s.countUpper("-1.21345607890000000000100000000011") == s2.countUpper("-1.21345607890000000000100000000011")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test14()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.countUpper("-1.201345670809000000000999999001") == s2.countUpper("-1.201345670809000000000999999001"),
			s.countUpper("100901") == s2.countUpper("100901"),
			s.countUpper("1.2304567890000000001") == s2.countUpper("1.2304567890000000001"),
			s.countUpper("1.23400091") == s2.countUpper("1.23400091"),
			s.countUpper("123456378.54321") == s2.countUpper("123456378.54321"),
			s.countUpper("-1.203045670890000000001") == s2.countUpper("-1.203045670890000000001"),
			s.countUpper("-1.2013456750809000000000001") == s2.countUpper("-1.2013456750809000000000001"),
			s.countUpper("-1.2034567890") == s2.countUpper("-1.2034567890"),
			s.countUpper("-1.2034567289000000000401") == s2.countUpper("-1.2034567289000000000401"),
			s.countUpper("-1.2345678900000000001") == s2.countUpper("-1.2345678900000000001")
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
		test14();
	}
}
