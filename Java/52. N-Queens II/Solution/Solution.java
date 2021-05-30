package Solution;

import java.util.*;

class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        for (int i = 1; i <= 9; i++) {
            System.out.println(s.totalNQueens(i));
        }
    }

    private Stack<Point> positions;
    private boolean[] usedY;
    private int N;
    private int result;

    public int totalNQueens(int n) {
        N = n;
        usedY = new boolean[N];
        positions = new Stack<>();
        result = 0;
        helper(0);
        return result;
    }

    private void helper(int x) {
        if (x == N) {
            result ++;
            return;
        }
        
        for (int y = 0; y < N; y ++) {
            if (usedY[y]) continue;
            if (!checkDiag(x, y)) continue; // FAIL
            
            positions.push(new Point(x, y));
            usedY[y] = true;
            helper(x + 1);
            usedY[y] = false;
            positions.pop();
        }
    }
    
    private boolean checkDiag(int newX, int newY) {
        for (Point point: positions) {
            if (Math.abs(point.x - newX) == Math.abs(point.y - newY)) {
                return false;
            }
        }
        return true;
    }
    
    class Point {
        int x;
        int y;
      
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public String toString() {
            return String.format("[%d, %d]", x, y);
        }
    }
}