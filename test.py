import unittest
from example import get_neighboring_states

class TestNeighboringStatesApp(unittest.TestCase):
    def test_app_startup(self):
        """
        Test that the application can import and run basic functions
        """
        # If this test passes, it means the app can be imported without errors
        self.assertIsNotNone(get_neighboring_states, "Function get_neighboring_states should exist")

    def test_florida_neighbors(self):
        """
        Test that Florida has the correct neighboring states
        """
        florida_neighbors = get_neighboring_states("FLORIDA")
        
        # Expected neighbors of Florida
        expected_neighbors = ['Georgia', 'Alabama']
        
        # Check that the expected neighbors are in the result
        for neighbor in expected_neighbors:
            self.assertIn(neighbor, florida_neighbors, 
                          f"{neighbor} should be a neighbor of Florida")
        
        # Optional: Check the number of neighbors
        self.assertGreaterEqual(len(florida_neighbors), 2, 
                                "Florida should have at least 2 neighboring states")

    def test_state_name_case_insensitivity(self):
        """
        Test that the function works with different input case variations
        """
        variations = ["FLORIDA", "Florida", "florida"]
        
        for variation in variations:
            neighbors = get_neighboring_states(variation)
            self.assertTrue(len(neighbors) > 0, 
                            f"Should return neighbors for input: {variation}")

if __name__ == '__main__':
    unittest.main()