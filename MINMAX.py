import math
def minimax(curdepth,nodeindex,maxturn,scores,targetdepth):
    if curdepth==targetdepth :
        return scores[nodeindex]
    if maxturn:
        return max(minimax(curdepth+1,nodeindex*2,False,scores,targetdepth),
                   minimax(curdepth+1,nodeindex*2+1,False,scores,targetdepth),
                   minimax(curdepth+1,nodeindex*2+2,False,scores,targetdepth))
    else:
        return min(minimax(curdepth+1,nodeindex*2,True,scores,targetdepth),
                   minimax(curdepth+1,nodeindex*2+1,True,scores,targetdepth),
                   minimax(curdepth+1,nodeindex*2+2,True,scores,targetdepth))
    
scores=[10,-3,-19,11,11,0,-2,-2,-2,14,-16,2,17,15,-14,15,-15,13,-19,-9,4,-9,2,9,-14,2,-18]
treedepth=math.log(len(scores),3)
print("The optimal move is",minimax(0,0,True,scores,treedepth))
