from app.controllers.db_controller import DatabaseConnection

def get_item_by_id(item_id: str):
    dbc = DatabaseConnection()
    result = dbc.get_item_by_id(item_id)
    return result