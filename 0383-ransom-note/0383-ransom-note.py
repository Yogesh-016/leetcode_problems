class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            # If the character isn't in the magazine, we can't build the note
            if char not in magazine:
                return False
            # Remove the used character from the magazine (only once)
            magazine = magazine.replace(char, "", 1)
        
        return True