"""Example: Get video information by video ID and retrieve mediaRefId.

The video_id can be extracted from fetch_store_games response.
In the response, video URLs are in the format:
"com.epicgames.video://{video_id}?cover=..."

Example response from fetch_store_games:
{
    "type": "heroCarouselVideo",
    "url": "com.epicgames.video://6e8b6bc1-825e-4d09-acb2-a4c4e99a6856?cover=https%3A%2F%2Fcdn1.epicgames.com%2F..."
}

The video_id is the part between "com.epicgames.video://" and "?"
"""

import json
import re

from epicstore_api import EpicGamesStoreAPI


def extract_video_id(video_url: str) -> str | None:
    """Extract video_id from video URL.
    
    :param video_url: Video URL in format "com.epicgames.video://{video_id}?cover=..."
    :return: Video ID or None if not found
    """
    match = re.search(r'com\.epicgames\.video://([^?]+)', video_url)
    if match:
        return match.group(1)
    return None


def main() -> None:
    """Print video information by video ID."""
    # Initialize API
    api = EpicGamesStoreAPI(locale="zh-Hant")
    
    # Example video ID (from the URL example)
    video_id = "6e8b6bc1-825e-4d09-acb2-a4c4e99a6856"
    
    # Option 1: Provide sha256Hash explicitly
    sha256_hash = "52dbe3764aa1012313360dbbfaf2b550975edd7f30c2427ad00495c269646003"
    
    try:
        print(f"获取视频信息 (videoId: {video_id})...")
        # Get video information with explicit hash
        video = api.get_video_by_id(video_id, sha256_hash=sha256_hash)
        print('Video Response:\n', json.dumps(video, indent=4, ensure_ascii=False))
        
        # Extract mediaRefId if available
        if 'data' in video and 'Video' in video['data']:
            fetch_video_by_locale = video['data']['Video'].get('fetchVideoByLocale', [])
            if fetch_video_by_locale:
                print('\n媒体引用ID列表 (mediaRefIds):')
                for item in fetch_video_by_locale:
                    print(f"  Recipe: {item.get('recipe')}, MediaRefId: {item.get('mediaRefId')}")
    except Exception as e:
        print(f'Error: {e}')
    
    print("\n" + "="*50 + "\n")
    
    # Example: Extract video_id from fetch_store_games response
    try:
        print("示例：从 fetch_store_games 响应中提取 video_id...")
        # Example video URL from fetch_store_games response
        example_video_url = "com.epicgames.video://6e8b6bc1-825e-4d09-acb2-a4c4e99a6856?cover=https%3A%2F%2Fcdn1.epicgames.com%2Fspt-assets%2F3ac65ef5cdf44b8084fcac818002635f%2Feleven-video-tlx3p.png"
        extracted_id = extract_video_id(example_video_url)
        if extracted_id:
            print(f"从 URL 提取的 video_id: {extracted_id}")
            print(f"使用提取的 video_id 获取视频信息...")
            video2 = api.get_video_by_id(extracted_id, sha256_hash=sha256_hash)
            if 'data' in video2 and 'Video' in video2['data']:
                fetch_video_by_locale = video2['data']['Video'].get('fetchVideoByLocale', [])
                if fetch_video_by_locale:
                    print('媒体引用ID列表 (mediaRefIds):')
                    for item in fetch_video_by_locale:
                        print(f"  Recipe: {item.get('recipe')}, MediaRefId: {item.get('mediaRefId')}")
    except Exception as e:
        print(f'Error: {e}')
    
    print("\n" + "="*50 + "\n")
    
    try:
        print("尝试不提供 sha256Hash（需要配置 hash_endpoint）...")
        # Option 2: Try to get hash from hash_endpoint (if configured)
        # This will fail if hash_endpoint is not configured
        video3 = api.get_video_by_id(video_id)
        print('Video Response (from hash_endpoint):\n', json.dumps(video3, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f'Error (expected if hash_endpoint is not configured): {e}')


if __name__ == '__main__':
    main()

