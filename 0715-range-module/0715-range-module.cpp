class RangeModule {
public:
    map<int, int> mp;

    RangeModule() {
        
    }
    
    void addRange(int left, int right) {
        if (left >= right) return;

        auto it = mp.lower_bound(left);

        if (it != mp.begin()) {
            auto prevIt = prev(it);
            if (prevIt->second >= left) {
                it = prevIt;
            }
        }

        // Now it starts at the real first overlapping interval:

        while (it != mp.end() && it->first <= right) {
            if (it->second < left) {
                it++;
                continue;
            }

            left = min(left, it->first);
            right = max(right, it->second);

            it = mp.erase(it); // returns next iterator
        }

        mp[left] = right;
    }
    
    bool queryRange(int left, int right) {
        auto it = mp.upper_bound(left);
        if (it == mp.begin()) return false;

        it--;
        return it->second >= right;
    }
    
    void removeRange(int left, int right) {

        if (left >= right) return;

        auto it = mp.lower_bound(left);

        if (it != mp.begin()) {
            auto prevIt = prev(it);
            if (prevIt->second > left) {
                it = prevIt;
            }
        }


        while (it != mp.end() && it->first < right) {
            int a = it->first;
            int b = it->second;

            if (b <= left) {
                it++;
                continue;
            }

            it = mp.erase(it);

            if (a < left) {
                mp[a] = left;
            }

            if (b > right) {
                mp[right] = b;
            }
        }
    }

};

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule* obj = new RangeModule();
 * obj->addRange(left,right);
 * bool param_2 = obj->queryRange(left,right);
 * obj->removeRange(left,right);
 */