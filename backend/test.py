import json
import unittest
from app import app

class GraphQLApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.headers = {'Content-Type': 'application/json'}
    
    def test_query_products(self):
        query = '''
        query {
            products {
                id
                name
                price
                stock
                available
            }
        }
        '''
        response = self.client.post('/graphql', headers=self.headers, data=json.dumps({'query': query}))
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn('data', data)
        self.assertIn('products', data['data'])
        self.assertIsInstance(data['data']['products'], list)
        for product in data['data']['products']:
            self.assertIn('id', product)
            self.assertIn('name', product)
            self.assertIn('price', product)
            self.assertIn('stock', product)
            self.assertIn('available', product)

    def test_modify_stock_mutation(self):
        mutation = '''
        mutation {
            modifyStock(id: 1, stock: 5) {
                product {
                    id
                    stock
                    available
                }
            }
        }
        '''
        response = self.client.post('/graphql', headers=self.headers, data=json.dumps({'query': mutation}))
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn('data', data)
        self.assertIn('modifyStock', data['data'])
        product = data['data']['modifyStock']['product']
        self.assertEqual(product['id'], 1)
        self.assertIsInstance(product['stock'], int)
        self.assertIn(product['available'], [True, False])

    def test_invalid_query(self):
        invalid_query = 'products { id name }'
        response = self.client.post('/graphql', headers=self.headers, data=json.dumps({'query': invalid_query}))
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn('errors', data)

    def test_missing_query_field(self):
        response = self.client.post('/graphql', headers=self.headers, data=json.dumps({}))
        self.assertEqual(response.status_code, 400)

        data = response.get_json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Falta la consulta GraphQL')


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(GraphQLApiTestCase)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n\n===== RESUMEN DE RESULTADOS =====")
    print(f"Tests ejecutados: {result.testsRun}")
    print(f"Tests fallidos: {len(result.failures)}")
    print(f"Tests con error: {len(result.errors)}")

    if result.wasSuccessful():
        print("¡Todos los tests pasaron correctamente! ✅")
    else:
        print("Algunos tests fallaron o tuvieron errores. ❌")
