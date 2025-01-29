class MiniMaxAgent:
    def __init__(self, state_space_graph, start_node):
        self.state_space_graph = state_space_graph
        self.start_node = start_node
    
    def minimax(self, node, depth, maximizing_player):
        # Base case: if we reach a leaf node or max depth, return the utility value
        if not self.state_space_graph[node]['neighbors'] or depth == 0:
            return self.state_space_graph[node]['utility'] if self.state_space_graph[node]['utility'] is not None else 0
        
        if maximizing_player:
            max_eval = float('-inf')
            for neighbor in self.state_space_graph[node]['neighbors']:
                eval = self.minimax(neighbor, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for neighbor in self.state_space_graph[node]['neighbors']:
                eval = self.minimax(neighbor, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval
    
    def best_destination(self):
        # Determine the best destination by running the minimax search from the start node
        best_value = float('-inf')
        best_node = self.start_node
        
        for neighbor in self.state_space_graph[self.start_node]['neighbors']:
            node_value = self.minimax(neighbor, 3, False)  # Depth of 3 is arbitrarily chosen for this example
            if node_value > best_value:
                best_value = node_value
                best_node = neighbor
        
        return best_node, best_value


# Figure 4

state_space_graph4 = {
"Shambu": {
    "neighbors":["Gedo"],
    "utility": 4
    },
"Fincha": {
    "neighbors":["Gedo"],
    "utility": 5
    },
"Gedo": {
    "neighbors":["Shambu", "Fincha", "Ambo"],
    "utility": None
    },
"Gimbi": {
    "neighbors":["Nekemte"],
    "utility": 8},
"Ambo": {
    "neighbors":["Gedo", "Nekemte", "Addis Ababa"],
    "utility": None
    },
"Addis Ababa": {
    "neighbors":["Ambo", "Buta Jirra", "Adama"],
    "utility": None
    },
"Nekemte": {
    "neighbors":["Gimbi", "Limu", "Ambo"],
    "utility": None
    },
"Limu": {
    "neighbors":["Nekemte"],
    "utility": 8
    },
"Adama": {
    "neighbors":["Addis Ababa", "Mojo", "Dire Dawa"],
    "utility": None
    },
"Buta Jirra": {
    "neighbors":["Addis Ababa", "Worabe", "Wolkite"],
    "utility": None
    },
"Dire Dawa": {
    "neighbors":["Adama", "Harar", "Chiro"],
    "utility": None},
"Harar": {
    "neighbors":["Dire Dawa"],
    "utility": 10
    },
"Chiro": {
    "neighbors":["Dire Dawa"],
    "utility": 6
    },
"Worabe": {
    "neighbors":["Buta Jirra", "Hossana", "Durame"],
    "utility": None
    },
"Wolkite": {
    "neighbors":["Buta Jirra", "Bench Maji", "Tepi"],
    "utility": None
    },
"Hossana": {
    "neighbors":["Worabe"],
    "utility": 6
    },
"Durame": {
    "neighbors":["Worabe"],
    "utility": 5
    },
"Bench Maji": {
    "neighbors":["Wolkite"],
    "utility": 5
    },
"Tepi": {
    "neighbors":["Wolkite"],
    "utility": 6
    },
"Mojo": {
    "neighbors":["Adama", "Kaffa", "Dilla"],
    "utility": None
    },
"Kaffa": {
    "neighbors":["Mojo"],
    "utility": 7
    },
"Dilla": {
    "neighbors":["Mojo"], 
    "utility": 9
    }
}

# Initialize the agent
start_state = input("Enter intial state: ")
agent = MiniMaxAgent(state_space_graph4, start_state)

# Get the best destination based on MiniMax search
best_destination, utility = agent.best_destination()
print(f"The best route from {start_state} to {best_destination} is with a utility of {utility}.")

