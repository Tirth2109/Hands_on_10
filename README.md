

This repository provides Python implementations for three fundamental tree data structures: Binary Search Tree (BST), Red-Black Tree (RBT), and AVL Tree. Each structure includes the core operations typically associated with tree data structures—namely, insertion, deletion, searching, and traversal. 

The **Binary Search Tree (BST)** supports insertion of nodes while maintaining the inherent order property, ensuring each node fits the left-child/right-child relationship. Deletion involves removing nodes and restructuring as necessary to maintain the BST property, while search functionality allows users to check for the existence of specific values. In-order traversal is available, which outputs the nodes in sorted order, providing an efficient way to access the tree's contents in a sequence.

The **Red-Black Tree (RBT)**, a balanced tree structure, maintains its unique properties by enforcing rules during insertion and deletion operations, allowing it to balance itself automatically. The RBT implementation ensures that each insertion keeps the red-black properties intact, and deletion operations preserve the tree’s balance by following red-black rules. Searching for specific values and performing in-order traversal are also supported, allowing users to check for the presence of elements and display the tree's contents in order.

The **AVL Tree**, another self-balancing structure, automatically rebalances after insertions and deletions to ensure efficient access times. Insertion in the AVL Tree adjusts the tree as needed to maintain height balance, and deletion does the same to prevent height imbalances. Like the other trees, the AVL Tree supports search operations and in-order traversal to output elements in sorted order, ensuring quick access and efficient organization of elements.

To use this repository, simply clone it to your machine. Running the main script initiates test cases for each type of tree, demonstrating the primary functionalities of each structure. These tests cover various scenarios, including insertion of multiple values, deletion of specific nodes, and searching for existing or non-existing elements. In-order traversal output can also be observed in these tests, providing a way to verify the correct ordering of elements.

Overall, this repository serves as an effective introduction to tree data structures in Python, providing hands-on implementations of the essential operations associated with Binary Search Trees, Red-Black Trees, and AVL Trees. These implementations are designed to highlight the unique properties and functionalities of each structure, making this resource valuable for anyone looking to deepen their understanding of tree data structures in computer science.

