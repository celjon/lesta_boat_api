class Rowboat:
    def __init__(self):
        self.is_moving = False
        self.direction = None
        self.passengers = 0

    def row_forward(self):
        self.is_moving = True
        self.direction = "forward"
        return "The boat is moving forward"

    def row_backward(self):
        self.is_moving = True
        self.direction = "backward"
        return "The boat is moving backward"

    def stop(self):
        self.is_moving = False
        self.direction = None
        return "The boat has stopped"

    def board_passenger(self):
        self.passengers += 1
        return f"Passenger boarded. Current count: {self.passengers}"

    def leave_passenger(self):
        if self.passengers > 0:
            self.passengers -= 1
            return f"Passenger left the boat. Remaining: {self.passengers}"
        return "No passengers to leave"


if __name__ == "__main__":
    boat = Rowboat()

    print(boat.row_forward())  # The boat is moving forward
    print(boat.stop())  # The boat has stopped
    print(boat.board_passenger())  # Passenger boarded. Current count: 1
    print(boat.leave_passenger())  # Passenger left the boat. Remaining: 0
    print(boat.leave_passenger())  # No passengers to leave
