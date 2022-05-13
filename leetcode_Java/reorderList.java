/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {

    public class ListNode {
        public int val;
        public ListNode next;

        ListNode() {
        }

        public ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }

        public static ListNode of(int... integers) {
            if (integers == null || integers.length == 0) throw new IllegalArgumentException();

            ListNode head = new ListNode(0);
            ListNode last = head;
            ListNode p;
            for (int integer : integers) {
                p = new ListNode(integer);
                last.next = p;
                last = last.next;
            }

            return head.next;
        }

        @Override
        public String toString() {
            return "ListNode{" +
                    "val=" + val +
                    ", next=" + next +
                    '}';
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof ListNode)) return false;
            ListNode listNode = (ListNode) o;
            return val == listNode.val &&
                    Objects.equals(next, listNode.next);
        }

        @Override
        public int hashCode() {
            return Objects.hash(val, next);
        }
    }

    public static void reorderList(ListNode head) { // array int[]
        if (head == null) return;

        ListNode slow = head;
        ListNode fast = head;

        // 1. 반 짜르고
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        ListNode prev = null, curr = slow, next;
        // 1 -> 2 -> 3 -> null
        // null <- 1 <- 2 <- 3
        // 3 -> 2 -> 1 -> null
        // 2. 반짜르고 뒷부분 리버스
        while (curr != null) {
            next = curr.next;

            curr.next = prev;

            prev = curr;
            curr = next;
        }

        // 1 -> 2 -> 3
        // 6 -> 5 -> 4

        // 3. 앞부분 + 뒷부분 재조합
        ListNode first = head, second = prev;
        while (second.next != null) {
            next = first.next;
            first.next = second;
            first = next;

            next = second.next;
            second.next = first;
            second = next;
        }
    }

    public static void main(String[] argv) {
        ListNode head = ListNode.of(1, 2, 3, 4);
        reorderList(head);
    }


}