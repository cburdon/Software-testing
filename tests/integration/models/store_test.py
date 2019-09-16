from models.store import StoreModel
from models.item import ItemModel
from tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')

        self.assertListEqual(store.items.all(), [],
                             "The store's items length was not 0 even though no items were added.")

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')

            self.assertIsNone(StoreModel.find_by_name('test'),
                              "The store exists when it should not.")

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test'),
                                 "The store doesn't exist in the db when it should have been created.")

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test'),
                              "The store exists when it should have been deleted from the database.")

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1,
                             "The item didn't get added to the store relationship.")

            self.assertEqual(store.items.first().name, 'test_item',
                             'The item name does not match the first item on the store inventory.')

    def test_store_json(self):
        store = StoreModel('test')

        expected = {
            'id': None,
            'name': 'test',
            'items': []
            }

        self.assertDictEqual(store.json(), expected,
                             "the JSON file of the store and with no items does not match the expected value.")

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'id': 1,
                'name': 'test',
                'items': [{'name': 'test_item', 'price': 19.99}]
            }

            self.assertDictEqual(store.json(), expected,
                                 "the JSON file of the store and its items does not match the expected value.")


