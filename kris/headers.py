def Headers(site_brand):
    if 'taobao' == site_brand:
        headers = {
            'authority': 's.taobao.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'sec-fetch-user': '?1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'referer': 'https://www.taobao.com/?spm=a230r.1.0.0.18434f0fZ0XBOG',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'cookie': 'thw=cn; v=0; cna=ba/BFhNadHgCARsSEUxw1LSm; cookie2=1e442ba61c5425457fbebe075e26de5f; t=add1e52914eb6b2016ee6d22120993af; _tb_token_=71ee7533e5de4; _samesite_flag_=true; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&id2=UoLfdCpv5t6I&nk2=0%2BFaWwjTPm8%3D&vt3=F8dBxdsXGDvOYjaB7kg%3D; csg=6c8ad4c6; lgc=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; dnk=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; skt=c149b9211e8c32ee; existShop=MTU4MDkxMjY2MA%3D%3D; uc4=id4=0%40UOrptUgWFjW%2BSDCzGvbpHBpU%2BNI%3D&nk4=0%400VoIkNFbMLOWIlARu3ield73yQ%3D%3D; tracknick=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; enc=WmrrgcHnzMECUXK5Bd0pEoDu5afsV9a894wVWiyPk4vBa6PjkJJ2om7H9JCVtpwO5%2B0QWiuQzvoXN3IKdiHeaA%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _m_h5_tk=3368371eacfccc8f82862a86dd7b8dfd_1582826745984; _m_h5_tk_enc=ce0978d905508de861ab72e478d76a9a; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=UtASsssmfaCONGki4KTH3w%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTUOLr0PocV7g%3D%3D&cart_m=0&tag=10&lng=zh_CN; mt=ci=-1_0; isg=BD09yBmkPwUVjZtnjAo1pyidTJk32nEskr7nYP-CeRTDNl1oxyqB_Atk5GpwrYnk; l=dBg7ckIgQhWWcsvkBOCanurza77OSIRYYuPzaNbMi_5BA6T6xJ7OoRsl8F96VjWfT2LB4Tn8Nrv9-etuZ7DmndK-g3fPaxDc.; JSESSIONID=37DFFF827495F13075CA01C510DE2A11'
        }
    elif 'zhihu' == site_brand:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'
        }
    elif 'amazon' == site_brand:
        headers = {
            'authority': 'www.amazon.com',
            'cache-control': 'max-age=0',
            'rtt': '100',
            'downlink': '3.25',
            'ect': '4g',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            # 'referer': 'https://www.amazon.com/s?k=spy+camera&crid=5DFMN9HZSKYG&sprefix=spy%2Caps%2C355&ref=nb_sb_ss_ts-doa-p_3_3',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'session-id=147-1122365-4740253; session-id-time=2082787201l; i18n-prefs=USD; skin=noskin; ubid-main=135-6782372-6842461; lc-main=en_US; session-token=RbFJddhjZUa5vox+FlUJE/xOprFZTI8ujE1A0ij61C0R3f7//29BPgC+TmrFSSAxxO30Vn9d1998Ct+PY9PzcKC6Qnu3iFShNkxqG+ua0IUaqcZ83atQFfrzD0sOsMP3c8kXJjrSobpR7rjz4Y3RWk6WMeGXegcnVu307RJia5guC4DOoRSvieN9LdZMRgW0; csm-hit=tb:E30D4NJ2CCW63N2CV37P+s-7T3ZD5V0KA63JS40D8YH|1645690630489&t:1645690630489&adb:adblk_no',
            # 'cookie': 'session-id-time=2082787201l; i18n-prefs=USD; ubid-main=135-2420930-0181523; session-id=140-8709027-1314032; lc-main=en_US; skin=noskin; session-token=E6NldNmB/sIGfmw0O7scS2kqHoJXLCxoq5809aur7UvhMG6Zq7em9sAVdMiVNjnD49Nm+Rhp/lvK+1YUZrHTA/yG20BCIPkmAGtUesXwIxZmIrs4rFSHcsAO+I3CGSjNjQBkJTHRWjcorwjpHnTWb1rONdOXmj3PjJc7l674Anp84d0Lw2bN0AmQNBGYxoYD; csm-hit=adb:adblk_no&t:1645804010403&tb:YKK1BQN71BRRZP67HN34+s-0TDSSCR2S0CKMK27G06P|1645804010403'
        }
    elif 'ins' == site_brand:
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'cookie': 'mid=YbymrwALAAEzEsPPRlnStgdMPN2E; ig_did=0AA66AEE-F134-483A-B8F0-15C7039B1E7E; ig_nrcb=1; ig_lang=zh-hk; ds_user_id=207843075; sessionid=207843075%3AcelhbwceJgHL0q%3A18; csrftoken=guEVNaiBM3YkJ2dQcoIDJBcEv0Ij1cft; shbid="6728\054207843075\0541673712042:01f7a14522b2d7d03401e06629a0a5587f95e66c535f993aedf154a3290ce30abcbb8197"; shbts="1642176042\054207843075\0541673712042:01f7d9ae6c7d3ab5c109d657b1c3e16ac2de87f746745d13d5d5d6dd6c902c7737990838"; rur="PRN\054207843075\0541673714027:01f7297bb60e60433bc6c60034c3e0e57f27cf87ce1bb86e2ba7edd91154295376d40c74"',
        }
    else:
        pass
    return headers