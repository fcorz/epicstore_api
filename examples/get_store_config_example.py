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
    
    # Option 1: Provide sha256Hash explicitly
    sha256_hash = "f51a14bfd8e8969386e70f7c734c2671d9f61833021174e44723ddda9881739e"
    
    try:
        # Get store configuration with explicit hash
        config = api.get_store_config(sandbox_id, sha256_hash=sha256_hash)
        print('Store Config Response:\n', json.dumps(config, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f'Error: {e}')
    
    print("\n" + "="*50 + "\n")
    
    try:
        print("尝试不提供 sha256Hash（需要配置 hash_endpoint）...")
        # Option 2: Try to get hash from hash_endpoint (if configured)
        # This will fail if hash_endpoint is not configured
        config2 = api.get_store_config(sandbox_id)
        print('Store Config Response (from hash_endpoint):\n', json.dumps(config2, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f'Error (expected if hash_endpoint is not configured): {e}')


if __name__ == '__main__':
    main()

