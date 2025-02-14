import pytest
from rowing_boat import Rowboat

@pytest.fixture
def boat():
    return Rowboat()

def test_row_forward(boat):
    assert boat.row_forward() == "The boat is moving forward"
    assert boat.is_moving is True
    assert boat.direction == "forward"

def test_row_backward(boat):
    assert boat.row_backward() == "The boat is moving backward"
    assert boat.is_moving is True
    assert boat.direction == "backward"

def test_stop(boat):
    boat.row_forward()
    assert boat.stop() == "The boat has stopped"
    assert boat.is_moving is False
    assert boat.direction is None

def test_board_passenger(boat):
    assert boat.board_passenger() == "Passenger boarded. Current count: 1"
    assert boat.passengers == 1

def test_leave_passenger(boat):
    boat.board_passenger()
    assert boat.leave_passenger() == "Passenger left the boat. Remaining: 0"
    assert boat.passengers == 0

def test_leave_passenger_empty(boat):
    assert boat.leave_passenger() == "No passengers to leave"
