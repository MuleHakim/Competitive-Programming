class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        domainDict = defaultdict(int)
        result = []

        for domain in cpdomains:

            length = len(domain)
            ind = domain.index(" ")

            for index in range(length - 1, -1, -1):

                if domain[index] == ".":
                    domainDict[domain[index + 1:]] += int(domain[:ind])

                elif domain[index] == " ":
                    domainDict[domain[index + 1:]] += int(domain[:ind])
                    break

        for dom in domainDict:

            eachOutput = str(domainDict[dom]) + " " + dom
            result.append(eachOutput)

        return result
