class Node:
    def __init__(self, game):
        self.game = game
        self.left = None
        self.right = None

class GameBST:
    def __init__(self):
        self.root = None

    def insert(self, game):
        new_node = Node(game)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if game.platform.lower() < current.game.platform.lower():
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def in_order(self):
        result = []

        def _in_order(node):
            if node is not None:
                _in_order(node.left)
                result.append(node.game)
                _in_order(node.right)

        _in_order(self.root)
        return result

    def search_by_platform(self, platform):
        platform = platform.lower()
        matches = []

        def _search(node):
            if node is None:
                return
            if platform < node.game.platform.lower():
                _search(node.left)
            elif platform > node.game.platform.lower():
                _search(node.right)
            else:
                # equal platform: check both sides for duplicates
                matches.append(node.game)
                _search(node.left)
                _search(node.right)

        _search(self.root)
        return matches
