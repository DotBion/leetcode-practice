class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        nointervals = []
        nointervals.append(intervals[0])
        
        starti = 0
        endi = 1
        #l = len(nointervals)
        for i in range(1,len(intervals)) :
            #l = len(nointervals)
            #if (nointervals[l-1][starti]<=intervals[i][starti] and  intervals[i][starti]<=nointervals[l-1][endi]) or (intervals[i][starti]<=nointervals[l-1][starti] and nointervals[l-1][starti]<=intervals[i][endi]):
            if intervals[i][starti]<=nointervals[-1][endi] :
                nointervals[-1][endi] = max(nointervals[-1][endi], intervals[i][endi])



                # newinterval = nointervals.pop()
                # newstart = min(intervals[i][starti],newinterval[starti])
                # newend = max(intervals[i][endi],newinterval[endi])
                # newinterval = [newstart,newend]
                # nointervals.append(newinterval)
            else :
                nointervals.append(intervals[i])
        return nointervals
