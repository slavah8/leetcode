class RLEIterator {
public:
    vector<long long> enc;
    int i;
    long long count;
    int value;

    RLEIterator(vector<int>& encoding) {
        
        enc.assign(encoding.begin(), encoding.end());
        i = 0;
    }
    
    int next(int n) {
        long long need = n;

        while (i < (int)enc.size() && need > 0) {
            if (enc[i] == 0) {
                i += 2;
                continue;
            }

            if (enc[i] >= need) {
                enc[i] -= need;
                return (int)enc[i + 1];
            } else {
                need -= enc[i];
                enc[i] = 0;
                i += 2;
            }
        }
        return -1;
    }
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator* obj = new RLEIterator(encoding);
 * int param_1 = obj->next(n);
 */