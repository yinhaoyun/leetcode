class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = minutes / 60
        hour_angle  = ((hour % 12) / 12) + (min_angle / 12)
        angle = abs((hour_angle - min_angle) * 360)
        if angle <= 180:
            return angle
        else:
            return 360 - angle


s = Solution()
print(s.angleClock(hour = 12, minutes = 30))  # 165
print(s.angleClock(hour = 3, minutes = 30))  # 75
print(s.angleClock(hour = 3, minutes = 15))  # 7.5
print(s.angleClock(hour = 4, minutes = 50))  # 155
