class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c2 = Counter(t)
        c1 = {}
        mn = float('inf')
        rep = ''
        l = h = 0
        for r in range(len(s)):
            if s[r] not in c2:
                continue
            # ajouter freq de s[r] dand c1
            if s[r] in c1:
                c1[s[r]] += 1
            else:
                c1[s[r]] = 1
            
            if c1[s[r]] == c2[s[r]]:
                h += 1
            #print(h, c1, c2)
            #valide
            while (l < len(s) and h == len(c2)):
                if r - l + 1 < mn:
                    mn = r - l + 1
                    rep = s[l : r + 1]
                #supprimer s[l] 
                if s[l] in c1:
                    c1[s[l]] -= 1
                    if c1[s[l]] < c2[s[l]]:
                        h -= 1
                l += 1  
        return rep