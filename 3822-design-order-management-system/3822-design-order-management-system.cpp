class OrderManagementSystem {
        unordered_map<int, pair<int, int>> byId;

        // // (type, price) -> set of active orderIds
        unordered_map<long long, unordered_set<int>> bucket;

        int typeCode(const string &orderType) {
            return (orderType == "buy") ? 0 : 1;
        }

        long long key(int type, int price) {
            return ((long long)type << 32) | (unsigned int)price;
        }

public:
    OrderManagementSystem() {
        // orderId -> {type(0 buy / 1 sell), price}
        
    }
    
    void addOrder(int orderId, string orderType, int price) {
        int t = typeCode(orderType);
        byId[orderId] = {t, price};
        bucket[key(t, price)].insert(orderId);
    }
    
    void modifyOrder(int orderId, int newPrice) {
        auto &info = byId[orderId];
        int t = info.first;
        int oldPrice = info.second;

        if (oldPrice == newPrice) return;

        long long oldKey = key(t, oldPrice);
        bucket[oldKey].erase(orderId);
        if (bucket[oldKey].empty()) bucket.erase(oldKey);

        info.second = newPrice;
        bucket[key(t, newPrice)].insert(orderId);
    }
    
    void cancelOrder(int orderId) {
        auto info = byId[orderId];
        int t = info.first;
        int price = info.second;

        byId.erase(orderId);

        long long k = key(t, price);
        bucket[k].erase(orderId);
        if (bucket[k].empty()) bucket.erase(k);

    }
    
    vector<int> getOrdersAtPrice(string orderType, int price) {
        int t = typeCode(orderType);
        long long k = key(t, price);

        vector<int> res;
        auto it = bucket.find(k);
        if (it == bucket.end()) return res;

        for (int id : it->second) res.push_back(id);
        return res;

    }
};

/**
 * Your OrderManagementSystem object will be instantiated and called as such:
 * OrderManagementSystem* obj = new OrderManagementSystem();
 * obj->addOrder(orderId,orderType,price);
 * obj->modifyOrder(orderId,newPrice);
 * obj->cancelOrder(orderId);
 * vector<int> param_4 = obj->getOrdersAtPrice(orderType,price);
 */