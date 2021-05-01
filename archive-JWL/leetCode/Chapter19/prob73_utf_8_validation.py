class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i=0
        res = True
        temp = 0
        while i < len(data):
            
            temp = self.checkPrimaryBytes(data,i)
            
            if temp>=0:
                temp1 = self.checkAdditionalBytes(data,i,temp)
                
                if temp1==True:
                    i+=temp
                else:
                    res = False
                    break
            else:
                res = False
                break
            i+=1
        return res
    
    def checkPrimaryBytes(self,data: List[int],idx: int)-> int:
        temp = "{0:b}".format(data[idx]).zfill(8)
        
        res = -1
        if temp[0] == "0":
            res = 0
        if temp[0:3]=="110":
            res = 1
        if temp[0:4]=="1110":
            res = 2
        if temp[0:5]=="11110":
            res = 3
        return res
    
    def checkAdditionalBytes(self,data: List[int],idx: int,num: int)->bool:
        res = True
        if(idx+num<len(data)):
            for i in range(1,num+1):
                if "{0:b}".format(data[idx+i]).zfill(8)[:2] != "10":
                    res = False
                    break
        else:
            res = False
        return res
            
