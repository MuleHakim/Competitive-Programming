class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for recipe, ingred in zip(recipes,ingredients): 
            indegree[recipe] = len(ingred)
            for i in ingred:
                graph[i].append(recipe)
                
        ans = []
        queue = deque(supplies)
        recipes = set(recipes)
        while queue: 
            node = queue.popleft()
            if node in recipes:
                ans.append(node)
            for neig in graph[node]: 
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    queue.append(neig)

        return ans 