from epicstore_api import EpicGamesStoreAPI, OfferData


def main() -> None:
    """Prints offer ID and developer for every offer of the first product in mapping."""
    api = EpicGamesStoreAPI(locale="zh-CN")
    namespace, slug = next(iter(api.get_product_mapping().items()))
    
    # Get product using IPv4 endpoint
    print(f"获取产品详情 (slug: {slug})...")
    first_product = api.get_product_ipv4(slug)
    print(f"产品名称: {first_product.get('productName', 'N/A')}")
    print(f"命名空间: {first_product.get('namespace', 'N/A')}\n")
    
    offers = [
        OfferData(page['namespace'], page['offer']['id'])
        for page in first_product.get('pages', [])
        if page.get('offer') and 'id' in page['offer']
    ]
    
    if offers:
        offers_data = api.get_offers_data(*offers)
        for offer_data in offers_data:
            data = offer_data['data']['Catalog']['catalogOffer']
            developer_name = ''
            for custom_attribute in data.get('customAttributes', []):
                if custom_attribute['key'] == 'developerName':
                    developer_name = custom_attribute['value']
            print('Offer ID:', data['id'], '\nDeveloper Name:', developer_name)
    else:
        print("未找到可用的offers")


if __name__ == '__main__':
    main()
