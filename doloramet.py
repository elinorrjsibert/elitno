def get_track_info(num_tracks, leadout_offset, offsets):
    return (1, num_tracks, leadout_offset) + offsets

# Example usage:
num_tracks = 12
leadout_offset = 150
offsets = (100, 200, 300)
result = get_track_info(num_tracks, leadout_offset, offsets)
print(result)  # Output: (1, 12, 150, 100, 200, 300)
