
from main import add_parcel, track_parcel

def test_add_parcel():
    parcel = add_parcel("P101", "Shipped")
    assert parcel["parcel_id"] == "P101"

def test_track_parcel():
    parcel = add_parcel("P101", "Delivered")
    assert track_parcel(parcel) == "Delivered"
