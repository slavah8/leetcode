class Cashier {

    private final int n;
    private final int discount;
    private int count = 0;
    private final Map<Integer, Integer> priceMap = new HashMap<>();

    public Cashier(int n, int discount, int[] products, int[] prices) {
        this.n = n;
        this.discount = discount;

        for (int i = 0; i < products.length; i++) {
            priceMap.put(products[i], prices[i]);
        }    
    }
    
    public double getBill(int[] product, int[] amount) {
        count++;

        double subtotal = 0.0;

        for (int i = 0; i < product.length; i++) {
            int price = priceMap.get(product[i]);
            subtotal += (double) price * amount[i];
        }

        if (count % n == 0) {
            subtotal = subtotal * (100 - discount) / 100.0;
        }
        return subtotal;
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * Cashier obj = new Cashier(n, discount, products, prices);
 * double param_1 = obj.getBill(product,amount);
 */