class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index_mapper = {
            val: i
            for i, val in enumerate(inorder)
        }
        preorder_index = 0

        def helper(left, right):
            nonlocal preorder_index
            if left > right :
                return 

            root_val = preorder[preorder_index]
            root = TreeNode(
                val=root_val
            )
            preorder_index += 1 

            index = index_mapper[
                root_val
            ]

            root.left = helper(
                left, index-1
            )
            root.right = helper(
                index+1, right
            )


            return root

        return helper(0, len(inorder)-1)