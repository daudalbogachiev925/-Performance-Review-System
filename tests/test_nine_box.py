from src.nine_box import grid_position, nine_box_label

def test_top_talent():
    assert nine_box_label(*grid_position(5, 5)) == "Top Talent"

def test_underperformer():
    assert nine_box_label(*grid_position(1, 1)) == "Underperformer"
