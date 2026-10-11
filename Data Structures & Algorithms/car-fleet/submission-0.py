class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(
            zip(position, speed), reverse=True
        )

        fleet = 0 
        time_fleet = 0 
        for p, s in cars:
            time = (target - p)/s
            if time > time_fleet:
                time_fleet = time
                fleet += 1 
            
        return fleet


        