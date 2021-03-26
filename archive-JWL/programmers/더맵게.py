import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0]<K and len(scoville)>1:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1+min2*2)
        answer+=1
    if scoville[0]<K and len(scoville)==1 :
        answer = -1
    return answer

# 첫번째 풀이
# def solution(scoville, K):
#     answer = 0
#     sorted(scoville)
#     while(scoville[0]<K and len(scoville)>1):
#         new_scov = scoville[0] + scoville[1]*2
#         scoville.pop(0)
#         scoville.pop(0)
#
#         for i, scov in enumerate(scoville):
#             if scov > new_scov:
#                 scoville.insert(i,new_scov)
#                 new_scov = -1
#                 break
#         if new_scov != -1:
#             scoville.append(new_scov)
#         answer+=1
#     if(len(scoville)==1 and scoville[0] < K):
#         answer = -1
#     return answer