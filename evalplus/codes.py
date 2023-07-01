# import java.util.ArrayList;
# import java.util.HashMap;
# import java.util.List;
# import java.util.Map;
#
# public class Main {
#     public static void main(String[] args) {
#         ArrayList<String> keys = new ArrayList<>();
#         keys.add("A");
#         keys.add("B");
#         keys.add("C");
#
#         ArrayList<Integer> values = new ArrayList<>();
#         values.add(1);
#         values.add(2);
#         values.add(3);
#
#         Map<String, Integer> map = createMap(keys, values);
#         System.out.println(map);
#
#         ArrayList<Integer> intKeys = new ArrayList<>();
#         intKeys.add(1);
#         intKeys.add(2);
#         intKeys.add(3);
#
#         ArrayList<String> stringValues = new ArrayList<>();
#         stringValues.add("One");
#         stringValues.add("Two");
#         stringValues.add("Three");
#
#         Map<Integer, String> genericMap = createMap(intKeys, stringValues);
#         System.out.println(genericMap);
#     }
#
#     public static <K, V> Map<K, V> createMap(List<K> keys, List<V> values) {
#         if (keys.size() != values.size()) {
#             throw new IllegalArgumentException("The sizes of the input lists must be the same.");
#         }
#
#         Map<K, V> map = new HashMap<>();
#         for (int i = 0; i < keys.size(); i++) {
#             K key = keys.get(i);
#             V value = values.get(i);
#             map.put(key, value);
#         }
#         return map;
#     }
# }