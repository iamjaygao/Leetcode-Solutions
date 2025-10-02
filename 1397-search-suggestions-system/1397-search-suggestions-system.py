class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            start = bisect.bisect_left(products, prefix)
            res = []
            for i in range(start, min(start+3, len(products))):
                if products[i].startswith(prefix):
                    res.append(products[i])
                else:
                    break
            ans.append(res)
        return ans

        