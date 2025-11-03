"""Example: Get product offer details by product ID and offer ID."""

import json

from epicstore_api import EpicGamesStoreAPI


def main() -> None:
    """Print product offer details by product ID and offer ID."""
    # Initialize API with locale and country
    api = EpicGamesStoreAPI(locale="zh-CN", country="TW")
    
    # Example product ID and offer ID
    product_id = "3ac65ef5cdf44b8084fcac818002635f"
    offer_id = "cb49140c3c11429589ab22fd75c41504"
    
    try:
        # Get product offer details by product ID and offer ID
        offer = api.get_product_offer_by_id(product_id, offer_id)
        print('Product Offer Details Response:\n', json.dumps(offer, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()

