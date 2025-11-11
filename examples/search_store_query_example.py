"""Example: Search store products using searchStoreQuery."""

import json

from epicstore_api import EpicGamesStoreAPI


def main() -> None:
    """Print search results for store products."""
    # Initialize API
    api = EpicGamesStoreAPI(locale="zh-Hant", country="TW")
    
    # Option 1: Provide sha256Hash explicitly
    sha256_hash = "7d58e12d9dd8cb14c84a3ff18d360bf9f0caa96bf218f2c5fda68ba88d68a437"
    
    try:
        print("搜索商店产品（使用默认参数获取全部）...")
        # Search store with default parameters (gets all categories)
        results = api.search_store_query(
            count=40,
            start=0,
            sha256_hash=sha256_hash,
        )
        print('Search Results Response:\n', json.dumps(results, indent=4, ensure_ascii=False))
        
        # Extract and display product information if available
        if isinstance(results, dict):
            if 'data' in results and 'Catalog' in results['data']:
                search_store = results['data']['Catalog'].get('searchStore', {})
                elements = search_store.get('elements', [])
                print(f'\n找到 {len(elements)} 个产品')
                if elements:
                    print('\n前3个产品:')
                    for idx, product in enumerate(elements[:3], 1):
                        print(f'\n产品 {idx}:')
                        print(f"  ID: {product.get('id', 'N/A')}")
                        print(f"  标题: {product.get('title', 'N/A')}")
                        print(f"  命名空间: {product.get('namespace', 'N/A')}")
    except Exception as e:
        print(f'Error: {e}')
    
    print("\n" + "="*50 + "\n")
    
    try:
        print("尝试使用自定义参数...")
        # Search with custom parameters
        results2 = api.search_store_query(
            category="games/edition/base|bundles/games",
            count=20,
            start=0,
            sort_by="releaseDate",
            sort_dir="DESC",
            keywords="",
            tag="",
            allow_countries="TW",
            with_price=True,
            sha256_hash=sha256_hash,
        )
        print('Search Results Response (custom):\n', json.dumps(results2, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f'Error: {e}')
    
    print("\n" + "="*50 + "\n")
    
    try:
        print("尝试不提供 sha256Hash（需要配置 hash_endpoint）...")
        # Option 2: Try to get hash from hash_endpoint (if configured)
        # This will fail if hash_endpoint is not configured
        results3 = api.search_store_query(
            count=10,
            start=0,
        )
        print('Search Results Response (from hash_endpoint):\n', json.dumps(results3, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f'Error (expected if hash_endpoint is not configured): {e}')


if __name__ == '__main__':
    main()

