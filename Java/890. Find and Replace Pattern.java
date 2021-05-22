class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        return Solution2(words, pattern);
    }

    // Normalize
    private List<String> Solution2(String[] words, String pattern) {
        List<String> result = new ArrayList<>();
        String np = normalize(pattern);
        for (String word : words) {
            if (np.equals(normalize(word))) {
                result.add(word);
            }
        }
        return result;
    }
    
    private String normalize(String word) {
        StringBuilder sb = new StringBuilder();
        Map<Character, Character> map = new HashMap<>();
        char next = 'a';
        for (char c: word.toCharArray()) {
            if (map.get(c) != null) {
                sb.append(map.get(c));
            } else {
                map.put(c, next);
                sb.append(next++);
            }
        }
        return sb.toString();
    }

    private List<String> Solution1(String[] words, String pattern) {
        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (match(word, pattern)) {
                result.add(word);
            }
        }
        return result;
    }
    
    private boolean match(String word, String pattern) {
        Map<Character, Character> m = new HashMap<>();
        for (int i = 0; i < word.length(); i++) {
            char w = word.charAt(i);
            char p = pattern.charAt(i);
            if (!m.containsKey(w)) m.put(w, p);
            if (m.get(w) != p) return false;
        }
        
        boolean[] seen = new boolean[26];
        for (char c: m.values()) {
            if (seen[c - 'a']) return false;
            seen[c - 'a'] = true;
        }
        return true;
    }
}
