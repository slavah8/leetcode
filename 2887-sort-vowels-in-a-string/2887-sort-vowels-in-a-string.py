class Solution:
    def sortVowels(self, s: str) -> str:
        
        counts = collections.Counter()
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        for char in s:
            if char not in vowels:
                continue
            counts[char] += 1

        sorted_counts = dict(sorted(counts.items(), key = lambda x: ord(x[0])))
        print(sorted_counts)

        result = []
        for char in s:
            if char not in vowels:
                result.append(char)
            else:
                for vowel, count in sorted_counts.items():
                    result.append(vowel)
                    sorted_counts[vowel] -= 1
                    if sorted_counts[vowel] == 0:
                        del sorted_counts[vowel]
                    break
        return ''.join(result)
            