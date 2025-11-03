"""Example: Get product details by product ID."""

import json

from epicstore_api import EpicGamesStoreAPI


def main() -> None:
    """Print product details by product ID."""
    # Initialize API with locale and country
    api = EpicGamesStoreAPI(locale="zh-CN", country="TW")
    
    # Example product ID
    product_id = "3ac65ef5cdf44b8084fcac818002635f"
    
    try:
        # Get product details by product ID
        product = api.get_product_by_id(product_id)
        print('Product Details Response:\n', json.dumps(product, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()

