class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.allSnaps = []
        self.cur = dict()
        
    def set(self, index: int, val: int) -> None:
        self.cur[index] = val

    def snap(self) -> int:
        self.allSnaps.append(dict(self.cur))
        return len(self.allSnaps) - 1 

    def get(self, index: int, snap_id: int) -> int:
        snap = self.allSnaps[snap_id]
        return snap[index] if index in snap else 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)