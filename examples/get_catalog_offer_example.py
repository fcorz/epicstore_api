"""Example: Get catalog offer details.

Note: This method returns the short description (短描述) of the product.
For long description (长描述) content, please use other methods.
"""

import json

from epicstore_api import EpicGamesStoreAPI


def main() -> None:
    """Print catalog offer details."""
    # Initialize API
    api = EpicGamesStoreAPI(locale="zh-CN", country="TW")
    
    # Example offer ID and sandbox ID from the URL
    offer_id = "f506d29d55bb4c72b8d57fd9857b2be4"
    sandbox_id = "94cec4802e954a6c9579e29e8b817f3a"
    
    # Option 1: Provide sha256Hash explicitly
    sha256_hash = "abafd6e0aa80535c43676f533f0283c7f5214a59e9fae6ebfb37bed1b1bb2e9b"
    
    try:
        print(f"获取 catalog offer (offerId: {offer_id}, sandboxId: {sandbox_id})...")
        # Get catalog offer with explicit hash
        offer = api.get_catalog_offer(
            offer_id=offer_id,
            sandbox_id=sandbox_id,
            sha256_hash=sha256_hash,
        )
        print('Catalog Offer Response:\n', json.dumps(offer, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f'Error: {e}')
    
    print("\n" + "="*50 + "\n")
    
    try:
        print("尝试不提供 sha256Hash（需要配置 hash_endpoint）...")
        # Option 2: Try to get hash from hash_endpoint (if configured)
        # This will fail if hash_endpoint is not configured
        offer2 = api.get_catalog_offer(
            offer_id=offer_id,
            sandbox_id=sandbox_id,
            # sha256_hash not provided, will try to get from hash_endpoint
        )
        print('Catalog Offer Response (from hash_endpoint):\n', json.dumps(offer2, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f'Error (expected if hash_endpoint is not configured): {e}')


if __name__ == '__main__':
    main()

