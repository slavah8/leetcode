class FirstUnique {
private:
    queue<int> q;
    unordered_map<int, int> counts;
public:
    FirstUnique(vector<int>& nums) {
        for (int x : nums) {
            add(x);
        }

    }
    
    int showFirstUnique() {
        while (!q.empty() && counts[q.front()] > 1) {
            q.pop();
        }
        return q.empty() ? -1 : q.front();
    }
    
    void add(int value) {
        counts[value]++;
        q.push(value);
        
    }
};

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique* obj = new FirstUnique(nums);
 * int param_1 = obj->showFirstUnique();
 * obj->add(value);
 */