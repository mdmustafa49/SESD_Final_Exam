
def add_parcel(parcel_id, status):
    return {
        "parcel_id": parcel_id,
        "status": status
    }

def track_parcel(parcel):
    return parcel["status"]
