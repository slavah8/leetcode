class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        sorted_characters = sorted(properties, key = lambda x: (-x[0], x[1]))
        print(sorted_characters)

        weak = 0
        max_defense = -1
        # we know their attack is bigger so we can just compare the defense
        for atk, df in sorted_characters:
            if max_defense > df:
                weak += 1
            max_defense = max(max_defense, df)
        return weak
