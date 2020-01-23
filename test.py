import unittest


class TestRoutes(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        from app import app
        cls.app = app.test_client()
        
    def test_index_route(self):
        response = self.app.get('/') 
        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 

    def test_create_team_route(self):
        response = self.app.get('/created/teams')
        self.assertEqual(response.status_code, 200)
    
    def test_add_player_route(self):
        response = self.app.get('/player/new')
        self.assertEqual(response.status_code, 200)
    
    def test_team_new_route(self):
        response = self.app.get('/team/new')
        self.assertEqual(response.status_code, 200)
    
    def test_delete_team_route(self):
        response = self.app.get('/delete_team/<team_id>')
        self.assertEqual(response.status_code, 500)
    
    def test_edit_team_route(self):
        response = self.app.get('/edit_team/<team_id>')
        self.assertEqual(response.status_code, 500)
    
    def test_update_team_route(self):
        response = self.app.get('/update_team/<team_id>')
        self.assertEqual(response.status_code, 405)
   


if __name__ == '__main__':
    unittest.main()