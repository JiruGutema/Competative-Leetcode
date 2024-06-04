class Solution {
    
    public static List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        if (strs.length == 0) {
            
            return new ArrayList<>();
        
        }
        
        try{
        for (String s : strs) {
            char[] ch = s.toCharArray();
            Arrays.sort(ch);
            String el = String.valueOf(ch);
            if (!map.containsKey(el)) map.put(el, new ArrayList<>());
            map.get(el).add(s);}}
        catch (Exception e){
            //nothing
        }
            
        return new ArrayList<>(map.values());
    }
}