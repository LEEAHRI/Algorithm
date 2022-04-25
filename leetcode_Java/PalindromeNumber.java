import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
//    public boolean isPalindrome(int x) {
//        String a = String.valueOf(x);
//        ArrayList<Character> b = new ArrayList<Character>();
//        for (int i = 0; i < a.length(); i++) {
//            char currentCharacter = a.charAt(i);
//            b.add(currentCharacter);
//
//        }
//
//
//        System.out.println(b);
//
//        return false;
//    }

    public boolean isPalindrome(int x) {
        String a = String.valueOf(x);
        ArrayList<Character> list = new ArrayList<>();
        for (int i = 0; i < a.length(); i++) {
            char currentCharacter = a.charAt(i);//getting the character at current index
            list.add(currentCharacter);//adding the character to the list
        }
        List<Character> copiedList = new ArrayList<>();
        copiedList.addAll(list);
        Collections.reverse(list);
        for (int idx = 0; idx < list.size(); idx++) {
            if (list.get(idx) != copiedList.get(idx)) {
                return false;
            }
        }
        return true;
    }
}

public class PalindromeNumber {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isPalindrome(-121));
    }
}
