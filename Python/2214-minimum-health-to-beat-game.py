class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage) + max(max(damage) - armor, 0) - max(damage) + 1