# solved by satyam kumar
# question link https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        dict={1000:'M',
              900:'CM',
              500:'D',
              400:'CD',
              100:'C',
              90:'XC',
              50:'L',
              40:'XL',
              10:'X',
              9:'IX',
              5:'V',
              4:'IV',
              1:'I'}
        lst=[*dict.keys()]
        print(lst)
        ret_str=''
        for i,n in enumerate(str(num)):
            
            new=n + (len(str(num))-1-i)*'0'
            print(new)
            while int(new)!=0:
                if int(new) in lst:
                    ret_str=ret_str+dict[int(new)]
                    new='0'
                else:
                    for key in lst:
                        if int(new)>key:
                            ret_str=ret_str+dict[key]
                            new=str(int(new)-key)
                            break
                print(ret_str)
                            
                            



        return ret_str
        