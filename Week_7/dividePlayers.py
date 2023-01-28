class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        pre_team = skill[0] + skill[-1]
        sum_teams = 0
        left, right = 0, len(skill) - 1
        
        while left <= right:
            if skill[left] + skill[right] != pre_team:
                return -1
            sum_teams += skill[left] * skill[right]
            left += 1
            right -= 1
            
        return sum_teams
        
