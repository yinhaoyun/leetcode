import java.util.Arrays;

class Solution {
    
    private static List<List<String>> result;
    private List<Stack<Point>> positionResult;
    private Stack<Point> positions;
    private int N = 0;
    public List<List<String>> solveNQueens(int n) {
        N = n;
        positions = new Stack<>();
        positionResult = new ArrayList<>();
        result = new ArrayList<>();
        helper(0);
        
        for (Stack<Point> stk: positionResult) {
            result.add(convert(stk));
        }
        return result;
    }
    
    private List<String> convert(Stack<Point> stk) {
        StringBuilder[] sbs = new StringBuilder[N];
        char[] dots = new char[N];
        Arrays.fill(dots, '.');
        String dotsStr = new String(dots);
        for (int i = 0; i < sbs.length; i++) {
            sbs[i] = new StringBuilder(dotsStr);
        }
        for (Point point: stk) {
            sbs[point.x].setCharAt(point.y, 'Q');
        }

        List<String> result = new ArrayList<>();
        for (StringBuilder sb: sbs) {
            result.add(sb.toString());
        }
        return result;
    }

    private void helper(int x) {
        
        if (x == N) {
            assert positions.clone() != null;
            positionResult.add((Stack<Point>) positions.clone());
            return;
        }
        
        for (int y = 0; y < N; y ++) {
            if (!check(x, y)) continue; // FAIL
            
            positions.push(new Point(x, y));
            helper(x + 1);
            positions.pop();
            
        }
    }
    
    private boolean check(int newX, int newY) {
        for (Point point: positions) {
            if (point.x == newX || point.y == newY) {
                return false;
            }
            
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
