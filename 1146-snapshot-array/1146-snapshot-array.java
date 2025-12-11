class SnapshotArray {

    private static class Pair {
        int snapId;
        int val;
        Pair(int s, int v) {
            this.snapId = s;
            this.val = v;
        }
    }
    
    List<Pair>[] history;
    private int snapId;

    public SnapshotArray(int length) {
        history = new ArrayList[length];
        for (int i = 0; i < length; i++) {
            history[i] = new ArrayList<>();
            history[i].add(new Pair(0, 0));
        }
        snapId = 0;
    }
    
    public void set(int index, int val) {
        List<Pair> list = history[index];
        Pair last = list.get(list.size() - 1);

        if (last.snapId == snapId) {
            last.val = val;
        } else {
            list.add(new Pair(snapId, val));
        }
        
    }
    
    public int snap() {
        return snapId++;
    }
    
    public int get(int index, int snap_id) {
        List<Pair> list = history[index];

        // binary search for largest snapId <= targetSnapId
        int left = 0;
        int right = list.size() - 1;
        int res = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (list.get(mid).snapId <= snap_id) {
                res = list.get(mid).val;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return res;
        
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */