public class Codec {

    private final Map<String, String> codeToUrl = new HashMap<>(); // short : long
    private int id = 0;
    private final String base = "http://tinyurl.com/";

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        String code = String.valueOf(id++);
        codeToUrl.put(code, longUrl);
        return base + code;

    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        String code = shortUrl.substring(base.length());
        return codeToUrl.get(code);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));