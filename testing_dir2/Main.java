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
			s.strlen("Hello, World!") == s2.strlen("Hello, World!"),
			s.strlen("12345") == s2.strlen("12345"),
			s.strlen(" ") == s2.strlen(" "),
			s.strlen("This is a long string that has many characters in it") == s2.strlen("This is a long string that has many characters in it"),
			s.strlen("abcdefghijklmnopqrstuvwxyz") == s2.strlen("abcdefghijklmnopqrstuvwxyz"),
			s.strlen("Testing testing 123") == s2.strlen("Testing testing 123"),
			s.strlen("The quick brown fox jumps over the lazy dog") == s2.strlen("The quick brown fox jumps over the lazy dog"),
			s.strlen("one\\ntwo\\nthree\\nfour\\nfive") == s2.strlen("one\\ntwo\\nthree\\nfour\\nfive"),
			s.strlen("1234567890") == s2.strlen("1234567890"),
			s.strlen("This string has a \\n newline character") == s2.strlen("This string has a \\n newline character"),
			s.strlen("one\\ntwo\\nthree\\nf\\nfoive") == s2.strlen("one\\ntwo\\nthree\\nf\\nfoive"),
			s.strlen("The quick brown fox jumps overq the lazy dog") == s2.strlen("The quick brown fox jumps overq the lazy dog"),
			s.strlen("abcdefgjklmnopqrstuvwxyz") == s2.strlen("abcdefgjklmnopqrstuvwxyz"),
			s.strlen("three\\nfour\\nfive") == s2.strlen("three\\nfour\\nfive"),
			s.strlen(" This striThis is a long string that has many characters in itng has a \\n newline character") == s2.strlen(" This striThis is a long string that has many characters in itng has a \\n newline character"),
			s.strlen("") == s2.strlen(""),
			s.strlen("The quick brown fox jumps over the lazy This striThis is a long string that has many characters in itng has a \\n newline character dog") == s2.strlen("The quick brown fox jumps over the lazy This striThis is a long string that has many characters in itng has a \\n newline character dog"),
			s.strlen("1234 This striThis is a long string that has many characters in itng has a \\n newline character5") == s2.strlen("1234 This striThis is a long string that has many characters in itng has a \\n newline character5"),
			s.strlen("The quick brown fox jumps over the lazy This striThis is aaracter dog") == s2.strlen("The quick brown fox jumps over the lazy This striThis is aaracter dog"),
			s.strlen("one\\ntwot\\nthree\\nfour\\nfive") == s2.strlen("one\\ntwot\\nthree\\nfour\\nfive"),
			s.strlen("11234567890") == s2.strlen("11234567890"),
			s.strlen("one\\ntwot\\nthrThis is a long string that has many characters in itee\\nfour\\nfive") == s2.strlen("one\\ntwot\\nthrThis is a long string that has many characters in itee\\nfour\\nfive"),
			s.strlen("The quick brown f ox jumps over the lazy dog") == s2.strlen("The quick brown f ox jumps over the lazy dog"),
			s.strlen("122345") == s2.strlen("122345"),
			s.strlen("Testing testingone\\ntwot\\nthrThis is a long string that has many characters in itee\\nfour\\nfive 123") == s2.strlen("Testing testingone\\ntwot\\nthrThis is a long string that has many characters in itee\\nfour\\nfive 123"),
			s.strlen("one\\ntwot\\nthrThis is a long string thtat has many characters in itee\\nfour\\nfive") == s2.strlen("one\\ntwot\\nthrThis is a long string thtat has many characters in itee\\nfour\\nfive"),
			s.strlen("123345") == s2.strlen("123345"),
			s.strlen("The quick brown fox jumps over the lazy Thisthree\\nfour\\nfiveracter dog") == s2.strlen("The quick brown fox jumps over the lazy Thisthree\\nfour\\nfiveracter dog"),
			s.strlen("GNDKQyadEb") == s2.strlen("GNDKQyadEb"),
			s.strlen("Hello, Woorld!") == s2.strlen("Hello, Woorld!"),
			s.strlen("of\\nfoive") == s2.strlen("of\\nfoive"),
			s.strlen("The quick brown fox jumps overq theHello, World! lazy dog") == s2.strlen("The quick brown fox jumps overq theHello, World! lazy dog"),
			s.strlen("M") == s2.strlen("M"),
			s.strlen("NEvG") == s2.strlen("NEvG"),
			s.strlen("Hello, Woorlod!") == s2.strlen("Hello, Woorlod!"),
			s.strlen("thrieeThe quick brown fox jumps overq the lazy dog\\nfour\\nfive") == s2.strlen("thrieeThe quick brown fox jumps overq the lazy dog\\nfour\\nfive"),
			s.strlen("one\\ntwot\\nthree\\nfour\\nfiv") == s2.strlen("one\\ntwot\\nthree\\nfour\\nfiv"),
			s.strlen("abcdefghijklmnopq1234 This striThis is a long string that has many characters in itng has a \\n newline character5rstuvwxyz") == s2.strlen("abcdefghijklmnopq1234 This striThis is a long string that has many characters in itng has a \\n newline character5rstuvwxyz"),
			s.strlen("Hello, Woo12345rld!") == s2.strlen("Hello, Woo12345rld!"),
			s.strlen("one\\ntwot This striThis is a long streing that has many characters in itng has a \\n newline character\\nthree\\nfour\\nfive") == s2.strlen("one\\ntwot This striThis is a long streing that has many characters in itng has a \\n newline character\\nthree\\nfour\\nfive"),
			s.strlen(" This striThis is a long string that has many characters in itng has a \\n neawline character") == s2.strlen(" This striThis is a long string that has many characters in itng has a \\n neawline character"),
			s.strlen("1223545") == s2.strlen("1223545"),
			s.strlen("one\\ntwota\\nthrThis is a long string that has many characters in itee\\nfour\\nfive") == s2.strlen("one\\ntwota\\nthrThis is a long string that has many characters in itee\\nfour\\nfive"),
			s.strlen("The quick brzown fox jumps over the leazy Thisis is aaracter dog") == s2.strlen("The quick brzown fox jumps over the leazy Thisis is aaracter dog"),
			s.strlen("1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5") == s2.strlen("1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5"),
			s.strlen("TestiTng testing 123") == s2.strlen("TestiTng testing 123"),
			s.strlen("GNDThis string has a \\n newline characterdEb") == s2.strlen("GNDThis string has a \\n newline characterdEb"),
			s.strlen("The quick brzown fox sjumps over the leazy Thisis is aaracter dog") == s2.strlen("The quick brzown fox sjumps over the leazy Thisis is aaracter dog"),
			s.strlen("G1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5NDKQyadEb") == s2.strlen("G1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5NDKQyadEb"),
			s.strlen("The quick brown fox jumps over theThe quick brown fox jumps overq the lazy dog lazy Thisthree\\nfour\\nfiveracter dog") == s2.strlen("The quick brown fox jumps over theThe quick brown fox jumps overq the lazy dog lazy Thisthree\\nfour\\nfiveracter dog")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test1()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("G1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5NDKThe quick brown fox jumps over theThe quick brown fox jumps overq the lazy dog lazy Thisthree\\nfour\\nfiveracter dogQyadEb") == s2.strlen("G1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5NDKThe quick brown fox jumps over theThe quick brown fox jumps overq the lazy dog lazy Thisthree\\nfour\\nfiveracter dogQyadEb"),
			s.strlen("oef\\nffoive") == s2.strlen("oef\\nffoive"),
			s.strlen("one\\ntwot\\nthrThis is a long string that has many characters in itee\\nfoour\\nfive") == s2.strlen("one\\ntwot\\nthrThis is a long string that has many characters in itee\\nfoour\\nfive"),
			s.strlen("of\\nfoivfe") == s2.strlen("of\\nfoivfe"),
			s.strlen("Testing te stingone\\ntwot\\nthrThis is a long string that has many characters in itee\\nfour\\nfive 123") == s2.strlen("Testing te stingone\\ntwot\\nthrThis is a long string that has many characters in itee\\nfour\\nfive 123"),
			s.strlen("Hello, WoG1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5NDKThe quick brown fox jumps over theThe quick brown fox jumps overq the lazy dog lazby Thisthree\\nfour\\nfiveracter dogQyadEborlod!") == s2.strlen("Hello, WoG1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5NDKThe quick brown fox jumps over theThe quick brown fox jumps overq the lazy dog lazby Thisthree\\nfour\\nfiveracter dogQyadEborlod!"),
			s.strlen("Hello,The quick brown fox jumps over the lazy Thisthree\\nfour\\nfiveracter dog Woo12345rld!") == s2.strlen("Hello,The quick brown fox jumps over the lazy Thisthree\\nfour\\nfiveracter dog Woo12345rld!"),
			s.strlen("Hello, WoG1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5NDKThe quick brown fox jumps over theThe quick by Thisthree\\nfour\\nfiveracter dogQyadEborlod!") == s2.strlen("Hello, WoG1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5NDKThe quick brown fox jumps over theThe quick by Thisthree\\nfour\\nfiveracter dogQyadEborlod!"),
			s.strlen("off\\nfoiivfe") == s2.strlen("off\\nfoiivfe"),
			s.strlen("912345667890") == s2.strlen("912345667890"),
			s.strlen("abcdefgjklmnopqrstuvwxyzive") == s2.strlen("abcdefgjklmnopqrstuvwxyzive"),
			s.strlen("The quick brown fox jumps over the lazy This striThis is aaracter dogM") == s2.strlen("The quick brown fox jumps over the lazy This striThis is aaracter dogM"),
			s.strlen("Hello, WoG1234 This sitriThis is a long string that has many characters in itng h as a \\n newline character5NDKThe quick brown fox jumps over theThe quick brown fox jumps overq the lazy dog lazby Thisthree\\nfour\\nfiveracter dogQyadEborlod!") == s2.strlen("Hello, WoG1234 This sitriThis is a long string that has many characters in itng h as a \\n newline character5NDKThe quick brown fox jumps over theThe quick brown fox jumps overq the lazy dog lazby Thisthree\\nfour\\nfiveracter dogQyadEborlod!"),
			s.strlen("The quick brown f ox jumps over the lazyg") == s2.strlen("The quick brown f ox jumps over the lazyg"),
			s.strlen("one\\ntwot\\nthrThis is a long string that has  many characters in itee\\nfour\\nfive") == s2.strlen("one\\ntwot\\nthrThis is a long string that has  many characters in itee\\nfour\\nfive"),
			s.strlen("one\\n\\ntwot\\nthrThis is a long string that has many characters in itee\\nfoour\\nfive") == s2.strlen("one\\n\\ntwot\\nthrThis is a long string that has many characters in itee\\nfoour\\nfive"),
			s.strlen("thrieeThe quick brown f ox jumps over the lazy dogThe quick brown fox jumps overq the lazy dog\\nfour\\nfive") == s2.strlen("thrieeThe quick brown f ox jumps over the lazy dogThe quick brown fox jumps overq the lazy dog\\nfour\\nfive"),
			s.strlen("G1The quick brown f ox jumps over the lazy dog234  has a \\n newline character5NDKQyadEb") == s2.strlen("G1The quick brown f ox jumps over the lazy dog234  has a \\n newline character5NDKQyadEb"),
			s.strlen("TheHello,The quick brown fox jumps over the lazy Thisthree\\nfour\\nfiveracter dog Woo12345rld! quick broThis string Thas a \\n newline characterwn fox jumps over the lazy Thisthree\\nfour\\nfiveracter dog") == s2.strlen("TheHello,The quick brown fox jumps over the lazy Thisthree\\nfour\\nfiveracter dog Woo12345rld! quick broThis string Thas a \\n newline characterwn fox jumps over the lazy Thisthree\\nfour\\nfiveracter dog"),
			s.strlen("off\\nfoivife") == s2.strlen("off\\nfoivife"),
			s.strlen("three\\nefour\\noff\\nfoiivfe") == s2.strlen("three\\nefour\\noff\\nfoiivfe"),
			s.strlen("Test1iTng testing 123") == s2.strlen("Test1iTng testing 123"),
			s.strlen("one\\ntwota\\nthrThis is a long string that has many chone\\ntwot\\nthrThis is a long string that has  many characters in itee\\nfour\\nfivearacters in itee\\nfour\\nfive") == s2.strlen("one\\ntwota\\nthrThis is a long string that has many chone\\ntwot\\nthrThis is a long string that has  many characters in itee\\nfour\\nfivearacters in itee\\nfour\\nfive"),
			s.strlen("TheHello,The quick brown fox jumps over the lazy Thisthree\\nfour\\nfiveracter dog Woo12345rld! quick broThis string Thas a \\n newline characterwn fox jumps over theone\\ntwota\\nthrThis is a long string that has many characters in itee\\nfour\\nfive dog") == s2.strlen("TheHello,The quick brown fox jumps over the lazy Thisthree\\nfour\\nfiveracter dog Woo12345rld! quick broThis string Thas a \\n newline characterwn fox jumps over theone\\ntwota\\nthrThis is a long string that has many characters in itee\\nfour\\nfive dog"),
			s.strlen("thrieeThe quick brown f ox jumps over the lazy dogThe quick brown fox jumps overq the lazy dog\\nfour\\nfive ") == s2.strlen("thrieeThe quick brown f ox jumps over the lazy dogThe quick brown fox jumps overq the lazy dog\\nfour\\nfive "),
			s.strlen("oene") == s2.strlen("oene"),
			s.strlen("off\\nabcdefgjklmnopqrstuvwxyzfoivife") == s2.strlen("off\\nabcdefgjklmnopqrstuvwxyzfoivife"),
			s.strlen("The quick brown f ox jumps over the lazy") == s2.strlen("The quick brown f ox jumps over the lazy"),
			s.strlen("abcdefghijklTest1iTng testing 123mnopq1234 This striThis is a long string that has many characters in itnghas a \\n newline character5rstuvwxyz") == s2.strlen("abcdefghijklTest1iTng testing 123mnopq1234 This striThis is a long string that has many characters in itnghas a \\n newline character5rstuvwxyz"),
			s.strlen("abcdeflghijklmnopqrstuvwxyz") == s2.strlen("abcdeflghijklmnopqrstuvwxyz"),
			s.strlen("1o, Woorld!890") == s2.strlen("1o, Woorld!890"),
			s.strlen("12333345") == s2.strlen("12333345"),
			s.strlen("1122345") == s2.strlen("1122345"),
			s.strlen("one\\ntwota\\nthrThis is a long string that has many characters ien itee\\nfour\\nfive") == s2.strlen("one\\ntwota\\nthrThis is a long string that has many characters ien itee\\nfour\\nfive"),
			s.strlen("Hello, W123345orld!") == s2.strlen("Hello, W123345orld!"),
			s.strlen("one\\ntwo\\nthrfoive") == s2.strlen("one\\ntwo\\nthrfoive"),
			s.strlen("one\\ntwot\\nthrThis is a long string that has  many characterns in itee\\nfour\\nfive") == s2.strlen("one\\ntwot\\nthrThis is a long string that has  many characterns in itee\\nfour\\nfive"),
			s.strlen("one\\ntwotaa\\nthrThis is a long string that has many characters ien itee\\n1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5four\\nfive") == s2.strlen("one\\ntwotaa\\nthrThis is a long string that has many characters ien itee\\n1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5four\\nfive"),
			s.strlen("The quick brzown fox sjumps over the leazy Thisis is aaThe quick brown fox jumps overq theHello, World! lazy dogracter dog") == s2.strlen("The quick brzown fox sjumps over the leazy Thisis is aaThe quick brown fox jumps overq theHello, World! lazy dogracter dog"),
			s.strlen("MThe quick brown fox jumps over the lazy This striThis is aaracter dogM") == s2.strlen("MThe quick brown fox jumps over the lazy This striThis is aaracter dogM"),
			s.strlen("The quick brzown fox jumps over the leazy Thisis is aaracter Hello, Woorld!dog") == s2.strlen("The quick brzown fox jumps over the leazy Thisis is aaracter Hello, Woorld!dog"),
			s.strlen("1234 This sitriThis is a long string that has many character12345s in itng has a \\n newline character5") == s2.strlen("1234 This sitriThis is a long string that has many character12345s in itng has a \\n newline character5"),
			s.strlen("1234 This sitriThis is a long string that has many characters in itng has a \\n neThe quick brown f ox jumps over the lazygwline character5") == s2.strlen("1234 This sitriThis is a long string that has many characters in itng has a \\n neThe quick brown f ox jumps over the lazygwline character5"),
			s.strlen("912345667890The quick brown fox jumps over the lazy This striThis is aaracter dogM") == s2.strlen("912345667890The quick brown fox jumps over the lazy This striThis is aaracter dogM"),
			s.strlen("Hellone\\ntwot\\nthree\\nfour\\nfivo, WoG1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5NDKThe quirck brown fox jumps over theThe quick by Thisthree\\nfour\\nfiveracter dogQyadEborlod!") == s2.strlen("Hellone\\ntwot\\nthree\\nfour\\nfivo, WoG1234 This sitriThis is a long string that has many characters in itng has a \\n newline character5NDKThe quirck brown fox jumps over theThe quick by Thisthree\\nfour\\nfiveracter dogQyadEborlod!"),
			s.strlen("The quick brown fox11234567890 jumps over the lazy This striThis is aaracter dog") == s2.strlen("The quick brown fox11234567890 jumps over the lazy This striThis is aaracter dog"),
			s.strlen("one\\ntwota\\nthrThis is a long string that has many characters iThe quick bis striThis is aaracter dogMen itee\\nfour\\nfive") == s2.strlen("one\\ntwota\\nthrThis is a long string that has many characters iThe quick bis striThis is aaracter dogMen itee\\nfour\\nfive"),
			s.strlen("The quick brown fox jumps over theThe quick brown fox jxumps overq the lazy dog lazy Thisthree\\nfour\\nfiveracter dog") == s2.strlen("The quick brown fox jumps over theThe quick brown fox jxumps overq the lazy dog lazy Thisthree\\nfour\\nfiveracter dog"),
			s.strlen("one\\ntwot\\nthrThis is a long string that has many characters in itee\\nfour\\nfiveabcdefghijklmnopqrstuvwxyz") == s2.strlen("one\\ntwot\\nthrThis is a long string that has many characters in itee\\nfour\\nfiveabcdefghijklmnopqrstuvwxyz"),
			s.strlen("Testing te stingone\\ntwot\\nthrThis is a long strinThe quick brown fox jumps over theThe quick brown fox jumps overq the lazy dog lazy Thisthree\\nfour\\nfiveracter dogg that has many characters in itee\\nfour\\nfive 123") == s2.strlen("Testing te stingone\\ntwot\\nthrThis is a long strinThe quick brown fox jumps over theThe quick brown fox jumps overq the lazy dog lazy Thisthree\\nfour\\nfiveracter dogg that has many characters in itee\\nfour\\nfive 123")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test2()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("  ") == s2.strlen("  "),
			s.strlen("\t") == s2.strlen("\t"),
			s.strlen("\\n") == s2.strlen("\\n"),
			s.strlen("\\r") == s2.strlen("\\r"),
			s.strlen("àèìòùáéíóúýâêîôûãñõäëïöüÿç") == s2.strlen("àèìòùáéíóúýâêîôûãñõäëïöüÿç"),
			s.strlen("This is a sample string to test the function") == s2.strlen("This is a sample string to test the function"),
			s.strlen("The Quick Brown Fox Jumps Over The Lazy Dog") == s2.strlen("The Quick Brown Fox Jumps Over The Lazy Dog"),
			s.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !n 1t") == s2.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !n 1t"),
			s.strlen("          ") == s2.strlen("          "),
			s.strlen("   \\n\\n   ") == s2.strlen("   \\n\\n   "),
			s.strlen("Quick") == s2.strlen("Quick"),
			s.strlen("   ") == s2.strlen("   "),
			s.strlen("           ") == s2.strlen("           "),
			s.strlen("           àèìòùáéíóúýâêîôûãñõäëïöüÿç") == s2.strlen("           àèìòùáéíóúýâêîôûãñõäëïöüÿç"),
			s.strlen("      ") == s2.strlen("      "),
			s.strlen("w1th") == s2.strlen("w1th"),
			s.strlen("Th!") == s2.strlen("Th!"),
			s.strlen("   \\n\\n 1s  ") == s2.strlen("   \\n\\n 1s  "),
			s.strlen("Jumps") == s2.strlen("Jumps"),
			s.strlen("Fox") == s2.strlen("Fox"),
			s.strlen("1t") == s2.strlen("1t"),
			s.strlen("    This is a sample string to test the function          ") == s2.strlen("    This is a sample string to test the function          "),
			s.strlen("Th!s 1s 4 str1ng wtest5ymb0ls !n 1t") == s2.strlen("Th!s 1s 4 str1ng wtest5ymb0ls !n 1t"),
			s.strlen("    This is a sampleto string to test the function          ") == s2.strlen("    This is a sampleto string to test the function          "),
			s.strlen("Qukick") == s2.strlen("Qukick"),
			s.strlen("    \t ") == s2.strlen("    \t "),
			s.strlen("            ") == s2.strlen("            "),
			s.strlen("   \\n\\n  string") == s2.strlen("   \\n\\n  string"),
			s.strlen("Tish!") == s2.strlen("Tish!"),
			s.strlen("Th!s 1s 4 str1ng wtest5ymb0ls !n 1t\\n") == s2.strlen("Th!s 1s 4 str1ng wtest5ymb0ls !n 1t\\n"),
			s.strlen("ps") == s2.strlen("ps"),
			s.strlen("a") == s2.strlen("a"),
			s.strlen("Dog") == s2.strlen("Dog"),
			s.strlen("Tish!           ") == s2.strlen("Tish!           "),
			s.strlen("4") == s2.strlen("4"),
			s.strlen("is") == s2.strlen("is"),
			s.strlen("Jummtops") == s2.strlen("Jummtops"),
			s.strlen("!n") == s2.strlen("!n"),
			s.strlen("Tish!           4") == s2.strlen("Tish!           4"),
			s.strlen("yLazy") == s2.strlen("yLazy"),
			s.strlen(" ã          àèìòùáéíóúýâêîôûãñõäëïöüÿç") == s2.strlen(" ã          àèìòùáéíóúýâêîôûãñõäëïöüÿç"),
			s.strlen("LqNCZA") == s2.strlen("LqNCZA"),
			s.strlen("Over") == s2.strlen("Over"),
			s.strlen("hyNcJH") == s2.strlen("hyNcJH"),
			s.strlen("QFoxukick") == s2.strlen("QFoxukick"),
			s.strlen("Fo    This is a sampleto string to test the function  n        x") == s2.strlen("Fo    This is a sampleto string to test the function  n        x"),
			s.strlen("!nn") == s2.strlen("!nn"),
			s.strlen("\t\t") == s2.strlen("\t\t"),
			s.strlen("whyNcJH1th") == s2.strlen("whyNcJH1th"),
			s.strlen("TheTe") == s2.strlen("TheTe")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test3()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("    This is a sampl           eto string to test the func tion          ") == s2.strlen("    This is a sampl           eto string to test the func tion          "),
			s.strlen("     ã          àèìòùáéíóúýâêîôûãñõäëïöüÿç  ") == s2.strlen("     ã          àèìòùáéíóúýâêîôûãñõäëïöüÿç  "),
			s.strlen("QFoQxukick") == s2.strlen("QFoQxukick"),
			s.strlen("tn") == s2.strlen("tn"),
			s.strlen("Th!s 1s 4 str1ng wtest5ymb0ls !nsampleto 1t\\n") == s2.strlen("Th!s 1s 4 str1ng wtest5ymb0ls !nsampleto 1t\\n"),
			s.strlen("iw1th") == s2.strlen("iw1th"),
			s.strlen("x      ") == s2.strlen("x      "),
			s.strlen("Dàèìòù4áéíóúýâêîôûãñõäëïöüÿçgog") == s2.strlen("Dàèìòù4áéíóúýâêîôûãñõäëïöüÿçgog"),
			s.strlen("    This is a sample    \\n\\n 1s  string to test the functoion          ") == s2.strlen("    This is a sample    \\n\\n 1s  string to test the functoion          "),
			s.strlen("isJumps") == s2.strlen("isJumps"),
			s.strlen("function") == s2.strlen("function"),
			s.strlen("func") == s2.strlen("func"),
			s.strlen("Dëàèìòù4áéíóúýâêîôûãñõäëïÿçgog") == s2.strlen("Dëàèìòù4áéíóúýâêîôûãñõäëïÿçgog"),
			s.strlen("sampl") == s2.strlen("sampl"),
			s.strlen("funcc") == s2.strlen("funcc"),
			s.strlen("Lazy") == s2.strlen("Lazy"),
			s.strlen("Th!s 1s 4 str1ng wtest5ymb40ls !n 1t\\n") == s2.strlen("Th!s 1s 4 str1ng wtest5ymb40ls !n 1t\\n"),
			s.strlen("n") == s2.strlen("n"),
			s.strlen("Doo") == s2.strlen("Doo"),
			s.strlen("aOver") == s2.strlen("aOver"),
			s.strlen("Th!s 1s 4 str1ng wtest5ymb0lse !n 1t\\n") == s2.strlen("Th!s 1s 4 str1ng wtest5ymb0lse !n 1t\\n"),
			s.strlen("Dëàèìòùõäëïÿçgog") == s2.strlen("Dëàèìòùõäëïÿçgog"),
			s.strlen("str1ng") == s2.strlen("str1ng"),
			s.strlen("    This is a sampl            eto string to test the func Theon          ") == s2.strlen("    This is a sampl            eto string to test the func Theon          "),
			s.strlen("Tish!           4!n") == s2.strlen("Tish!           4!n"),
			s.strlen("Th!s40ls !n 1t\\n") == s2.strlen("Th!s40ls !n 1t\\n"),
			s.strlen("cQukick") == s2.strlen("cQukick"),
			s.strlen("   \\n\\n     ") == s2.strlen("   \\n\\n     "),
			s.strlen("QuaOverick") == s2.strlen("QuaOverick"),
			s.strlen("Te") == s2.strlen("Te"),
			s.strlen("QFoxuk") == s2.strlen("QFoxuk"),
			s.strlen("Jum5ymb0lsmtops") == s2.strlen("Jum5ymb0lsmtops"),
			s.strlen("Th!s40ls") == s2.strlen("Th!s40ls"),
			s.strlen("   \\n\\n  1s  ") == s2.strlen("   \\n\\n  1s  "),
			s.strlen("funnc") == s2.strlen("funnc"),
			s.strlen("eto") == s2.strlen("eto"),
			s.strlen("    This is a sample string to test the function  i        ") == s2.strlen("    This is a sample string to test the function  i        "),
			s.strlen("sample") == s2.strlen("sample"),
			s.strlen("        functoion   ") == s2.strlen("        functoion   "),
			s.strlen("     ã         ô àèìòùáéíóúýâêîôûãñõäëïöüÿç  ") == s2.strlen("     ã         ô àèìòùáéíóúýâêîôûãñõäëïöüÿç  "),
			s.strlen("Tetn") == s2.strlen("Tetn"),
			s.strlen("mThfGqorZJum5ymb0lsmtops") == s2.strlen("mThfGqorZJum5ymb0lsmtops"),
			s.strlen("   \\n\\nwtest5ymb40ls    ") == s2.strlen("   \\n\\nwtest5ymb40ls    "),
			s.strlen("    This is a sample strinisg to test the function          ") == s2.strlen("    This is a sample strinisg to test the function          "),
			s.strlen("   \\nhyNcJH\\n  string") == s2.strlen("   \\nhyNcJH\\n  string"),
			s.strlen("str1ngsampl") == s2.strlen("str1ngsampl"),
			s.strlen("       ") == s2.strlen("       "),
			s.strlen("   \\n\\nwwtest5ymb40ls    ") == s2.strlen("   \\n\\nwwtest5ymb40ls    "),
			s.strlen("iwTish!1th") == s2.strlen("iwTish!1th"),
			s.strlen("test") == s2.strlen("test")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test4()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("TTetn") == s2.strlen("TTetn"),
			s.strlen("    ") == s2.strlen("    "),
			s.strlen("   \\n\\nwwtes            ls    ") == s2.strlen("   \\n\\nwwtes            ls    "),
			s.strlen("LaàèìòùáéíóúýâêîôûãñõäëïöüÿçQFoQxukyicky") == s2.strlen("LaàèìòùáéíóúýâêîôûãñõäëïöüÿçQFoQxukyicky"),
			s.strlen("ver") == s2.strlen("ver"),
			s.strlen("    4\\n\\n  1s  ") == s2.strlen("    4\\n\\n  1s  "),
			s.strlen("    This is a sample TTetnstrinisg to test the function           ") == s2.strlen("    This is a sample TTetnstrinisg to test the function           "),
			s.strlen("This is a sample string    This is a sampl            eto string to test the func Theon           to test the function") == s2.strlen("This is a sample string    This is a sampl            eto string to test the func Theon           to test the function"),
			s.strlen("tn ã          àèìòùáéíóúýâêîôûãñõäëïöüÿç") == s2.strlen("tn ã          àèìòùáéíóúýâêîôûãñõäëïöüÿç"),
			s.strlen("Tish!          4") == s2.strlen("Tish!          4"),
			s.strlen("strin") == s2.strlen("strin"),
			s.strlen("àèìòùáéíóúýâêîèôûãñõäëïöüÿç") == s2.strlen("àèìòùáéíóúýâêîèôûãñõäëïöüÿç"),
			s.strlen("   \\nhy    This is a sample strinisg to test the fuunction          NcJH\\n  string") == s2.strlen("   \\nhy    This is a sample strinisg to test the fuunction          NcJH\\n  string"),
			s.strlen("funthec") == s2.strlen("funthec"),
			s.strlen("  Tish!           4!n \\n\\n  1s  ") == s2.strlen("  Tish!           4!n \\n\\n  1s  "),
			s.strlen("funtThis is a sample string    This is a sampl            eto string to test the func Theon           to test the functionhec") == s2.strlen("funtThis is a sample string    This is a sampl            eto string to test the func Theon           to test the functionhec"),
			s.strlen("        ") == s2.strlen("        "),
			s.strlen("Th!s1s 1s 4 str1ng w1th 5ymb0ls !n 1t") == s2.strlen("Th!s1s 1s 4 str1ng w1th 5ymb0ls !n 1t"),
			s.strlen("   \\n\\nBrown") == s2.strlen("   \\n\\nBrown"),
			s.strlen("   \\n\\n wwtest5ymb40ls    ") == s2.strlen("   \\n\\n wwtest5ymb40ls    "),
			s.strlen("iis") == s2.strlen("iis"),
			s.strlen("                ã           àèìòùáöüÿç   ") == s2.strlen("                ã           àèìòùáöüÿç   "),
			s.strlen("astr1ngsampl") == s2.strlen("astr1ngsampl"),
			s.strlen("QQFoxuk") == s2.strlen("QQFoxuk"),
			s.strlen("functoion") == s2.strlen("functoion"),
			s.strlen("   \\nTetn\\nBrown") == s2.strlen("   \\nTetn\\nBrown"),
			s.strlen("Th!s40ls !n 1t   \\n\\n wwtest5ymb40ls    \\n") == s2.strlen("Th!s40ls !n 1t   \\n\\n wwtest5ymb40ls    \\n"),
			s.strlen("nFo") == s2.strlen("nFo"),
			s.strlen("The QuiisJumpsck Brown Fox Jg") == s2.strlen("The QuiisJumpsck Brown Fox Jg"),
			s.strlen("Th!s 1s 4 stTheTer1ng wtest5ymb0lse !n 1t\\n") == s2.strlen("Th!s 1s 4 stTheTer1ng wtest5ymb0lse !n 1t\\n"),
			s.strlen("Jum5ymb0lsmfunction") == s2.strlen("Jum5ymb0lsmfunction"),
			s.strlen("iiis") == s2.strlen("iiis"),
			s.strlen("        funthec    ") == s2.strlen("        funthec    "),
			s.strlen("hyNcJ") == s2.strlen("hyNcJ"),
			s.strlen("TTh!s40lsh!s 1s 4 str1ng wtest5ymb0lse !n 1t\\n") == s2.strlen("TTh!s40lsh!s 1s 4 str1ng wtest5ymb0lse !n 1t\\n"),
			s.strlen("    This is a sample string to tea  ") == s2.strlen("    This is a sample string to tea  "),
			s.strlen("fufncc") == s2.strlen("fufncc"),
			s.strlen("p1ss") == s2.strlen("p1ss"),
			s.strlen("wiw1th") == s2.strlen("wiw1th"),
			s.strlen("44") == s2.strlen("44"),
			s.strlen("eeTe") == s2.strlen("eeTe"),
			s.strlen("           àèìòùáéíóúýâêîôiwTish!1thûãñõäëïöüÿç") == s2.strlen("           àèìòùáéíóúýâêîôiwTish!1thûãñõäëïöüÿç"),
			s.strlen("Lazyy") == s2.strlen("Lazyy"),
			s.strlen("This is a sample string    This is a sampl            eto string to test the func Theon       to test the function") == s2.strlen("This is a sample string    This is a sampl            eto string to test the func Theon       to test the function"),
			s.strlen("RLkion") == s2.strlen("RLkion"),
			s.strlen("stricQukickn") == s2.strlen("stricQukickn"),
			s.strlen("funtht") == s2.strlen("funtht"),
			s.strlen("TheyLazyTe") == s2.strlen("TheyLazyTe"),
			s.strlen("   \\nhy    This is a sample strinisg to test the fuunction          NcJH\\n  string4") == s2.strlen("   \\nhy    This is a sample strinisg to test the fuunction          NcJH\\n  string4"),
			s.strlen("i        s") == s2.strlen("i        s")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test5()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("etoo") == s2.strlen("etoo"),
			s.strlen("Th!s 1s 4 str1ng wtest5ymb40ls s!n 1t\\n") == s2.strlen("Th!s 1s 4 str1ng wtest5ymb40ls s!n 1t\\n"),
			s.strlen("FoFxuk") == s2.strlen("FoFxuk"),
			s.strlen("The Quick Brown Fox Jumpe Lazy Dog") == s2.strlen("The Quick Brown Fox Jumpe Lazy Dog"),
			s.strlen("4!n") == s2.strlen("4!n"),
			s.strlen("QuiisJumpsck") == s2.strlen("QuiisJumpsck"),
			s.strlen("This is a sample string    This is a sampl            eto string to LqNCZAtest the func Theon           to test the function") == s2.strlen("This is a sample string    This is a sampl            eto string to LqNCZAtest the func Theon           to test the function"),
			s.strlen("         ") == s2.strlen("         "),
			s.strlen("!") == s2.strlen("!"),
			s.strlen("TT") == s2.strlen("TT"),
			s.strlen("mThftGqorZJum5ymb0lsmtops") == s2.strlen("mThftGqorZJum5ymb0lsmtops"),
			s.strlen("wwtes") == s2.strlen("wwtes"),
			s.strlen("Tis          ") == s2.strlen("Tis          "),
			s.strlen("wtest5ymb40ls") == s2.strlen("wtest5ymb40ls"),
			s.strlen("    This is a sample strintg to test the function          ") == s2.strlen("    This is a sample strintg to test the function          "),
			s.strlen(" àèìòùáéíóúýâêîôiwTish!1thûãñõäëïöüÿç  \\n\\nwtest5ymb40ls    ") == s2.strlen(" àèìòùáéíóúýâêîôiwTish!1thûãñõäëïöüÿç  \\n\\nwtest5ymb40ls    "),
			s.strlen("QFoxukcick") == s2.strlen("QFoxukcick"),
			s.strlen("Tis") == s2.strlen("Tis"),
			s.strlen("fux      ncc") == s2.strlen("fux      ncc"),
			s.strlen("fux") == s2.strlen("fux"),
			s.strlen("YJvcL") == s2.strlen("YJvcL"),
			s.strlen("Qck") == s2.strlen("Qck"),
			s.strlen("TTh!s40lsh!s 1s 4 str1nb0lse !n 1t\\n") == s2.strlen("TTh!s40lsh!s 1s 4 str1nb0lse !n 1t\\n"),
			s.strlen(" Th!s  \\n\\n 1s  ") == s2.strlen(" Th!s  \\n\\n 1s  "),
			s.strlen("    This is a sampl          tothe func tion          ") == s2.strlen("    This is a sampl          tothe func tion          "),
			s.strlen("nn") == s2.strlen("nn"),
			s.strlen("sTh!s4strinisg05ymb0lsls") == s2.strlen("sTh!s4strinisg05ymb0lsls"),
			s.strlen("  Th!s 1s 4 str1ng wtest5ymb0ls !nsampleto 1t\\n") == s2.strlen("  Th!s 1s 4 str1ng wtest5ymb0ls !nsampleto 1t\\n"),
			s.strlen("whyNcJH1thfunnc") == s2.strlen("whyNcJH1thfunnc"),
			s.strlen("why1NcJH1th") == s2.strlen("why1NcJH1th"),
			s.strlen("iisTe") == s2.strlen("iisTe"),
			s.strlen("Th!s40ls !n 1This is a sample string    This is a sampl            eto string to LqNCZAtest the func Theon           to test the functi           àèìòùáéíóúýâêîôûãñõäëïöüÿçnt\\n") == s2.strlen("Th!s40ls !n 1This is a sample string    This is a sampl            eto string to LqNCZAtest the func Theon           to test the functi           àèìòùáéíóúýâêîôûãñõäëïöüÿçnt\\n"),
			s.strlen("stcricQukDogickn") == s2.strlen("stcricQukDogickn"),
			s.strlen("why1N    This is a sampleto string to test the function          cJH1th") == s2.strlen("why1N    This is a sampleto string to test the function          cJH1th"),
			s.strlen("ssps") == s2.strlen("ssps"),
			s.strlen("Th    This is a sample TTetnstrinisg to test the function           !s40ls !n 1t\\n") == s2.strlen("Th    This is a sample TTetnstrinisg to test the function           !s40ls !n 1t\\n"),
			s.strlen("    This irs a sample string to tea  ") == s2.strlen("    This irs a sample string to tea  "),
			s.strlen("fuwhy1N    This is a sampleto string to test the function          cJH1th") == s2.strlen("fuwhy1N    This is a sampleto string to test the function          cJH1th"),
			s.strlen("   \\n\\nwwtes            ls   Th!s 1s 4 str1ng wtest5ymb0ls !n 1t\\n ") == s2.strlen("   \\n\\nwwtes            ls   Th!s 1s 4 str1ng wtest5ymb0ls !n 1t\\n "),
			s.strlen("hy") == s2.strlen("hy"),
			s.strlen("strinisg") == s2.strlen("strinisg"),
			s.strlen("           fux") == s2.strlen("           fux"),
			s.strlen("iiàèìòùáéíóúýâêîèôûãñõäëïöüÿç") == s2.strlen("iiàèìòùáéíóúýâêîèôûãñõäëïöüÿç"),
			s.strlen("   \\nhy    This is a sample strinisg to test the fuunction          NcJH\\n  strin") == s2.strlen("   \\nhy    This is a sample strinisg to test the fuunction          NcJH\\n  strin"),
			s.strlen("why1N") == s2.strlen("why1N"),
			s.strlen("Laàèìòùáéíóúùýâê   \\n\\n  1s  îôûãñõäëïöüÿçQFoQxukyicky") == s2.strlen("Laàèìòùáéíóúùýâê   \\n\\n  1s  îôûãñõäëïöüÿçQFoQxukyicky"),
			s.strlen("   \\nhy    This is a sample strinisg to test othe fuunction          NcJH\\n  string4") == s2.strlen("   \\nhy    This is a sample strinisg to test othe fuunction          NcJH\\n  string4"),
			s.strlen("!s40ls") == s2.strlen("!s40ls"),
			s.strlen("This is a sample string    This is a sampl            eto string to test thLaàèìòùáéíóúùýâê   \\n\\n  1s  îôûãñõäëïöüÿçQFoQxukyickythe function") == s2.strlen("This is a sample string    This is a sampl            eto string to test thLaàèìòùáéíóúùýâê   \\n\\n  1s  îôûãñõäëïöüÿçQFoQxukyickythe function"),
			s.strlen("Theon") == s2.strlen("Theon")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test6()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("t1t") == s2.strlen("t1t"),
			s.strlen(" cJH1th1s 4         funthec    ls !nsampleto 1t\\n") == s2.strlen(" cJH1th1s 4         funthec    ls !nsampleto 1t\\n"),
			s.strlen("Th!s 1s 4 stsr1ng wtest5ymb0ls !n 1t\\n") == s2.strlen("Th!s 1s 4 stsr1ng wtest5ymb0ls !n 1t\\n"),
			s.strlen("Laàèìòùáéíóúùýâê") == s2.strlen("Laàèìòùáéíóúùýâê"),
			s.strlen("       This is a sample string to test the function          1s  ") == s2.strlen("       This is a sample string to test the function          1s  "),
			s.strlen("whyLaàèìòùáéíóúùýâê   \\n\\n  1s  îôûãñõäëïöüÿçQFoQxukyickytothe  \t H1th") == s2.strlen("whyLaàèìòùáéíóúùýâê   \\n\\n  1s  îôûãñõäëïöüÿçQFoQxukyickytothe  \t H1th"),
			s.strlen("wwwtes") == s2.strlen("wwwtes"),
			s.strlen("îôûãñõäëïöüÿçQFoQxukyickythe") == s2.strlen("îôûãñõäëïöüÿçQFoQxukyickythe"),
			s.strlen("   \\n\\nBro   \\n\\n 1s  n") == s2.strlen("   \\n\\nBro   \\n\\n 1s  n"),
			s.strlen("    This is a sample TTetnstrinisg tiiiso test the function           ") == s2.strlen("    This is a sample TTetnstrinisg tiiiso test the function           "),
			s.strlen("\\n\\n") == s2.strlen("\\n\\n"),
			s.strlen("Tishstrintg4") == s2.strlen("Tishstrintg4"),
			s.strlen("why1N    This is a sampleto string to test e function          cJH1th") == s2.strlen("why1N    This is a sampleto string to test e function          cJH1th"),
			s.strlen("sThe Quick Brown Fox Jumps Over The Lazy DogtcricQukDogickn") == s2.strlen("sThe Quick Brown Fox Jumps Over The Lazy DogtcricQukDogickn"),
			s.strlen("    This is a sample sttotherintg to test the function          ") == s2.strlen("    This is a sample sttotherintg to test the function          "),
			s.strlen("to") == s2.strlen("to"),
			s.strlen("tt1t") == s2.strlen("tt1t"),
			s.strlen("RL   \\n\\n  1s  kion") == s2.strlen("RL   \\n\\n  1s  kion"),
			s.strlen("LqNCZAtest") == s2.strlen("LqNCZAtest"),
			s.strlen("ps1ss") == s2.strlen("ps1ss"),
			s.strlen("nF") == s2.strlen("nF"),
			s.strlen("wwhyNcJH1thfunnchy1N") == s2.strlen("wwhyNcJH1thfunnchy1N"),
			s.strlen("àèìòùáöüÿç") == s2.strlen("àèìòùáöüÿç"),
			s.strlen("sJummtops") == s2.strlen("sJummtops"),
			s.strlen("   \\n\\nwwtens            ls   Th!s 1s 4 str1ng wtest5ymb0ls !n 1t\\n ") == s2.strlen("   \\n\\nwwtens            ls   Th!s 1s 4 str1ng wtest5ymb0ls !n 1t\\n "),
			s.strlen("   ã \t ") == s2.strlen("   ã \t "),
			s.strlen("fuunction") == s2.strlen("fuunction"),
			s.strlen("\\n\\nfunc") == s2.strlen("\\n\\nfunc"),
			s.strlen("wtest5ymb0lse") == s2.strlen("wtest5ymb0lse"),
			s.strlen("QQFoTTxuk") == s2.strlen("QQFoTTxuk"),
			s.strlen("sQuiisJsumpsck") == s2.strlen("sQuiisJsumpsck"),
			s.strlen("Brown") == s2.strlen("Brown"),
			s.strlen("FMc") == s2.strlen("FMc"),
			s.strlen("p1sBrown") == s2.strlen("p1sBrown"),
			s.strlen("TlTh!s40lsh!s") == s2.strlen("TlTh!s40lsh!s"),
			s.strlen("This is a sample string    This is a sampl            eto string to test thLaàèìòùáéíóúùýâê   \\n\\n  Bro1s  îôûãñõäëïöüÿçQFoQxukyickythe function") == s2.strlen("This is a sample string    This is a sampl            eto string to test thLaàèìòùáéíóúùýâê   \\n\\n  Bro1s  îôûãñõäëïöüÿçQFoQxukyickythe function"),
			s.strlen("i        s   ") == s2.strlen("i        s   "),
			s.strlen("    This is a sample sttotherintg to test the funcstricQukickntion          ") == s2.strlen("    This is a sample sttotherintg to test the funcstricQukickntion          "),
			s.strlen("  LqNCZAtest") == s2.strlen("  LqNCZAtest"),
			s.strlen("hyisJumpsJ") == s2.strlen("hyisJumpsJ"),
			s.strlen("   \\nhyN cJH\\n  string") == s2.strlen("   \\nhyN cJH\\n  string"),
			s.strlen("OvhyNcJer") == s2.strlen("OvhyNcJer"),
			s.strlen("othe") == s2.strlen("othe"),
			s.strlen("LaàèìòùáéQFoxukcky") == s2.strlen("LaàèìòùáéQFoxukcky"),
			s.strlen("LaàèìòùáéíiisTeóúùýâê") == s2.strlen("LaàèìòùáéíiisTeóúùýâê"),
			s.strlen("fuuni        sction") == s2.strlen("fuuni        sction"),
			s.strlen("fuon") == s2.strlen("fuon"),
			s.strlen("stgrsr1ng") == s2.strlen("stgrsr1ng"),
			s.strlen("Ove    This is a sample    \\n\\n 1s  string to test the functoion          r") == s2.strlen("Ove    This is a sample    \\n\\n 1s  string to test the functoion          r"),
			s.strlen(" Tsh!s   \\n\\n 1s  ") == s2.strlen(" Tsh!s   \\n\\n 1s  ")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test7()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("Jum5ymbops") == s2.strlen("Jum5ymbops"),
			s.strlen("The") == s2.strlen("The"),
			s.strlen("whyLaàèìòùáéíóúùýâê   \\n\\n  1s  îôãñõäëïöüÿçQFoQxukyickytothe  \t H1th") == s2.strlen("whyLaàèìòùáéíóúùýâê   \\n\\n  1s  îôãñõäëïöüÿçQFoQxukyickytothe  \t H1th"),
			s.strlen("tiiiiso") == s2.strlen("tiiiiso"),
			s.strlen("pFomThfGqorZJum5ymb0lsmtopss") == s2.strlen("pFomThfGqorZJum5ymb0lsmtopss"),
			s.strlen("LqqNCZA") == s2.strlen("LqqNCZA"),
			s.strlen("ncc") == s2.strlen("ncc"),
			s.strlen("Tishstrintgi        s4") == s2.strlen("Tishstrintgi        s4"),
			s.strlen("!ncnncc") == s2.strlen("!ncnncc"),
			s.strlen("string") == s2.strlen("string"),
			s.strlen("   \\n   \\n\\nBrownrown") == s2.strlen("   \\n   \\n\\nBrownrown"),
			s.strlen("4n") == s2.strlen("4n"),
			s.strlen("B        functoion   rown") == s2.strlen("B        functoion   rown"),
			s.strlen("vemThfGqorZJum5ymb0lsmtopsr") == s2.strlen("vemThfGqorZJum5ymb0lsmtopsr"),
			s.strlen("Th!s40ls !n 1This is a sample string    This is a samplt1t            eto string to LqNCZAtest the func Theon           to test the functi           àèìòùáéíóúýâêîôûãñõäëïöüÿçnt\\n") == s2.strlen("Th!s40ls !n 1This is a sample string    This is a samplt1t            eto string to LqNCZAtest the func Theon           to test the functi           àèìòùáéíóúýâêîôûãñõäëïöüÿçnt\\n"),
			s.strlen("àèìòùáéíóúýâêîôiwTish!1thûãñõäëïöüÿç") == s2.strlen("àèìòùáéíóúýâêîôiwTish!1thûãñõäëïöüÿç"),
			s.strlen("Th    This is a sample TTetnstrinisg Jumpeto test the function           !s40ls !n 1t\\n") == s2.strlen("Th    This is a sample TTetnstrinisg Jumpeto test the function           !s40ls !n 1t\\n"),
			s.strlen("Ove") == s2.strlen("Ove"),
			s.strlen("FoF1Thisxuk") == s2.strlen("FoF1Thisxuk"),
			s.strlen("   \\n\\nwwtes            ls    Th!s 1s 4 str1ng wtest5ymb0ls !n 1t\\n ") == s2.strlen("   \\n\\nwwtes            ls    Th!s 1s 4 str1ng wtest5ymb0ls !n 1t\\n "),
			s.strlen("B") == s2.strlen("B"),
			s.strlen("\\n\\nfnunc") == s2.strlen("\\n\\nfnunc"),
			s.strlen("sns") == s2.strlen("sns"),
			s.strlen("wiw1thstricQukickn") == s2.strlen("wiw1thstricQukickn"),
			s.strlen("  ring to tea  ") == s2.strlen("  ring to tea  "),
			s.strlen("DogtcricQukDogickn") == s2.strlen("DogtcricQukDogickn"),
			s.strlen("Dàèìòù4áéíóúýp1ssâêîôcJH1thûãñõäëïöüÿçgog") == s2.strlen("Dàèìòù4áéíóúýp1ssâêîôcJH1thûãñõäëïöüÿçgog"),
			s.strlen(" Th!s   \\n\\n 1s  ") == s2.strlen(" Th!s   \\n\\n 1s  "),
			s.strlen("  Th!s 1s 4 str1ng wtest5nymb0ls !nsampleto 1t\\n") == s2.strlen("  Th!s 1s 4 str1ng wtest5nymb0ls !nsampleto 1t\\n"),
			s.strlen("Do") == s2.strlen("Do"),
			s.strlen("   \\n\\n  striing") == s2.strlen("   \\n\\n  striing"),
			s.strlen("Th!s 1s 4 stsr1ng wtest5ymb0TTh!s40lsh!sls !n 1t\\n") == s2.strlen("Th!s 1s 4 stsr1ng wtest5ymb0TTh!s40lsh!sls !n 1t\\n"),
			s.strlen("striing") == s2.strlen("striing"),
			s.strlen("wteb40ls") == s2.strlen("wteb40ls"),
			s.strlen("fJumpeuon") == s2.strlen("fJumpeuon"),
			s.strlen("hyNycJ") == s2.strlen("hyNycJ"),
			s.strlen("mThfGeeTeqorZJum5ymb0lsmtops") == s2.strlen("mThfGeeTeqorZJum5ymb0lsmtops"),
			s.strlen("cJH1th") == s2.strlen("cJH1th"),
			s.strlen("TTh!s40lsh!s") == s2.strlen("TTh!s40lsh!s"),
			s.strlen("nfuntThis is a sample string    This is a sampl            eto string to test the func Theon           to test the functionheccc") == s2.strlen("nfuntThis is a sample string    This is a sampl            eto string to test the func Theon           to test the functionheccc"),
			s.strlen("fnunnc") == s2.strlen("fnunnc"),
			s.strlen("                ã           ") == s2.strlen("                ã           "),
			s.strlen("whyLaàèìòùáéíóúùýâê") == s2.strlen("whyLaàèìòùáéíóúùýâê"),
			s.strlen("ô") == s2.strlen("ô"),
			s.strlen("LaazLyy") == s2.strlen("LaazLyy"),
			s.strlen("psx       ") == s2.strlen("psx       "),
			s.strlen("stgrsr1ngLqNCZAtest") == s2.strlen("stgrsr1ngLqNCZAtest"),
			s.strlen("This is a sample string    This is a sampl            eto string to test thLaàèìòùáhéíóúùýâê   \\n\\n  Bro1s  îôûãñõäëïöüÿçQFoQxwtest5ymb0lseukyickythe function") == s2.strlen("This is a sample string    This is a sampl            eto string to test thLaàèìòùáhéíóúùýâê   \\n\\n  Bro1s  îôûãñõäëïöüÿçQFoQxwtest5ymb0lseukyickythe function"),
			s.strlen("This is a sample string    This is a sampl            eto string to LqNCZAtmThfGeeTeqorZJum5ymb0lsmtopsest the func Theon           to test the function") == s2.strlen("This is a sample string    This is a sampl            eto string to LqNCZAtmThfGeeTeqorZJum5ymb0lsmtopsest the func Theon           to test the function"),
			s.strlen("Foxx") == s2.strlen("Foxx")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test8()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("îôûãñõäëïöüÿçQFoQxukyicky") == s2.strlen("îôûãñõäëïöüÿçQFoQxukyicky"),
			s.strlen("The Quick Br owsttotherintgn Fox Jumpe Lazy og") == s2.strlen("The Quick Br owsttotherintgn Fox Jumpe Lazy og"),
			s.strlen("og") == s2.strlen("og"),
			s.strlen("str1ngsampaOverl") == s2.strlen("str1ngsampaOverl"),
			s.strlen("Fo stgrsr1ng   This is aTh!s 1s 4 str1ng wtest5ymb0lse !n 1t\\n sampleto string to test the function  n        x") == s2.strlen("Fo stgrsr1ng   This is aTh!s 1s 4 str1ng wtest5ymb0lse !n 1t\\n sampleto string to test the function  n        x"),
			s.strlen(" ã          àèìòùáéíóúýâêîôûãñõäëïöàèìòùáéíóúýâêîôûãñõäëïöüÿçüÿç") == s2.strlen(" ã          àèìòùáéíóúýâêîôûãñõäëïöàèìòùáéíóúýâêîôûãñõäëïöüÿçüÿç"),
			s.strlen("This") == s2.strlen("This"),
			s.strlen("    This is a sampl           eto string to test thes func tion          ") == s2.strlen("    This is a sampl           eto string to test thes func tion          "),
			s.strlen("funthstr1ng") == s2.strlen("funthstr1ng"),
			s.strlen("tet") == s2.strlen("tet"),
			s.strlen("whyNcJH1c") == s2.strlen("whyNcJH1c"),
			s.strlen("    This is a sample strinisg to test the functiostgrsr1ngLqNCZAtestn          ") == s2.strlen("    This is a sample strinisg to test the functiostgrsr1ngLqNCZAtestn          "),
			s.strlen("    This is a sample    \\n\\n 1s  string to te   ") == s2.strlen("    This is a sample    \\n\\n 1s  string to te   "),
			s.strlen("x  cJH1th1s 4         funthec    ls !nsampleto 1t\\n     ") == s2.strlen("x  cJH1th1s 4         funthec    ls !nsampleto 1t\\n     "),
			s.strlen("hTheTe") == s2.strlen("hTheTe"),
			s.strlen("funaTh!s") == s2.strlen("funaTh!s"),
			s.strlen("   \\nhy    This is a sample strinisg to test the fuunction          NcJH\\n  string4cJH1Jth") == s2.strlen("   \\nhy    This is a sample strinisg to test the fuunction          NcJH\\n  string4cJH1Jth"),
			s.strlen("BB") == s2.strlen("BB"),
			s.strlen("why1N  p  This is a sampleto string to test the function          cJH1th") == s2.strlen("why1N  p  This is a sampleto string to test the function          cJH1th"),
			s.strlen("mThftGqorZJum5ymb0lsmtstricQukicknops") == s2.strlen("mThftGqorZJum5ymb0lsmtstricQukicknops"),
			s.strlen(" àèìòùáéíóúýâêîôiwTish!!1thûãñõäëïöüÿç  \\n\\nwtest5ymb40ls    ") == s2.strlen(" àèìòùáéíóúýâêîôiwTish!!1thûãñõäëïöüÿç  \\n\\nwtest5ymb40ls    "),
			s.strlen("   \\n\\nRL 1s  ") == s2.strlen("   \\n\\nRL 1s  "),
			s.strlen("Th!s 1s RL4 str1ng wtest5ymb0l !n 1t\\n") == s2.strlen("Th!s 1s RL4 str1ng wtest5ymb0l !n 1t\\n"),
			s.strlen("str1nb0lse") == s2.strlen("str1nb0lse"),
			s.strlen("   \\nhy    This  is a sample strinisg to test the fuunction          NcJH\\n  string4cJH1Jth") == s2.strlen("   \\nhy    This  is a sample strinisg to test the fuunction          NcJH\\n  string4cJH1Jth"),
			s.strlen("nfuntThis") == s2.strlen("nfuntThis"),
			s.strlen("samplt1t") == s2.strlen("samplt1t"),
			s.strlen("wiw1s1th") == s2.strlen("wiw1s1th"),
			s.strlen("  Th!s 1s 4 st1r1ng wtest5nymb0ls !nsampleto 1t\\n") == s2.strlen("  Th!s 1s 4 st1r1ng wtest5nymb0ls !nsampleto 1t\\n"),
			s.strlen("nfuntThis        ") == s2.strlen("nfuntThis        "),
			s.strlen("Tish!  TTh!s40lsh!s 1s 4 str1ng wtest5ymb0lse !n 1t\\n         ") == s2.strlen("Tish!  TTh!s40lsh!s 1s 4 str1ng wtest5ymb0lse !n 1t\\n         "),
			s.strlen("Tish!          This is a sample string    This is a sampl   unction4") == s2.strlen("Tish!          This is a sample string    This is a sampl   unction4"),
			s.strlen("p") == s2.strlen("p"),
			s.strlen("Th!s 1s str1ng wtest5ymb0ls !n 1t\\n") == s2.strlen("Th!s 1s str1ng wtest5ymb0ls !n 1t\\n"),
			s.strlen("FMcc") == s2.strlen("FMcc"),
			s.strlen("BBo") == s2.strlen("BBo"),
			s.strlen("f\\n\\nfnunc") == s2.strlen("f\\n\\nfnunc"),
			s.strlen("îôûãñõäëïöüÿçQFoyQxukyickythe") == s2.strlen("îôûãñõäëïöüÿçQFoyQxukyickythe"),
			s.strlen("functionheccc") == s2.strlen("functionheccc"),
			s.strlen("Th!s40ls !n 1This is a sample string    This is a samplt1t            etto string to LqNCZAtest the func Theon           to test the functi           àèìòùáéíóúýâêîôûãñõäëïöüÿçnt\\n") == s2.strlen("Th!s40ls !n 1This is a sample string    This is a samplt1t            etto string to LqNCZAtest the func Theon           to test the functi           àèìòùáéíóúýâêîôûãñõäëïöüÿçnt\\n"),
			s.strlen("Bro") == s2.strlen("Bro"),
			s.strlen("JTh!s 1s 4 str1ng wtest5ymb0ls !nsampleto 1t\\num5ymb0lsmfunction") == s2.strlen("JTh!s 1s 4 str1ng wtest5ymb0ls !nsampleto 1t\\num5ymb0lsmfunction"),
			s.strlen("sThe Quick Brown Fox Jumps Over The Lazy DogttcricQukDogickn") == s2.strlen("sThe Quick Brown Fox Jumps Over The Lazy DogttcricQukDogickn"),
			s.strlen("sTh!s4strinisg05ymb0lslTs") == s2.strlen("sTh!s4strinisg05ymb0lslTs"),
			s.strlen("puobAuk") == s2.strlen("puobAuk"),
			s.strlen("Juom5ymbops") == s2.strlen("Juom5ymbops"),
			s.strlen("LaàèìòùáéQFoxxukcky") == s2.strlen("LaàèìòùáéQFoxxukcky"),
			s.strlen("whyNcJH1funnc") == s2.strlen("whyNcJH1funnc"),
			s.strlen("Th") == s2.strlen("Th"),
			s.strlen("Jg") == s2.strlen("Jg")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test9()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("thLaàèìòùáéíóúùýâê") == s2.strlen("thLaàèìòùáéíóúùýâê"),
			s.strlen("fuwhy1N") == s2.strlen("fuwhy1N"),
			s.strlen("fuuni") == s2.strlen("fuuni"),
			s.strlen("Bro1s") == s2.strlen("Bro1s"),
			s.strlen("\\r\\r") == s2.strlen("\\r\\r"),
			s.strlen("why1N  p  This is a samplefunction          cJH1th") == s2.strlen("why1N  p  This is a samplefunction          cJH1th"),
			s.strlen("QQFoTfuuniTxuk") == s2.strlen("QQFoTfuuniTxuk"),
			s.strlen("     o test the function1s  ") == s2.strlen("     o test the function1s  "),
			s.strlen("QFoxucick") == s2.strlen("QFoxucick"),
			s.strlen("àèìòùáéíóúýâêîôiwTish!1thûãñõäëïñöüÿç") == s2.strlen("àèìòùáéíóúýâêîôiwTish!1thûãñõäëïñöüÿç"),
			s.strlen("fnuncc") == s2.strlen("fnuncc"),
			s.strlen("Th!s 1s 4 sTtTheTer1ng wtest5ymb0lse !n 1t\\nJum5ymb0lsmfunction") == s2.strlen("Th!s 1s 4 sTtTheTer1ng wtest5ymb0lse !n 1t\\nJum5ymb0lsmfunction"),
			s.strlen("Ths !nîôûãñõäëïöüÿçQFoyQxukyickythe 1t\\n") == s2.strlen("Ths !nîôûãñõäëïöüÿçQFoyQxukyickythe 1t\\n"),
			s.strlen("p1s4Bnrown") == s2.strlen("p1s4Bnrown"),
			s.strlen("   \\n\\n  ") == s2.strlen("   \\n\\n  "),
			s.strlen("k") == s2.strlen("k"),
			s.strlen("etfuntThisoo") == s2.strlen("etfuntThisoo"),
			s.strlen("àèìòùáéíóúýâêîôûãñõäëïöàèìòùáéíóúýâêîôûãñõäëïöüÿçüÿç") == s2.strlen("àèìòùáéíóúýâêîôûãñõäëïöàèìòùáéíóúýâêîôûãñõäëïöüÿçüÿç"),
			s.strlen("LaàèìòùáéíúýâêîôûãñõäëïöüÿçQFoQxukyickThs !nîôûãñõäëïöüÿçQFoyQxukyickythe 1t\\ny") == s2.strlen("LaàèìòùáéíúýâêîôûãñõäëïöüÿçQFoQxukyickThs !nîôûãñõäëïöüÿçQFoyQxukyickythe 1t\\ny"),
			s.strlen("hyàèìòùáéíóúýâêîôûãñõäëïöàèìòùáéíóúýâêîôûãñõäëïöüÿçüÿç") == s2.strlen("hyàèìòùáéíóúýâêîôûãñõäëïöàèìòùáéíóúýâêîôûãñõäëïöüÿçüÿç"),
			s.strlen("Tish!whyNcJH1th          4") == s2.strlen("Tish!whyNcJH1th          4"),
			s.strlen("Th    This iTh!s 1s RL4 str1ng wtest5ymb0l !n 1t\\ns a sample TTetnstrinisg Jumpet   \\n\\nwtest5ymb40ls    t\\n") == s2.strlen("Th    This iTh!s 1s RL4 str1ng wtest5ymb0l !n 1t\\ns a sample TTetnstrinisg Jumpet   \\n\\nwtest5ymb40ls    t\\n"),
			s.strlen("Tish!whyNcJH1whyLaàèìòùáéíóúùýâê   \\n\\n  1s  îôãñõäëïöüÿçQFoQxukyickytothe  \t H1th  4") == s2.strlen("Tish!whyNcJH1whyLaàèìòùáéíóúùýâê   \\n\\n  1s  îôãñõäëïöüÿçQFoQxukyickytothe  \t H1th  4"),
			s.strlen("wDohycJHt") == s2.strlen("wDohycJHt"),
			s.strlen("TtTetn") == s2.strlen("TtTetn"),
			s.strlen("isJuis") == s2.strlen("isJuis"),
			s.strlen("Th!s1s") == s2.strlen("Th!s1s"),
			s.strlen("   s is a sample    \\n\\n 1s  string to te   ") == s2.strlen("   s is a sample    \\n\\n 1s  string to te   "),
			s.strlen("wiiw1th") == s2.strlen("wiiw1th"),
			s.strlen("OvOe") == s2.strlen("OvOe"),
			s.strlen("sJTh!s 1s 4 str1ng wtest5ymb0ls !nsampleto 1t\\num5ymb0lsmfunctionJummtop    This is a sample sttotherintg to test the function      QuaOverick     s") == s2.strlen("sJTh!s 1s 4 str1ng wtest5ymb0ls !nsampleto 1t\\num5ymb0lsmfunctionJummtop    This is a sample sttotherintg to test the function      QuaOverick     s"),
			s.strlen("Laàaèìòù!nnáéíóúùýâê") == s2.strlen("Laàaèìòù!nnáéíóúùýâê"),
			s.strlen("  Tish!     sThe Quick Brown Fox Jumps Over The Lazy DogttcricQukDogickn      4!n \\n\\n  1s  ") == s2.strlen("  Tish!     sThe Quick Brown Fox Jumps Over The Lazy DogttcricQukDogickn      4!n \\n\\n  1s  "),
			s.strlen("!nirs") == s2.strlen("!nirs"),
			s.strlen("sJTh!s 1s 4 str1ng wtest5ymb0ls !nsampleto 1t\\num5ymb0lsmfunctionJummtop    This is a sample sttotherintg to test           àèìòùáéíóúýâêîôûãñõäëïöüÿçQuaOverick     s") == s2.strlen("sJTh!s 1s 4 str1ng wtest5ymb0ls !nsampleto 1t\\num5ymb0lsmfunctionJummtop    This is a sample sttotherintg to test           àèìòùáéíóúýâêîôûãñõäëïöüÿçQuaOverick     s"),
			s.strlen("           àèìòùáéíóúýâêîôiwTstgrsr1ngïöüÿç") == s2.strlen("           àèìòùáéíóúýâêîôiwTstgrsr1ngïöüÿç"),
			s.strlen("Tsh!s") == s2.strlen("Tsh!s"),
			s.strlen("àèìòùáéíóúýâêîôûãñõäëïöàèìòùáiséíóúýâêîôûãñõäëïöüÿçüÿç") == s2.strlen("àèìòùáéíóúýâêîôûãñõäëïöàèìòùáiséíóúýâêîôûãñõäëïöüÿçüÿç"),
			s.strlen("i       s   ") == s2.strlen("i       s   "),
			s.strlen("  Tish!     sThe Quick Brown Fox Jumps Over The Lazy DogttcricQukickn      4!n \\n\\n  1s  ") == s2.strlen("  Tish!     sThe Quick Brown Fox Jumps Over The Lazy DogttcricQukickn      4!n \\n\\n  1s  "),
			s.strlen("RL4") == s2.strlen("RL4"),
			s.strlen("st1r1ng") == s2.strlen("st1r1ng"),
			s.strlen("sTtTheTer1stgrsr1ngLqNCZAtestng") == s2.strlen("sTtTheTer1stgrsr1ngLqNCZAtestng"),
			s.strlen("zPyWTI") == s2.strlen("zPyWTI"),
			s.strlen("aTh!s") == s2.strlen("aTh!s"),
			s.strlen("Fow1thF1Thisxuk") == s2.strlen("Fow1thF1Thisxuk"),
			s.strlen("saTh!s40lsmplt1t") == s2.strlen("saTh!s40lsmplt1t"),
			s.strlen("     nFo   ") == s2.strlen("     nFo   "),
			s.strlen("t1") == s2.strlen("t1"),
			s.strlen("    This is a sample sttotherintg tàèìòùáöüÿço test the funcstricQukickntion          ") == s2.strlen("    This is a sample sttotherintg tàèìòùáöüÿço test the funcstricQukickntion          ")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test10()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("   \\n\\nwwtes        t    ls    Th!s 1s 4 str1ng wtest5ymb0ls !n 1t\\n ") == s2.strlen("   \\n\\nwwtes        t    ls    Th!s 1s 4 str1ng wtest5ymb0ls !n 1t\\n "),
			s.strlen("string4cJH1Jth") == s2.strlen("string4cJH1Jth"),
			s.strlen("     This is a sampl          tothe func tion          ") == s2.strlen("     This is a sampl          tothe func tion          "),
			s.strlen("BBro") == s2.strlen("BBro"),
			s.strlen("nnnp1ss") == s2.strlen("nnnp1ss"),
			s.strlen("BBBo") == s2.strlen("BBBo"),
			s.strlen("The QuiisJumpsck Brown Fox JgLaàaèìòù!nnáéíóúùýâê") == s2.strlen("The QuiisJumpsck Brown Fox JgLaàaèìòù!nnáéíóúùýâê"),
			s.strlen("wtest5ymb0lscQukiwhyLaàèìòùáéíóúùýâê   \\n\\n  1s  îôûãñõäëïöüÿçQFoQxukyickytothe  \t H1thkn") == s2.strlen("wtest5ymb0lscQukiwhyLaàèìòùáéíóúùýâê   \\n\\n  1s  îôûãñõäëïöüÿçQFoQxukyickytothe  \t H1thkn"),
			s.strlen("TBrownrown") == s2.strlen("TBrownrown"),
			s.strlen("vemThfGqorZJum5ymb0lsmtstgrsr1ngLqNCZAtestpsr") == s2.strlen("vemThfGqorZJum5ymb0lsmtstgrsr1ngLqNCZAtestpsr"),
			s.strlen("   \\nhy    This is a sample strinisg to ttest the fuunction          NcJH\\n  string") == s2.strlen("   \\nhy    This is a sample strinisg to ttest the fuunction          NcJH\\n  string"),
			s.strlen("wtest5nymb0ls") == s2.strlen("wtest5nymb0ls"),
			s.strlen("whyNcJH1thFox") == s2.strlen("whyNcJH1thFox"),
			s.strlen("1This") == s2.strlen("1This"),
			s.strlen("x  cJH1th1s 4         funtthec    ls !nsampleto 1t\\n     ") == s2.strlen("x  cJH1th1s 4         funtthec    ls !nsampleto 1t\\n     "),
			s.strlen("eo") == s2.strlen("eo"),
			s.strlen("  Th!s 1s 4 st1   \\n\\nwwtest5ymb40ls    r1ng wtest5nymb0ls !nsampleto 1t\\n") == s2.strlen("  Th!s 1s 4 st1   \\n\\nwwtest5ymb40ls    r1ng wtest5nymb0ls !nsampleto 1t\\n"),
			s.strlen("     ã          àèìòùáéíóúìýâêîôstgrsr1ngûãñõäëïöüÿç  ") == s2.strlen("     ã          àèìòùáéíóúìýâêîôstgrsr1ngûãñõäëïöüÿç  "),
			s.strlen("wtest5ymb0TîôãñõäëïöüÿçQFoQxukyickytothesh!sls") == s2.strlen("wtest5ymb0TîôãñõäëïöüÿçQFoQxukyickytothesh!sls"),
			s.strlen("This is a sample string    This is a sampl            eto string to test thLaàèìòùáhéíóúùýâê   \\n\\n  Bro1s  îôûãñõäëïöüÿçQFoQxwtest5ymb0lseukyickythe ction") == s2.strlen("This is a sample string    This is a sampl            eto string to test thLaàèìòùáhéíóúùýâê   \\n\\n  Bro1s  îôûãñõäëïöüÿçQFoQxwtest5ymb0lseukyickythe ction"),
			s.strlen("striing     This is a sampl          tothe func tion          ") == s2.strlen("striing     This is a sampl          tothe func tion          "),
			s.strlen("QQFoTkTxu") == s2.strlen("QQFoTkTxu"),
			s.strlen("thes") == s2.strlen("thes"),
			s.strlen("Th!s40ls !n 1This is a sample string    This Dàèìòù4áéíóúýâêîôûãñõäëïöüÿçgogis a samplt1t            etto string to LqNCZAtest the func Theon           to test the functi           àèìòùáéíóúýâêîQckôûãñõäëïöüÿçnt\\n") == s2.strlen("Th!s40ls !n 1This is a sample string    This Dàèìòù4áéíóúýâêîôûãñõäëïöüÿçgogis a samplt1t            etto string to LqNCZAtest the func Theon           to test the functi           àèìòùáéíóúýâêîQckôûãñõäëïöüÿçnt\\n"),
			s.strlen(" ã          àèòìòùáéíóúýâêîôûãñõäëïöàèìòùáéíóúýâêîôûãñõäëïöüÿçüÿç") == s2.strlen(" ã          àèòìòùáéíóúýâêîôûãñõäëïöàèìòùáéíóúýâêîôûãñõäëïöüÿçüÿç"),
			s.strlen("rBrown") == s2.strlen("rBrown"),
			s.strlen("hy         functoio") == s2.strlen("hy         functoio"),
			s.strlen("nnshthes") == s2.strlen("nnshthes"),
			s.strlen("wtest5ymb0l") == s2.strlen("wtest5ymb0l"),
			s.strlen(" àèìòùáéíóúýâêîôiwTish!!1th1ûãñõäëïöüÿç  \\n\\nwtest5ymb40ls    ") == s2.strlen(" àèìòùáéíóúýâêîôiwTish!!1th1ûãñõäëïöüÿç  \\n\\nwtest5ymb40ls    "),
			s.strlen("This is a sample string Theonto test the function") == s2.strlen("This is a sample string Theonto test the function"),
			s.strlen("     ã          àèìòùáDogttcricQukDogicknéíóúìýâêîôstwhy1Ngrsr1ngûãñõäëïöüÿç  ") == s2.strlen("     ã          àèìòùáDogttcricQukDogicknéíóúìýâêîôstwhy1Ngrsr1ngûãñõäëïöüÿç  "),
			s.strlen("sQuiisJsmpsck") == s2.strlen("sQuiisJsmpsck"),
			s.strlen("àèìòùáéíóúýâêîôiwTish!!1thûãñõäëïöüÿçtnwtest5ymb0lscQukiwhyLLaàèìòùáéíóúùýâê   \\n\\n  1s  îôûãñõäëïöüÿçQFoQxukyickytothe  \t H1thkn\\nBrown") == s2.strlen("àèìòùáéíóúýâêîôiwTish!!1thûãñõäëïöüÿçtnwtest5ymb0lscQukiwhyLLaàèìòùáéíóúùýâê   \\n\\n  1s  îôûãñõäëïöüÿçQFoQxukyickytothe  \t H1thkn\\nBrown"),
			s.strlen("   Jum5ymbops ã iëïöüÿç  ") == s2.strlen("   Jum5ymbops ã iëïöüÿç  "),
			s.strlen("o") == s2.strlen("o"),
			s.strlen("why1N  p  This is a sampleto string to test the function          cJH1t1sh") == s2.strlen("why1N  p  This is a sampleto string to test the function          cJH1t1sh"),
			s.strlen("ywwtensLazy    This is a samQuaOverickple TTetnstrinisg to test the function           ") == s2.strlen("ywwtensLazy    This is a samQuaOverickple TTetnstrinisg to test the function           "),
			s.strlen("OZn") == s2.strlen("OZn"),
			s.strlen("cJH1t1s") == s2.strlen("cJH1t1s"),
			s.strlen("stgrsr1ngLqNtCZAtest") == s2.strlen("stgrsr1ngLqNtCZAtest"),
			s.strlen("    This  is a sample TTetnstrinisg to test the function           ") == s2.strlen("    This  is a sample TTetnstrinisg to test the function           "),
			s.strlen("yyy") == s2.strlen("yyy"),
			s.strlen("Th!s 1s 4 str1n0g wtest5ymb0lse !n 1t\\n") == s2.strlen("Th!s 1s 4 str1n0g wtest5ymb0lse !n 1t\\n"),
			s.strlen("kRLkion") == s2.strlen("kRLkion"),
			s.strlen("Juom5This is a sample string    This is a sampl            eto string to test the func Theon       to test the functionymbops") == s2.strlen("Juom5This is a sample string    This is a sampl            eto string to test the func Theon       to test the functionymbops"),
			s.strlen("   \\n\\nRL 1Ls  ") == s2.strlen("   \\n\\nRL 1Ls  "),
			s.strlen("Th!s 1s 4 sTtTheTer1ng wtest5ymb0lse !n 1t\\nJum5ymb0lsmfunct ion") == s2.strlen("Th!s 1s 4 sTtTheTer1ng wtest5ymb0lse !n 1t\\nJum5ymb0lsmfunct ion"),
			s.strlen("        funthec  tothet ") == s2.strlen("        funthec  tothet "),
			s.strlen("  Tish!     sThe Quick Brown Fox Jumps Over The Lazy DogttTcricQukickn      4!n \\n\\n  1s  ") == s2.strlen("  Tish!     sThe Quick Brown Fox Jumps Over The Lazy DogttTcricQukickn      4!n \\n\\n  1s  ")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test11()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("    This is a sample strinitsg to test  the functiostgrsr1ngLqNCZAtestn          ") == s2.strlen("    This is a sample strinitsg to test  the functiostgrsr1ngLqNCZAtestn          "),
			s.strlen("hyNJcJ") == s2.strlen("hyNJcJ"),
			s.strlen("    This is a sample TTetnstrinisg tiiiso test the function       n    ") == s2.strlen("    This is a sample TTetnstrinisg tiiiso test the function       n    "),
			s.strlen("iwTish!1Fo") == s2.strlen("iwTish!1Fo"),
			s.strlen("Tish!          This is a sample string    This is a sampl   unction!n4") == s2.strlen("Tish!          This is a sample string    This is a sampl   unction!n4"),
			s.strlen("whyNcJH11thîôûãñõäëïöüÿçQFoQxwtest5ymb0lseukyickythefunnc") == s2.strlen("whyNcJH11thîôûãñõäëïöüÿçQFoQxwtest5ymb0lseukyickythefunnc"),
			s.strlen("strinifunctitsg") == s2.strlen("strinifunctitsg"),
			s.strlen("44n") == s2.strlen("44n"),
			s.strlen(" cJH1th1s 4         funthec    lwiiw1ths !nsampleto 1t\\n") == s2.strlen(" cJH1th1s 4         funthec    lwiiw1ths !nsampleto 1t\\n"),
			s.strlen("    This is a           ") == s2.strlen("    This is a           "),
			s.strlen("    \\n\\nwwtes            ls   Th!s 1s 4 str1ng wtest5ymb0ls !n 1t\\n ") == s2.strlen("    \\n\\nwwtes            ls   Th!s 1s 4 str1ng wtest5ymb0ls !n 1t\\n "),
			s.strlen("st1r1n") == s2.strlen("st1r1n"),
			s.strlen("fuwiw1thstricQukicknnc") == s2.strlen("fuwiw1thstricQukicknnc"),
			s.strlen("cJH1t1sh") == s2.strlen("cJH1t1sh"),
			s.strlen("mThfGeeTebqorZJum5ymb0lsmtops") == s2.strlen("mThfGeeTebqorZJum5ymb0lsmtops"),
			s.strlen("wtestm5nTheymb0ls") == s2.strlen("wtestm5nTheymb0ls"),
			s.strlen("iTh!s") == s2.strlen("iTh!s"),
			s.strlen("This is a sample string    Thits is a sampl            eto string to test the func Theon       to test the function") == s2.strlen("This is a sample string    Thits is a sampl            eto string to test the func Theon       to test the function"),
			s.strlen("tion") == s2.strlen("tion"),
			s.strlen("funtThis is a sample string    This is a sampl            eto string to test the func Theon               àèìòùáéíóúýâêîôûãñõäëïöüÿç       to test the functionhec") == s2.strlen("funtThis is a sample string    This is a sampl            eto string to test the func Theon               àèìòùáéíóúýâêîôûãñõäëïöüÿç       to test the functionhec"),
			s.strlen("Th!stàèìòùáöüÿço40ls !n 1t\\n") == s2.strlen("Th!stàèìòùáöüÿço40ls !n 1t\\n"),
			s.strlen("DëàèìòùhyNJcJõäëïÿçg") == s2.strlen("DëàèìòùhyNJcJõäëïÿçg"),
			s.strlen(" zPyWTI        functoion   ") == s2.strlen(" zPyWTI        functoion   "),
			s.strlen("aOwtest5nymb0lsver") == s2.strlen("aOwtest5nymb0lsver"),
			s.strlen("QQFoTfuuniTxusample") == s2.strlen("QQFoTfuuniTxusample"),
			s.strlen("rstn1r1n") == s2.strlen("rstn1r1n"),
			s.strlen(" àèìòh  ") == s2.strlen(" àèìòh  "),
			s.strlen("     ") == s2.strlen("     "),
			s.strlen("123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789") == s2.strlen("123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"),
			s.strlen("MNhqmCdV") == s2.strlen("MNhqmCdV"),
			s.strlen("      The    ") == s2.strlen("      The    "),
			s.strlen("    1t  The    ") == s2.strlen("    1t  The    "),
			s.strlen("MNhqmCV") == s2.strlen("MNhqmCV"),
			s.strlen("MNhqThe Quick Brown Fox Jumps Over The BrownLazy DogmCV") == s2.strlen("MNhqThe Quick Brown Fox Jumps Over The BrownLazy DogmCV"),
			s.strlen("1s") == s2.strlen("1s"),
			s.strlen("sampLazyle") == s2.strlen("sampLazyle"),
			s.strlen("ttest") == s2.strlen("ttest"),
			s.strlen("Lazy  ") == s2.strlen("Lazy  "),
			s.strlen("ThTis") == s2.strlen("ThTis"),
			s.strlen("MN!nhqmCCdV") == s2.strlen("MN!nhqmCCdV"),
			s.strlen("MNhqThe") == s2.strlen("MNhqThe"),
			s.strlen("  \\r \\n   ") == s2.strlen("  \\r \\n   "),
			s.strlen("MNhqThe CQuick Brown Fox Jumps Over The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuick Brown Fox Jumps Over The BrownLazy DogmCV"),
			s.strlen("  \\r \\n  ") == s2.strlen("  \\r \\n  "),
			s.strlen("BrownLazy") == s2.strlen("BrownLazy"),
			s.strlen("samplse") == s2.strlen("samplse"),
			s.strlen("Lazy z ") == s2.strlen("Lazy z "),
			s.strlen("  \\r \\n\\r  ") == s2.strlen("  \\r \\n\\r  "),
			s.strlen("TTBrownis") == s2.strlen("TTBrownis"),
			s.strlen("àèìòõùáéíóúýâêîôûãñõäëïöüÿç") == s2.strlen("àèìòõùáéíóúýâêîôûãñõäëïöüÿç")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test12()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("MNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCV"),
			s.strlen("ThTi") == s2.strlen("ThTi"),
			s.strlen("MNhqThe CQuick Brown Fox oJumps Over The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuick Brown Fox oJumps Over The BrownLazy DogmCV"),
			s.strlen("MNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCV\\n") == s2.strlen("MNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCV\\n"),
			s.strlen("MNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCV") == s2.strlen("MNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCV"),
			s.strlen("BBrownLazyLazy  ") == s2.strlen("BBrownLazyLazy  "),
			s.strlen("BrownsampBrownleLazy") == s2.strlen("BrownsampBrownleLazy"),
			s.strlen("MNMNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCV\\nhqmCV") == s2.strlen("MNMNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCV\\nhqmCV"),
			s.strlen("This is a sample strOvering to test the function") == s2.strlen("This is a sample strOvering to test the function"),
			s.strlen("MNhqThe CQuicJumpsk Brown Fox Jumps Over The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuicJumpsk Brown Fox Jumps Over The BrownLazy DogmCV"),
			s.strlen("MNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test the function The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test the function The BrownLazy DogmCV"),
			s.strlen("   \\n\\n   z") == s2.strlen("   \\n\\n   z"),
			s.strlen("  \\r \\n    ") == s2.strlen("  \\r \\n    "),
			s.strlen("CQuick") == s2.strlen("CQuick"),
			s.strlen("This is a sample strintog to test the function") == s2.strlen("This is a sample strintog to test the function"),
			s.strlen("TTBrownis   ") == s2.strlen("TTBrownis   "),
			s.strlen("    1t 1 The    ") == s2.strlen("    1t 1 The    "),
			s.strlen("testt") == s2.strlen("testt"),
			s.strlen("    \\n\\n   ") == s2.strlen("    \\n\\n   "),
			s.strlen("aa") == s2.strlen("aa"),
			s.strlen("   This is a sample string to test the function\\n\\n   z") == s2.strlen("   This is a sample string to test the function\\n\\n   z"),
			s.strlen("BrownLazys") == s2.strlen("BrownLazys"),
			s.strlen("ThT    1t 1 The    i") == s2.strlen("ThT    1t 1 The    i"),
			s.strlen("BBrownLazyLazy") == s2.strlen("BBrownLazyLazy"),
			s.strlen("GThT    1t 1 The    ic") == s2.strlen("GThT    1t 1 The    ic"),
			s.strlen("Th!s 1s 4 str1str1ngng w1th 5ymb0ls !n 1t") == s2.strlen("Th!s 1s 4 str1str1ngng w1th 5ymb0ls !n 1t"),
			s.strlen("RGTk") == s2.strlen("RGTk"),
			s.strlen("MNhqTMNMNhqThehe") == s2.strlen("MNhqTMNMNhqThehe"),
			s.strlen("CQuicJumpsk\\r") == s2.strlen("CQuicJumpsk\\r"),
			s.strlen("DogmVCVBBrownLazyLazy  ") == s2.strlen("DogmVCVBBrownLazyLazy  "),
			s.strlen("MNhqThe Quick Brown FoxJumps Over The BrownLazy DogmCV") == s2.strlen("MNhqThe Quick Brown FoxJumps Over The BrownLazy DogmCV"),
			s.strlen("àèìòõùáéíóúýâêîôûãñõäëïöüÿçç") == s2.strlen("àèìòõùáéíóúýâêîôûãñõäëïöüÿçç"),
			s.strlen("BBrownLaazyLazy  ") == s2.strlen("BBrownLaazyLazy  "),
			s.strlen("This is a sample strintog ton test the function") == s2.strlen("This is a sample strintog ton test the function"),
			s.strlen("BrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCVnsampBrownleLazy") == s2.strlen("BrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCVnsampBrownleLazy"),
			s.strlen("Lazy zThTi ") == s2.strlen("Lazy zThTi "),
			s.strlen("MNhqThe CQuick Brown Fox oJutesttmps Over The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuick Brown Fox oJutesttmps Over The BrownLazy DogmCV"),
			s.strlen("w1This is a sample sstrintog ton test the functiont") == s2.strlen("w1This is a sample sstrintog ton test the functiont"),
			s.strlen("    \\n\\n function  ") == s2.strlen("    \\n\\n function  "),
			s.strlen("   \\r\\n \\n   ") == s2.strlen("   \\r\\n \\n   "),
			s.strlen("MNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test thCV") == s2.strlen("MNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test thCV"),
			s.strlen("Th!s 1s 4 sstr1str1ngng w1th 5ymb0ls !n 1t") == s2.strlen("Th!s 1s 4 sstr1str1ngng w1th 5ymb0ls !n 1t"),
			s.strlen("OverThisBBrownLaazyLazy  ") == s2.strlen("OverThisBBrownLaazyLazy  "),
			s.strlen("  \\r  \\n   ") == s2.strlen("  \\r  \\n   "),
			s.strlen("BrowMNhqThe CQuick Brown Fstrintogwox Jumpes Over The BrownLazey DogmCVnsampBrownleLazy") == s2.strlen("BrowMNhqThe CQuick Brown Fstrintogwox Jumpes Over The BrownLazey DogmCVnsampBrownleLazy"),
			s.strlen("CQuicJstrOveringumpsk") == s2.strlen("CQuicJstrOveringumpsk"),
			s.strlen("thCV") == s2.strlen("thCV"),
			s.strlen("Jumpes") == s2.strlen("Jumpes"),
			s.strlen("      1t  The    ") == s2.strlen("      1t  The    "),
			s.strlen(" MNhqm CdV ") == s2.strlen(" MNhqm CdV ")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test13()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("MNhqThe CQuicJumpsk Brown Fox Jumps  OverThis is a sample string to test thCV") == s2.strlen("MNhqThe CQuicJumpsk Brown Fox Jumps  OverThis is a sample string to test thCV"),
			s.strlen("ThhT    1t 1 The    i") == s2.strlen("ThhT    1t 1 The    i"),
			s.strlen("ThTTi") == s2.strlen("ThTTi"),
			s.strlen("Foxa") == s2.strlen("Foxa"),
			s.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !n 1t Over The TTBrownisgmCV") == s2.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !n 1t Over The TTBrownisgmCV"),
			s.strlen("     str1ng 1t  The    This is a sampleOvering to test the function") == s2.strlen("     str1ng 1t  The    This is a sampleOvering to test the function"),
			s.strlen("Th!s 1s 4 str1str1ngng w1th 5ymb0ls !n 1tBrownLazys") == s2.strlen("Th!s 1s 4 str1str1ngng w1th 5ymb0ls !n 1tBrownLazys"),
			s.strlen("BrownL  \\r  \\n   azys") == s2.strlen("BrownL  \\r  \\n   azys"),
			s.strlen("àèìòõ\\nç") == s2.strlen("àèìòõ\\nç"),
			s.strlen("BBrownLaazyLazy") == s2.strlen("BBrownLaazyLazy"),
			s.strlen("MNhqmCdCQuicJumpsk\\r") == s2.strlen("MNhqmCdCQuicJumpsk\\r"),
			s.strlen("      The      ") == s2.strlen("      The      "),
			s.strlen("BBrownLMNhqThe CQuick BrMNhqThe Quick Brown Fox Jumps Over The BrownLazy DogmCVown Fox Jumpes Over The BrownLazy DogmCVaazyLazy  ") == s2.strlen("BBrownLMNhqThe CQuick BrMNhqThe Quick Brown Fox Jumps Over The BrownLazy DogmCVown Fox Jumpes Over The BrownLazy DogmCVaazyLazy  "),
			s.strlen("BrLownL  \\r  \\n   azys") == s2.strlen("BrLownL  \\r  \\n   azys"),
			s.strlen("OverThis") == s2.strlen("OverThis"),
			s.strlen("     str1ng 1t  The    This is a samp leOvering to test the function") == s2.strlen("     str1ng 1t  The    This is a samp leOvering to test the function"),
			s.strlen("   This is a sample string to test th e function\\n\\n   z") == s2.strlen("   This is a sample string to test th e function\\n\\n   z"),
			s.strlen("This nction") == s2.strlen("This nction"),
			s.strlen("zThTi ") == s2.strlen("zThTi "),
			s.strlen("BBrownLMNhqThehTTi") == s2.strlen("BBrownLMNhqThehTTi"),
			s.strlen("Th!s 1s 4 str1str1ngng w1th 5ymb0ls !n 1tBrow") == s2.strlen("Th!s 1s 4 str1str1ngng w1th 5ymb0ls !n 1tBrow"),
			s.strlen("MNhqThe CQuick Brown hFox Jumps Over The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuick Brown hFox Jumps Over The BrownLazy DogmCV"),
			s.strlen("oJutesttmps") == s2.strlen("oJutesttmps"),
			s.strlen("functont") == s2.strlen("functont"),
			s.strlen("MNMNhqThe CQuick Brown Fox Jumpes OvewnLazy DogmCV\\nhqmCV") == s2.strlen("MNMNhqThe CQuick Brown Fox Jumpes OvewnLazy DogmCV\\nhqmCV"),
			s.strlen("Fstrintogwox") == s2.strlen("Fstrintogwox"),
			s.strlen("MNhqThe CQuicJumpsk BrowMNhqmn Fox Jumps OverThis  to test t") == s2.strlen("MNhqThe CQuicJumpsk BrowMNhqmn Fox Jumps OverThis  to test t"),
			s.strlen("ic") == s2.strlen("ic"),
			s.strlen("MNhqThe CQuick Brown Fox oJutesttmps Oqver The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuick Brown Fox oJutesttmps Oqver The BrownLazy DogmCV"),
			s.strlen("This sample string to      The     test the function") == s2.strlen("This sample string to      The     test the function"),
			s.strlen("DogmCVown  GThT ") == s2.strlen("DogmCVown  GThT "),
			s.strlen("Th!s 1s 4 str1str1ngnsg w1th 5ymb0ls !n 1t") == s2.strlen("Th!s 1s 4 str1str1ngnsg w1th 5ymb0ls !n 1t"),
			s.strlen("Do      The    g") == s2.strlen("Do      The    g"),
			s.strlen("\t\t\t") == s2.strlen("\t\t\t"),
			s.strlen("    \\n\\n func!ntion  ") == s2.strlen("    \\n\\n func!ntion  "),
			s.strlen("te      1t  The    stt") == s2.strlen("te      1t  The    stt"),
			s.strlen("ThT     testt1t 1 The    i") == s2.strlen("ThT     testt1t 1 The    i"),
			s.strlen("bUmvrK") == s2.strlen("bUmvrK"),
			s.strlen("Tihis sample string to      The     test the function") == s2.strlen("Tihis sample string to      The     test the function"),
			s.strlen("Th!s 1s 4 str1ng w1thTTBrownis    5ymb0ls !n 1t") == s2.strlen("Th!s 1s 4 str1ng w1thTTBrownis    5ymb0ls !n 1t"),
			s.strlen("ThT") == s2.strlen("ThT"),
			s.strlen("r1ng") == s2.strlen("r1ng"),
			s.strlen("leOvering") == s2.strlen("leOvering"),
			s.strlen("te      1t  sThe    s tt") == s2.strlen("te      1t  sThe    s tt"),
			s.strlen("ttV") == s2.strlen("ttV"),
			s.strlen("   This is a sample stringunction\\n\\n   z") == s2.strlen("   This is a sample stringunction\\n\\n   z"),
			s.strlen("The The Lazy Dog") == s2.strlen("The The Lazy Dog"),
			s.strlen("MNhqThe CQuick Brown hFox Jumps Over The BrownLazy DoMNhqmCdCQuicJumpsk\\rgmCV") == s2.strlen("MNhqThe CQuick Brown hFox Jumps Over The BrownLazy DoMNhqmCdCQuicJumpsk\\rgmCV"),
			s.strlen("TThTi") == s2.strlen("TThTi"),
			s.strlen("MNhq1TMNMNhqThehe") == s2.strlen("MNhq1TMNMNhqThehe")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test14()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("      T he    ") == s2.strlen("      T he    "),
			s.strlen("MNhqmC      The      ") == s2.strlen("MNhqmC      The      "),
			s.strlen("aaa") == s2.strlen("aaa"),
			s.strlen("BrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCVnsampBrownleLazyhTiTh!s 1s 4 str1ng w1th 5ymb0ls !n 1ts") == s2.strlen("BrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCVnsampBrownleLazyhTiTh!s 1s 4 str1ng w1th 5ymb0ls !n 1ts"),
			s.strlen("TTBrownisgmCV") == s2.strlen("TTBrownisgmCV"),
			s.strlen("MNhqThe CQuicJumpsk Brown Foxstr1str1ngng Jumps OverThis is a sample string to test thCV") == s2.strlen("MNhqThe CQuicJumpsk Brown Foxstr1str1ngng Jumps OverThis is a sample string to test thCV"),
			s.strlen("leOvMNhqThe CQuick Brown Fox oJumps Over The BrownLazy DogmCVering") == s2.strlen("leOvMNhqThe CQuick Brown Fox oJumps Over The BrownLazy DogmCVering"),
			s.strlen("ThT OverThisBBrownLaazyLazy   t1t 1 The    i") == s2.strlen("ThT OverThisBBrownLaazyLazy   t1t 1 The    i"),
			s.strlen("MNhqThe CQuDogmCVnsampBrownleLazyick Brown Fox oJutesttmps Oqver The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuDogmCVnsampBrownleLazyick Brown Fox oJutesttmps Oqver The BrownLazy DogmCV"),
			s.strlen("BzyLazy") == s2.strlen("BzyLazy"),
			s.strlen("MNhqThe CQuicJumpsk Brown Fox Jumpsw1This is a sample sstrintog ton test the functiont OverThis is a sample string to test the function The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuicJumpsk Brown Fox Jumpsw1This is a sample sstrintog ton test the functiont OverThis is a sample string to test the function The BrownLazy DogmCV"),
			s.strlen("ThT     testt1t 1 The    iMNhq1TMNMNhqThehe") == s2.strlen("ThT     testt1t 1 The    iMNhq1TMNMNhqThehe"),
			s.strlen("ThT    1sampLazylet 1 The    i") == s2.strlen("ThT    1sampLazylet 1 The    i"),
			s.strlen("s") == s2.strlen("s"),
			s.strlen("ThT     i") == s2.strlen("ThT     i"),
			s.strlen("  CdV  ") == s2.strlen("  CdV  "),
			s.strlen("\t\t\t\t") == s2.strlen("\t\t\t\t"),
			s.strlen("àèìòùáéíBrMNhqTheóúýâêîôûãñõäëïöüÿç") == s2.strlen("àèìòùáéíBrMNhqTheóúýâêîôûãñõäëïöüÿç"),
			s.strlen("    \\n\\n !func!ntion  ") == s2.strlen("    \\n\\n !func!ntion  "),
			s.strlen("    1t 1   ") == s2.strlen("    1t 1   "),
			s.strlen("    1tBrownsampBrownleLazy 1   ") == s2.strlen("    1tBrownsampBrownleLazy 1   "),
			s.strlen("tVhCV") == s2.strlen("tVhCV"),
			s.strlen("BBrownLaayLazy  ") == s2.strlen("BBrownLaayLazy  "),
			s.strlen("MNhqThe CQuick Brown Fox Jumpes OveJr The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuick Brown Fox Jumpes OveJr The BrownLazy DogmCV"),
			s.strlen("BrownL") == s2.strlen("BrownL"),
			s.strlen("BwBrownLazyLazy  ") == s2.strlen("BwBrownLazyLazy  "),
			s.strlen("BwownLazyLazy  ") == s2.strlen("BwownLazyLazy  "),
			s.strlen("TTBris   ") == s2.strlen("TTBris   "),
			s.strlen("      1t   The    ") == s2.strlen("      1t   The    "),
			s.strlen("MNhqThe CQuick Brown Fox Jumps Over The BrownLaz   \\n\\n   zy DomgmCV") == s2.strlen("MNhqThe CQuick Brown Fox Jumps Over The BrownLaz   \\n\\n   zy DomgmCV"),
			s.strlen("Th!s 1sr 4 str1str1ngnsg w1th 5ymb0ls !n 1t") == s2.strlen("Th!s 1sr 4 str1str1ngnsg w1th 5ymb0ls !n 1t"),
			s.strlen("ttVàèìòùáéíóúýâêîôûãñõäëïöüÿç") == s2.strlen("ttVàèìòùáéíóúýâêîôûãñõäëïöüÿç"),
			s.strlen("MNhqThe CQuticJumpsk Brown Fox Jumps OverThis is a sample string to test thCV") == s2.strlen("MNhqThe CQuticJumpsk Brown Fox Jumps OverThis is a sample string to test thCV"),
			s.strlen("MNhqmCdCQuicJumpsk\\rhqmCV") == s2.strlen("MNhqmCdCQuicJumpsk\\rhqmCV"),
			s.strlen("DogmCVering") == s2.strlen("DogmCVering"),
			s.strlen("OverThisBBrownLaazyLazy  \t\t\t") == s2.strlen("OverThisBBrownLaazyLazy  \t\t\t"),
			s.strlen("MNhqThe CQuicJumpsk BBrownLazyLazyBrown Fox Jumps  OverThis is a sample string to test thCV") == s2.strlen("MNhqThe CQuicJumpsk BBrownLazyLazyBrown Fox Jumps  OverThis is a sample string to test thCV"),
			s.strlen("   This is a sample strg to test t function\\n\\n   z") == s2.strlen("   This is a sample strg to test t function\\n\\n   z"),
			s.strlen("MNe CQuick Brown Fox oJumps Over The BrownLazy DogmCV") == s2.strlen("MNe CQuick Brown Fox oJumps Over The BrownLazy DogmCV"),
			s.strlen("DogmCVerinDog") == s2.strlen("DogmCVerinDog"),
			s.strlen("JumbUmvrKpes") == s2.strlen("JumbUmvrKpes"),
			s.strlen("BrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCLazy") == s2.strlen("BrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCLazy"),
			s.strlen("    1t 1 Thestring    ") == s2.strlen("    1t 1 Thestring    "),
			s.strlen("rstr1ng") == s2.strlen("rstr1ng"),
			s.strlen("to   This is a sample string to test the function\\n\\n   z") == s2.strlen("to   This is a sample string to test the function\\n\\n   z"),
			s.strlen("MNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test th e functionCdV The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test th e functionCdV The BrownLazy DogmCV"),
			s.strlen("BwownisLazyLazy  ") == s2.strlen("BwownisLazyLazy  "),
			s.strlen("ThT Th!s 1s 4 sstr1str1ngng w1th 5ymb0ls !n 1t   1t 1 The    i") == s2.strlen("ThT Th!s 1s 4 sstr1str1ngng w1th 5ymb0ls !n 1t   1t 1 The    i"),
			s.strlen("CQuicJumpskg\\r") == s2.strlen("CQuicJumpskg\\r"),
			s.strlen("s    \\n\\n !func!ntion  e") == s2.strlen("s    \\n\\n !func!ntion  e")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test15()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("aLLa zy z aa") == s2.strlen("aLLa zy z aa"),
			s.strlen("ThTMNei") == s2.strlen("ThTMNei"),
			s.strlen("g") == s2.strlen("g"),
			s.strlen("MNhqThe CQuicJumpsk Browno Fox Jumps Over The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuicJumpsk Browno Fox Jumps Over The BrownLazy DogmCV"),
			s.strlen("BrownsampBrownlMNhqThe CQuicJumpsk BBrownLazyLazyBrown Fox Jumps  OverThis is a sample string to test thCVeLazy") == s2.strlen("BrownsampBrownlMNhqThe CQuicJumpsk BBrownLazyLazyBrown Fox Jumps  OverThis is a sample string to test thCVeLazy"),
			s.strlen("thCVeLBrownLazazy") == s2.strlen("thCVeLBrownLazazy"),
			s.strlen("JuTTBrownismbUmvrKpes") == s2.strlen("JuTTBrownismbUmvrKpes"),
			s.strlen("CQuDogmCVnsampBrownleLazyick") == s2.strlen("CQuDogmCVnsampBrownleLazyick"),
			s.strlen("Th1tBrownsampBrownleLazy!s 1s 4 str1str1ngng w1th 5ymb0ls !n 1tBrownLazys") == s2.strlen("Th1tBrownsampBrownleLazy!s 1s 4 str1str1ngng w1th 5ymb0ls !n 1tBrownLazys"),
			s.strlen("samp") == s2.strlen("samp"),
			s.strlen("rrstr1ng") == s2.strlen("rrstr1ng"),
			s.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !n 1t Over The TrownisgmCV") == s2.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !n 1t Over The TrownisgmCV"),
			s.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !n 1testt1tt Over The TBrowMNhqmnrownisgmCV") == s2.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !n 1testt1tt Over The TBrowMNhqmnrownisgmCV"),
			s.strlen("Brow") == s2.strlen("Brow"),
			s.strlen("àèìòõùáéíóúýâêîôûãñõäëïöüÿ") == s2.strlen("àèìòõùáéíóúýâêîôûãñõäëïöüÿ"),
			s.strlen("MNhqThe CQuick Brown hFox Jumps OveMNhqThe CQuicJumpsk Brown Fox Jumps  OverThis is a sample string to test thCVr The BrownLazy DoMNhqmCdCQuicJumpsk\\rgmCV") == s2.strlen("MNhqThe CQuick Brown hFox Jumps OveMNhqThe CQuicJumpsk Brown Fox Jumps  OverThis is a sample string to test thCVr The BrownLazy DoMNhqmCdCQuicJumpsk\\rgmCV"),
			s.strlen("bUmv") == s2.strlen("bUmv"),
			s.strlen("  \\rLazy \\n\\r  ") == s2.strlen("  \\rLazy \\n\\r  "),
			s.strlen("stri     ntog") == s2.strlen("stri     ntog"),
			s.strlen("Th!s 1s 4 str1ng w1thTTBrownis    55ymb0ls !n 1t") == s2.strlen("Th!s 1s 4 str1ng w1thTTBrownis    55ymb0ls !n 1t"),
			s.strlen("teestt") == s2.strlen("teestt"),
			s.strlen("MNhqThBrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCLazyk BrowMNhqmn Fox Jumps OverThis  to test t") == s2.strlen("MNhqThBrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCLazyk BrowMNhqmn Fox Jumps OverThis  to test t"),
			s.strlen("tetest") == s2.strlen("tetest"),
			s.strlen("  t     ") == s2.strlen("  t     "),
			s.strlen("OverThisBBrownLaazLazy  ") == s2.strlen("OverThisBBrownLaazLazy  "),
			s.strlen("DogmCLazyk") == s2.strlen("DogmCLazyk"),
			s.strlen("Thi") == s2.strlen("Thi"),
			s.strlen("MNhqThe CQuDogmCVnsampBrownleLazyick Brown Fox oJutesttmps OqveThT     testt1t 1 The    iMNhq1TMNMNhqTheher The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuDogmCVnsampBrownleLazyick Brown Fox oJutesttmps OqveThT     testt1t 1 The    iMNhq1TMNMNhqTheher The BrownLazy DogmCV"),
			s.strlen("aaaaa") == s2.strlen("aaaaa"),
			s.strlen(" Th!s 1s 4 str1ng w1th 5ymb0ls !n 1t Over The TTBrownisgmCV") == s2.strlen(" Th!s 1s 4 str1ng w1th 5ymb0ls !n 1t Over The TTBrownisgmCV"),
			s.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !n 1testt1tt Over The TBrowMNhqmnrownisgmCVstrC1ng") == s2.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !n 1testt1tt Over The TBrowMNhqmnrownisgmCVstrC1ng"),
			s.strlen("    1tBrownsampBrownleLazy 1   \t") == s2.strlen("    1tBrownsampBrownleLazy 1   \t"),
			s.strlen("Tntoghis") == s2.strlen("Tntoghis"),
			s.strlen("functontMNhqThe CQuDogmCVnsampBrownleLazyick Brown Fox oJutesttmps OqveThT     testt1t 1 The    iMNhq1TMNMNhqTheher The BrownLazy DogmCV") == s2.strlen("functontMNhqThe CQuDogmCVnsampBrownleLazyick Brown Fox oJutesttmps OqveThT     testt1t 1 The    iMNhq1TMNMNhqTheher The BrownLazy DogmCV"),
			s.strlen("1CQuicJstrOveringumpskt") == s2.strlen("1CQuicJstrOveringumpskt"),
			s.strlen("JumJp") == s2.strlen("JumJp"),
			s.strlen("  \\rLazy \\n\\r Th!s 1s 4 str1ng w1th 5ymb0ls !n 1testt1tt Over The TBrowMNhqmnrownisgmCVstrC1ng 1s") == s2.strlen("  \\rLazy \\n\\r Th!s 1s 4 str1ng w1th 5ymb0ls !n 1testt1tt Over The TBrowMNhqmnrownisgmCVstrC1ng 1s"),
			s.strlen("BBroownLazyLazy") == s2.strlen("BBroownLazyLazy"),
			s.strlen("s    \\n\\n !fu55ymb0lsnc!ntion  e") == s2.strlen("s    \\n\\n !fu55ymb0lsnc!ntion  e"),
			s.strlen("tVtV") == s2.strlen("tVtV"),
			s.strlen("MNhqmCdCV") == s2.strlen("MNhqmCdCV"),
			s.strlen("oMNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test thCV") == s2.strlen("oMNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test thCV"),
			s.strlen("MNhqThe CuQuicJumpsk Brown Foxstr1str1ngng Jumps OverThis is a sample string to test thCV") == s2.strlen("MNhqThe CuQuicJumpsk Brown Foxstr1str1ngng Jumps OverThis is a sample string to test thCV"),
			s.strlen("RDogmCLazyGGTk") == s2.strlen("RDogmCLazyGGTk"),
			s.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !n 1testMNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCVt1tt Over The TBrowMNhqmnrownisgmCV") == s2.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !n 1testMNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCVt1tt Over The TBrowMNhqmnrownisgmCV"),
			s.strlen("MNhqThe CQu\t\t\tick Brown func!ntionFox oJutesttmps Over The BrownLazy DogmCV") == s2.strlen("MNhqThe CQu\t\t\tick Brown func!ntionFox oJutesttmps Over The BrownLazy DogmCV"),
			s.strlen("This is ao sample starintog ton test the function") == s2.strlen("This is ao sample starintog ton test the function"),
			s.strlen("MNhqThe\t\t") == s2.strlen("MNhqThe\t\t"),
			s.strlen("to   Thihs is a sa\\nmple string to test the function\\n\\n   z") == s2.strlen("to   Thihs is a sa\\nmple string to test the function\\n\\n   z"),
			s.strlen("FstrintoBrLownLgwox") == s2.strlen("FstrintoBrLownLgwox")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test16()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("ttVàèìòùáéíóúýâêîôûãñõäëïìöüÿç") == s2.strlen("ttVàèìòùáéíóúýâêîôûãñõäëïìöüÿç"),
			s.strlen("BwownLazyLazy") == s2.strlen("BwownLazyLazy"),
			s.strlen("BrowwnL") == s2.strlen("BrowwnL"),
			s.strlen("Th!s") == s2.strlen("Th!s"),
			s.strlen("MNhqThe CQuick Brown hFox Jumps Over The BrownLazy DoMNhThis is a sample strintog to test the function\\rgmCV") == s2.strlen("MNhqThe CQuick Brown hFox Jumps Over The BrownLazy DoMNhThis is a sample strintog to test the function\\rgmCV"),
			s.strlen("MNMNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCV\\nhCV") == s2.strlen("MNMNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCV\\nhCV"),
			s.strlen("MNhqThBrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCLazyk BrowMNhqmn Fox Jumps OverThis  to tehst t") == s2.strlen("MNhqThBrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCLazyk BrowMNhqmn Fox Jumps OverThis  to tehst t"),
			s.strlen("MNMNhqThe CQuick Brown Fox JumpBrownL  \\r  \\n   azyses Over The BrownLazy DogmCV\\nhCV") == s2.strlen("MNMNhqThe CQuick Brown Fox JumpBrownL  \\r  \\n   azyses Over The BrownLazy DogmCV\\nhCV"),
			s.strlen("MNhqThe CQuick Brown Fox Jumpes OveJr The BrownLazy DogmBrownCV") == s2.strlen("MNhqThe CQuick Brown Fox Jumpes OveJr The BrownLazy DogmBrownCV"),
			s.strlen("r1g") == s2.strlen("r1g"),
			s.strlen("UcBwownisLazyLazy  ") == s2.strlen("UcBwownisLazyLazy  "),
			s.strlen("UcBwDomgmCVownisLazyLazy  ") == s2.strlen("UcBwDomgmCVownisLazyLazy  "),
			s.strlen("MNhqThe C Quick Brown Fox Jumps Over The BrownLazy DogmCV") == s2.strlen("MNhqThe C Quick Brown Fox Jumps Over The BrownLazy DogmCV"),
			s.strlen("BrownL  tt\\r  \\n   azys") == s2.strlen("BrownL  tt\\r  \\n   azys"),
			s.strlen("stCQuicJstrOveringumpskt") == s2.strlen("stCQuicJstrOveringumpskt"),
			s.strlen("LaOverThisBBrownLaazyLazy  \t\t\tzy  ") == s2.strlen("LaOverThisBBrownLaazyLazy  \t\t\tzy  "),
			s.strlen("TTBr ownis   ") == s2.strlen("TTBr ownis   "),
			s.strlen("aLLa zy z a") == s2.strlen("aLLa zy z a"),
			s.strlen("This is ao sample starintog ton test the n") == s2.strlen("This is ao sample starintog ton test the n"),
			s.strlen("      1t  T") == s2.strlen("      1t  T"),
			s.strlen("     str1ng 1t  The    This is a samThT    1sampLazylet 1 The    ipleOvering to test the function") == s2.strlen("     str1ng 1t  The    This is a samThT    1sampLazylet 1 The    ipleOvering to test the function"),
			s.strlen("TTBrownnnis   ") == s2.strlen("TTBrownnnis   "),
			s.strlen("    1tBrownsampBrownleLazy B1   \t") == s2.strlen("    1tBrownsampBrownleLazy B1   \t"),
			s.strlen("functBwownisLazyLazy  ion") == s2.strlen("functBwownisLazyLazy  ion"),
			s.strlen("MNhqThe C Quick Brown Fox zy DogmCV") == s2.strlen("MNhqThe C Quick Brown Fox zy DogmCV"),
			s.strlen("ickk") == s2.strlen("ickk"),
			s.strlen("BrozwnLazys") == s2.strlen("BrozwnLazys"),
			s.strlen("This i s a sample strintog to test the hfuncti on") == s2.strlen("This i s a sample strintog to test the hfuncti on"),
			s.strlen("1tBrownLazys") == s2.strlen("1tBrownLazys"),
			s.strlen("z") == s2.strlen("z"),
			s.strlen("Lazyy z ") == s2.strlen("Lazyy z "),
			s.strlen("BBrownLLazyLazy  ") == s2.strlen("BBrownLLazyLazy  "),
			s.strlen("stCQuicMNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCVstrOveringumpskt") == s2.strlen("stCQuicMNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCVstrOveringumpskt"),
			s.strlen("i") == s2.strlen("i"),
			s.strlen("CQuDogmCVnsampBrownfunctBwownisLazyLazy") == s2.strlen("CQuDogmCVnsampBrownfunctBwownisLazyLazy"),
			s.strlen("aLLaa zz aa") == s2.strlen("aLLaa zz aa"),
			s.strlen("UcBwDomgmCVownisLazyLazy") == s2.strlen("UcBwDomgmCVownisLazyLazy"),
			s.strlen("DogmCLazy") == s2.strlen("DogmCLazy"),
			s.strlen("BrownLazMNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test th e functionCdV The BrownLazy DogmCVys") == s2.strlen("BrownLazMNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test th e functionCdV The BrownLazy DogmCVys"),
			s.strlen("1testt1tt") == s2.strlen("1testt1tt"),
			s.strlen("sThe") == s2.strlen("sThe"),
			s.strlen("MNhqThe C Quic   k Brown FTh!s 1s 4 str1ng w1th 5ymb0ls !n 1testMNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCVt1tt Over The TBrowMNhqmnrownisgmCVox Jumps Over TheC BrownLazy DogmCV") == s2.strlen("MNhqThe C Quic   k Brown FTh!s 1s 4 str1ng w1th 5ymb0ls !n 1testMNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCVt1tt Over The TBrowMNhqmnrownisgmCVox Jumps Over TheC BrownLazy DogmCV"),
			s.strlen("Jumpsw1This") == s2.strlen("Jumpsw1This"),
			s.strlen("QGLWea") == s2.strlen("QGLWea"),
			s.strlen("1testt1t") == s2.strlen("1testt1t"),
			s.strlen("CCQuicJumpsk") == s2.strlen("CCQuicJumpsk"),
			s.strlen("MNhqmThTis  ") == s2.strlen("MNhqmThTis  "),
			s.strlen("This is a sample strintog to tesMNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test the function The BrownLazy DogmCVt the function") == s2.strlen("This is a sample strintog to tesMNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test the function The BrownLazy DogmCVt the function"),
			s.strlen("   This is a sampleT stringunction\\n\\n   z") == s2.strlen("   This is a sampleT stringunction\\n\\n   z"),
			s.strlen("aLLa zyz z a") == s2.strlen("aLLa zyz z a")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test17()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("nction") == s2.strlen("nction"),
			s.strlen("TBrowMNhqmnrownisgmCV") == s2.strlen("TBrowMNhqmnrownisgmCV"),
			s.strlen("DogmC    \\n\\n func!ntion  Lazyk") == s2.strlen("DogmC    \\n\\n func!ntion  Lazyk"),
			s.strlen("BryownLazys") == s2.strlen("BryownLazys"),
			s.strlen("ThTiTi") == s2.strlen("ThTiTi"),
			s.strlen("TMNhqmCVhis is ao sample starintog ton test the n") == s2.strlen("TMNhqmCVhis is ao sample starintog ton test the n"),
			s.strlen("     str1ng 1t  The    This is a samThT    1sampLazylet 1 The  MNhqThe CuQuicJumpsk Brown Fo    \\n\\n   xstr1str1ngng Jumps OverThis is a sample string to test thCVt the function") == s2.strlen("     str1ng 1t  The    This is a samThT    1sampLazylet 1 The  MNhqThe CuQuicJumpsk Brown Fo    \\n\\n   xstr1str1ngng Jumps OverThis is a sample string to test thCVt the function"),
			s.strlen("ntog") == s2.strlen("ntog"),
			s.strlen("hCV") == s2.strlen("hCV"),
			s.strlen("Th!s 1s 4Cr1ngng w1th 5ymb0ls !n 1t") == s2.strlen("Th!s 1s 4Cr1ngng w1th 5ymb0ls !n 1t"),
			s.strlen("ThT OverThisBBrownLaazyLazy   t1DomgmCV  i") == s2.strlen("ThT OverThisBBrownLaazyLazy   t1DomgmCV  i"),
			s.strlen("  \\r  \\n   àèì t   1t  The    òõùáéíóúýâêîôûãñõäëïöüÿ") == s2.strlen("  \\r  \\n   àèì t   1t  The    òõùáéíóúýâêîôûãñõäëïöüÿ"),
			s.strlen("samplsme") == s2.strlen("samplsme"),
			s.strlen("on") == s2.strlen("on"),
			s.strlen("ThT     ttestt1t 1 TBrownLazyhe    i") == s2.strlen("ThT     ttestt1t 1 TBrownLazyhe    i"),
			s.strlen("sasmplsme") == s2.strlen("sasmplsme"),
			s.strlen("\\n\\n\\n") == s2.strlen("\\n\\n\\n"),
			s.strlen("CQuticJumpsk") == s2.strlen("CQuticJumpsk"),
			s.strlen("OqvveThT") == s2.strlen("OqvveThT"),
			s.strlen("functontMNhqThLe CQuDogmCVnsampBrownleLazyick Brown Fox oJutesttmps OqveThT     testt1t 1 The    iMNhq1TMNMNhqTheher The BrownLazy DàèìòùáéíBrMNhqTheóúýâêîôûãñõäëïöüÿçogmCV") == s2.strlen("functontMNhqThLe CQuDogmCVnsampBrownleLazyick Brown Fox oJutesttmps OqveThT     testt1t 1 The    iMNhq1TMNMNhqTheher The BrownLazy DàèìòùáéíBrMNhqTheóúýâêîôûãñõäëïöüÿçogmCV"),
			s.strlen("C") == s2.strlen("C"),
			s.strlen("sTe") == s2.strlen("sTe"),
			s.strlen("w1thTTBrownis") == s2.strlen("w1thTTBrownis"),
			s.strlen("    samThT ") == s2.strlen("    samThT "),
			s.strlen("CQuicJumpskg") == s2.strlen("CQuicJumpskg"),
			s.strlen("CQuicJumpskg\\r\\r") == s2.strlen("CQuicJumpskg\\r\\r"),
			s.strlen("!func!ontion") == s2.strlen("!func!ontion"),
			s.strlen("MNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test thhe function The BrownLazy DogmCV") == s2.strlen("MNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sample string to test thhe function The BrownLazy DogmCV"),
			s.strlen("Jumpsw1Tntoghiss") == s2.strlen("Jumpsw1Tntoghiss"),
			s.strlen("BBrownLaayLazy") == s2.strlen("BBrownLaayLazy"),
			s.strlen("saasmplsme") == s2.strlen("saasmplsme"),
			s.strlen("MNhqThe Quick Brown Fox Jumps Over The BrownLazy DogmCrV") == s2.strlen("MNhqThe Quick Brown Fox Jumps Over The BrownLazy DogmCrV"),
			s.strlen("1seampLazyleat") == s2.strlen("1seampLazyleat"),
			s.strlen("ThhT") == s2.strlen("ThhT"),
			s.strlen("    1t 1 The    aaaaa") == s2.strlen("    1t 1 The    aaaaa"),
			s.strlen("BrownLazMNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sastr1str1ngnsgmple string to test th e functionCdV The BrownLazy DogmCVys") == s2.strlen("BrownLazMNhqThe CQuicJumpsk Brown Fox Jumps OverThis is a sastr1str1ngnsgmple string to test th e functionCdV The BrownLazy DogmCVys"),
			s.strlen("MNhqThe CQuick Brown hFox Jumps Over The BrownLazy DoMNhThis is a sample strintoTh!s 1s 4 str1ng w1th 5ymb0ls !n 1testMNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCVt1tt Over The TBrowMNhqmnrownisgmCVg to test the function\\rgmCV") == s2.strlen("MNhqThe CQuick Brown hFox Jumps Over The BrownLazy DoMNhThis is a sample strintoTh!s 1s 4 str1ng w1th 5ymb0ls !n 1testMNhqThe CQuick Brown Fox Jumpes Over The BrownLazy DogmCVt1tt Over The TBrowMNhqmnrownisgmCVg to test the function\\rgmCV"),
			s.strlen("GThT    1t 1 The CuQuicJumpsk   ic") == s2.strlen("GThT    1t 1 The CuQuicJumpsk   ic"),
			s.strlen("      The     ") == s2.strlen("      The     "),
			s.strlen("BBrownLaayLazystringunction") == s2.strlen("BBrownLaayLazystringunction"),
			s.strlen("UcBwDnomgmCVownisLazyLazy") == s2.strlen("UcBwDnomgmCVownisLazyLazy"),
			s.strlen("BBrownLaayLazystrizngunction") == s2.strlen("BBrownLaayLazystrizngunction"),
			s.strlen("BrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCVnsampBrownleLaLazy z zyhTiTh!s 1s 4 str1ng w1th 5ymb0ls !n 1ts") == s2.strlen("BrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCVnsampBrownleLaLazy z zyhTiTh!s 1s 4 str1ng w1th 5ymb0ls !n 1ts"),
			s.strlen("zz") == s2.strlen("zz"),
			s.strlen("w  CdV  1This is a sample sstrintogt ton test the functiont") == s2.strlen("w  CdV  1This is a sample sstrintogt ton test the functiont"),
			s.strlen("qygh") == s2.strlen("qygh"),
			s.strlen("BrowMNhqThe CQuick Brown Fstrintogwox Jumpes Over The BrownLazuey DogmCVnsampBrownleLazy") == s2.strlen("BrowMNhqThe CQuick Brown Fstrintogwox Jumpes Over The BrownLazuey DogmCVnsampBrownleLazy"),
			s.strlen("TheC") == s2.strlen("TheC"),
			s.strlen("    1t 1  The    ") == s2.strlen("    1t 1  The    "),
			s.strlen("  te      1t  sThe    s tt\\r \\n\\r Foxstr1str1ngng") == s2.strlen("  te      1t  sThe    s tt\\r \\n\\r Foxstr1str1ngng")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test18()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("DogmCV") == s2.strlen("DogmCV"),
			s.strlen("OverTh") == s2.strlen("OverTh"),
			s.strlen("   ThiBrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCLazys is a sample string to test th e function\\n\\n   z") == s2.strlen("   ThiBrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCLazys is a sample string to test th e function\\n\\n   z"),
			s.strlen("     str1ng 1t  The    This is a samThT    1sampLazylet i1 The  MNhqThe CuQuicJumpBsk Brown Fo    \\n\\n   xstr1str1ngng Jumps OverThis is a sample string to test thCVt the function") == s2.strlen("     str1ng 1t  The    This is a samThT    1sampLazylet i1 The  MNhqThe CuQuicJumpBsk Brown Fo    \\n\\n   xstr1str1ngng Jumps OverThis is a sample string to test thCVt the function"),
			s.strlen("Th!s 1s 4 str1str1 1t") == s2.strlen("Th!s 1s 4 str1str1 1t"),
			s.strlen("nctoion") == s2.strlen("nctoion"),
			s.strlen("TTBrown") == s2.strlen("TTBrown"),
			s.strlen("BBroownLaaLLa zy z aazyLazy") == s2.strlen("BBroownLaaLLa zy z aazyLazy"),
			s.strlen("str1g") == s2.strlen("str1g"),
			s.strlen("MNhqThBrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCLazyk BrowMNhqmn Fox Jumps OverThis  to ytehst t") == s2.strlen("MNhqThBrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCLazyk BrowMNhqmn Fox Jumps OverThis  to ytehst t"),
			s.strlen("BrowMNhqThe CQuick Brown Fstrintogwox Jumpes Over zy") == s2.strlen("BrowMNhqThe CQuick Brown Fstrintogwox Jumpes Over zy"),
			s.strlen("    1t  Theion    ") == s2.strlen("    1t  Theion    "),
			s.strlen("TTBrownis    ") == s2.strlen("TTBrownis    "),
			s.strlen("MNhqm") == s2.strlen("MNhqm"),
			s.strlen("   ThiBrowMNhqThe CQuick FoxJumpsBrown Fwox Jumpes Over The BrownLazey DogmCLazys is a sample string to test th e function\\n\\n   z") == s2.strlen("   ThiBrowMNhqThe CQuick FoxJumpsBrown Fwox Jumpes Over The BrownLazey DogmCLazys is a sample string to test th e function\\n\\n   z"),
			s.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !nw 1testt1tt Over The TBrowMNhqmnrownisgmCV") == s2.strlen("Th!s 1s 4 str1ng w1th 5ymb0ls !nw 1testt1tt Over The TBrowMNhqmnrownisgmCV"),
			s.strlen("JumbstringunctionUmvrKpes") == s2.strlen("JumbstringunctionUmvrKpes"),
			s.strlen("Lazy ") == s2.strlen("Lazy "),
			s.strlen("BwownLazyaLa zy  ") == s2.strlen("BwownLazyaLa zy  "),
			s.strlen("CCQuicJumt1DomgmCVpsk") == s2.strlen("CCQuicJumt1DomgmCVpsk"),
			s.strlen("Jumpsw1TntoghiTTBrisss") == s2.strlen("Jumpsw1TntoghiTTBrisss"),
			s.strlen("BrownL  tt\\r  \\n   aCQuDogmCVnsampBrownleLazyickzys") == s2.strlen("BrownL  tt\\r  \\n   aCQuDogmCVnsampBrownleLazyickzys"),
			s.strlen("UrK") == s2.strlen("UrK"),
			s.strlen("BBrownLaayLazystringunctionn") == s2.strlen("BBrownLaayLazystringunctionn"),
			s.strlen("VhCV") == s2.strlen("VhCV"),
			s.strlen("CQuicJstrOveJringumpsk") == s2.strlen("CQuicJstrOveJringumpsk"),
			s.strlen("MNhqThe CQuick Brown hFox Jumps OcveMNhqThe CQuicJumpsk Brown Fox Jumps  OverThis is a sample string to test thCVr The BrownLazy DoMNhqmCdCQuicJumpsk\\rgmCV") == s2.strlen("MNhqThe CQuick Brown hFox Jumps OcveMNhqThe CQuicJumpsk Brown Fox Jumps  OverThis is a sample string to test thCVr The BrownLazy DoMNhqmCdCQuicJumpsk\\rgmCV"),
			s.strlen("BrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCVnsampBrownleLaLazy z zyhTiTh!s 1s 4 str1ng w1th 5ymb0ls !n 1tsrrstr1ng") == s2.strlen("BrowMNhqThe CQuick Brown Fwox Jumpes Over The BrownLazey DogmCVnsampBrownleLaLazy z zyhTiTh!s 1s 4 str1ng w1th 5ymb0ls !n 1tsrrstr1ng"),
			s.strlen("OverThisBBrownLaazyLazy") == s2.strlen("OverThisBBrownLaazyLazy"),
			s.strlen("aCQuDogmCVnsampBrownleLazyickzys") == s2.strlen("aCQuDogmCVnsampBrownleLazyickzys"),
			s.strlen("UcBwownisLazzyz ") == s2.strlen("UcBwownisLazzyz "),
			s.strlen("iii") == s2.strlen("iii"),
			s.strlen("s    \\n\\n !func!ntio    \\n\\n func!ntion  n  e") == s2.strlen("s    \\n\\n !func!ntio    \\n\\n func!ntion  n  e"),
			s.strlen("Th!s 1s 4 str1sMNhqmtr1 1t") == s2.strlen("Th!s 1s 4 str1sMNhqmtr1 1t"),
			s.strlen("testVhCVtt") == s2.strlen("testVhCVtt"),
			s.strlen("DogmCVBrownsampBrownlMNhqThensampBrownleLazy") == s2.strlen("DogmCVBrownsampBrownlMNhqThensampBrownleLazy"),
			s.strlen("  te      1t  sThe    s tt\\r \\n1\\r Foxstr1str1ngng") == s2.strlen("  te      1t  sThe    s tt\\r \\n1\\r Foxstr1str1ngng"),
			s.strlen("MNhqThe Quick BrowTBrowMNhqmnrownisgmCVgn FoxJumpws Over The BrownLazy DogmCV") == s2.strlen("MNhqThe Quick BrowTBrowMNhqmnrownisgmCVgn FoxJumpws Over The BrownLazy DogmCV"),
			s.strlen("Th!s 1s 4 str1str1ngng w1th 5ymb0lDogmVCVBBrownLazyLazy  s !n 1tBrow") == s2.strlen("Th!s 1s 4 str1str1ngng w1th 5ymb0lDogmVCVBBrownLazyLazy  s !n 1tBrow"),
			s.strlen("Ju   This is a sampleT stringunction\\n\\n   zTTBrownismbUmvrKpes") == s2.strlen("Ju   This is a sampleT stringunction\\n\\n   zTTBrownismbUmvrKpes"),
			s.strlen("ç") == s2.strlen("ç"),
			s.strlen("TBrowMNhqmnrownisgmCVstrC1ng") == s2.strlen("TBrowMNhqmnrownisgmCVstrC1ng"),
			s.strlen("   This is a sample strinazysgunction\\n\\n   z") == s2.strlen("   This is a sample strinazysgunction\\n\\n   z"),
			s.strlen("aLLa") == s2.strlen("aLLa"),
			s.strlen("Th!s 1s 4s str1str1ngng w1th 5ymb0ls !n 1tBrow") == s2.strlen("Th!s 1s 4s str1str1ngng w1th 5ymb0ls !n 1tBrow"),
			s.strlen("BrownLazuey") == s2.strlen("BrownLazuey"),
			s.strlen("MNhqThe CQugicJumpsk Brown Foxstr1str1ngng Jumps OverThis is a sample string to test thCV") == s2.strlen("MNhqThe CQugicJumpsk Brown Foxstr1str1ngng Jumps OverThis is a sample string to test thCV"),
			s.strlen("\\nzTTBrownismbUmvrKpesBrMNhqThe\\nTh!s 1s 4 str1str1ngng w1th 5ymb0lDogmVCVBBrownLazyLazy  s !n 1tBrow\\n") == s2.strlen("\\nzTTBrownismbUmvrKpesBrMNhqThe\\nTh!s 1s 4 str1str1ngng w1th 5ymb0lDogmVCVBBrownLazyLazy  s !n 1tBrow\\n"),
			s.strlen("LaOverThissBBrownLaazyLazy  \t\t\tzy  ") == s2.strlen("LaOverThissBBrownLaazyLazy  \t\t\tzy  "),
			s.strlen("stCQuicJstrOveringumpsktoJutesttmps") == s2.strlen("stCQuicJstrOveringumpsktoJutesttmps")
		);
		if (correct.contains(false)) {
			throw new AssertionError();
		}
	}
	public static void test19()  throws NoSuchAlgorithmException {
		Solution s = new Solution();
		SolutionGenerated s2 = new SolutionGenerated();
		List<Boolean> correct = Arrays.asList(
			s.strlen("tstr1g") == s2.strlen("tstr1g"),
			s.strlen("Th!s 1s !4 str1str1ngnsg w1th 5ymb0ls !n 1t") == s2.strlen("Th!s 1s !4 str1str1ngnsg w1th 5ymb0ls !n 1t"),
			s.strlen("leOvMNhqThe CQuick Brown Fox oJumps Ovepr The BrownLazy DogmCVering") == s2.strlen("leOvMNhqThe CQuick Brown Fox oJumps Ovepr The BrownLazy DogmCVering"),
			s.strlen("CQuck") == s2.strlen("CQuck"),
			s.strlen("aLaLBrowTBrowMNhqmnrownisgmCVgna") == s2.strlen("aLaLBrowTBrowMNhqmnrownisgmCVgna"),
			s.strlen("thThT OaverThisBBrownLaazyLazye   t1t 1 The    iCVeLBrownLazazy") == s2.strlen("thThT OaverThisBBrownLaazyLazye   t1t 1 The    iCVeLBrownLazazy"),
			s.strlen("BBrownLLazyLazy") == s2.strlen("BBrownLLazyLazy"),
			s.strlen("Th!s 1s w1This is a sample sstrintog ton test the functiont4 str1str1ngng w1th 5ymb0ls !n 1t") == s2.strlen("Th!s 1s w1This is a sample sstrintog ton test the functiont4 str1str1ngng w1th 5ymb0ls !n 1t"),
			s.strlen(" Th!s 1s 4 str1ng w1thn 5ymb0ls !n 1t Over The TTBrownisgmCV") == s2.strlen(" Th!s 1s 4 str1ng w1thn 5ymb0ls !n 1t Over The TTBrownisgmCV"),
			s.strlen("testtt") == s2.strlen("testtt"),
			s.strlen("aLLaa zz aaick") == s2.strlen("aLLaa zz aaick"),
			s.strlen("DogmCrV") == s2.strlen("DogmCrV"),
			s.strlen("hThT     testt1t 1 The    iMNhq1TMNMNhqThehe") == s2.strlen("hThT     testt1t 1 The    iMNhq1TMNMNhqThehe"),
			s.strlen("         The     ") == s2.strlen("         The     ")
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
		test15();
		test16();
		test17();
		test18();
		test19();
	}
}
