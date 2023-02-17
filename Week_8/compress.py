class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2: return len(chars)
        left, right = 0, 0
        while right < len(chars):
		
            chars[left] = chars[right]
            count = 1
			
            while right + 1 < len(chars) and chars[right] == chars[right + 1]:
                right += 1
                count += 1
			
            if count > 1:
                for cnt in str(count):
                    chars[left + 1] = cnt
                    left += 1
            
            right += 1
            left += 1
        
        return left
