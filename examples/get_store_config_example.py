"""Example: Get store configuration for a product."""

import json

from epicstore_api import EpicGamesStoreAPI


def main() -> None:
    """Print store configuration for a product."""
    # Initialize API (you can optionally configure hash_endpoint)
    # api = EpicGamesStoreAPI(locale="zh-CN", hash_endpoint="https://your-hash-service.com/api/hash")
    api = EpicGamesStoreAPI(locale="zh-CN")
    
    # Example sandbox ID from the requirement document
    # 通常是游戏的 namespace 或者 offer_id 对应的值
    sandbox_id = "b4bb52a95d0b43d9af543c6ec3c54e04"
    
    try:
        # Get store configuration
        config = api.get_store_config(sandbox_id)
        print('Store Config Response:\n', json.dumps(config, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()

