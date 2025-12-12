class Bank {

    private final long[] bal;
    private final int n;

    public Bank(long[] balance) {
        this.bal = balance;
        this.n = balance.length;    
    }
    
    private boolean valid(int account) {
        return account >= 1 && account <= n; 
    }
    public boolean transfer(int account1, int account2, long money) {
        if (!valid(account1) || !valid(account2)) {
            return false;
        }
        int a = account1 - 1;
        int b = account2 - 1;

        if(bal[a] < money) {
            return false;
        }
        bal[a] -= money;
        bal[b] += money;
        return true;
    }
    
    public boolean deposit(int account, long money) {
        if (!valid(account)) {
            return false;
        }
        int i = account - 1;
        bal[i] += money;
        return true;
        
    }
    
    public boolean withdraw(int account, long money) {
        if (!valid(account)) {
            return false;
        }
        int i = account - 1;
        if (bal[i] < money) {
            return false;
        }
        bal[i] -= money;
        return true;
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */