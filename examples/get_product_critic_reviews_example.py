"""Example: Get critic reviews (OpenCritic) for a product by product ID."""

import json

from epicstore_api import EpicGamesStoreAPI


def main() -> None:
    """Print critic reviews for a product."""
    # Initialize API
    api = EpicGamesStoreAPI(locale="zh-Hant")
    
    # Example product ID from the URL
    product_id = "d42d7101bb7a41c09a810ee418b7d3d0"
    
    try:
        print(f"获取产品评论分数 (productId: {product_id})...")
        # Get critic reviews with default parameters (count=3, start=0)
        reviews = api.get_product_critic_reviews(product_id)
        print('Critic Reviews Response:\n', json.dumps(reviews, indent=4, ensure_ascii=False))
        
        # Extract and display review scores if available
        if isinstance(reviews, dict):
            # Try to find review scores in the response
            if 'data' in reviews:
                print('\n评论数据:')
                print(json.dumps(reviews['data'], indent=2, ensure_ascii=False))
            elif 'reviews' in reviews:
                print(f'\n找到 {len(reviews.get("reviews", []))} 条评论')
                for idx, review in enumerate(reviews.get('reviews', []), 1):
                    print(f'\n评论 {idx}:')
                    print(json.dumps(review, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f'Error: {e}')
    
    print("\n" + "="*50 + "\n")
    
    try:
        print("尝试获取更多评论 (count=10, start=0)...")
        # Get more reviews
        reviews2 = api.get_product_critic_reviews(product_id, count=10, start=0)
        print('Critic Reviews Response (count=10):\n', json.dumps(reviews2, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()

