
def origin_urls():
    url = {}
    url["1"] = "https://dtliving-pre.alicdn.com/live_hp/259ae09c-8fbc-4ccb-9c71-6b35bf8b4928_merge.m3u8?app_type=win&auth_key=1615360924-0-0-e91b024fc860281496aaf64ed6023610&cid=e5b012ef6c10389b49d0c369f0759688&token=4f355a3038792537a90424b3feddc603CTG9CbgW1Q0gMoj1b4wOOMf6911yAq-nsJ2rqV-QIQmzrP1XD-RmCWYBzMHPBu_M7nYaFRKrzRFMQ7dK4ctJ6Qib3of5TtJXK9Df5FzORzs=&token2=c108c5a384656a6c1ee212fe244699bbVxu0gmtGdA1n_1LKeioVSrVZZxDtLio7emdn27OOUDVfMgUlJbAGvMxe70G-TVBeQ_h2GhjGbVFxOuyeRlNbTvyZWY96MmDpVJpGyYb2gEA&version=5.3.6-Release.3896"
    url["2"] = ""
    url["3"] = ""
    url["4"] = ""
    url["5"] = ""
    url["6"] = ""
    url["a1"] = ""
    url["7-1"] = ""
    url["7-2"] = ""
    url["8"] = ""
    url["9"] = ""
    url["10"] = ""
    url["a2"] = ""
    url["11"] = ""
    url["12"] = ""
    url["a3"] = ""
    url["13"] = ""
    url["14"] = ""
    url["a4"] = ""
    url["15-1"] = ""
    url["15-2"] = ""
    url["16"] = ""
    url["a5"] = ""
    url["17"] = ""
    url["18"] = ""
    url["19-1"] = ""
    url["19-2"] = ""
    url["20"] = ""
    url["a6"] = ""
    url["21"] = ""
    url["22"] = ""
    url["23"] = ""
    url["24"] = ""
    url["25"] = ""
    url["26"] = ""
    url["27"] = ""
    url["a7"] = ""
    url["a8"] = ""
    url["29"] = ""
    url["30"] = ""
    url["a9"] = ""
    return url


def module():
    url = "https://dtliving-pre.alicdn.com/live_hp/66e15aa2-b972-4b6d-8ff6-7bf66228e195_merge.m3u8?app_type=mac&auth_key=1613788275-0-0-da9dea77749748ee2152f6eef864acf3&cid=e5b012ef6c10389b49d0c369f0759688&token=6cbe504a7f44bd0ceea1597e391cf098uq3CvoQbEcURzyijZWPj34gngP9FnjP7IsP0ml2O8yGZp-jNhrFzuncRJDm99plgE6XjRH2GvuL6CKX6_aRmtUJt7fXNjrBVsAy_bg6Gp9A=&token2=72dccd20be006fa0027abac2f5dc89edB358jo2IZy9H8ikjmV9c4b15nUcPKHCexl1env6oMF2mwgTcIZXPndMcAmwXux1UmP8y0J7C--3gS-9yIi7jPk2Eo7JvOwu9GRwRbzp_AJA&version=5.1.39"
    for key in url.split("&"):
        print(key)


def buildUrl(vidio_id, auth_key, cid, token, token2):
    return "https://dtliving-pre.alicdn.com/live_hp/%smerge.m3u8?app_type=mac&auth_key=%s&cid=%s&token=%s&token2=%s&version=5.1.39" % (vidio_id, auth_key, cid, token, token2)


def getParam(url):
    # for key in url.split("&"):
    #     print(key)

    live_hp = url.split("merge.m3u8")[0].split("Flive_hp%2F")[1]
    print(live_hp)

    auth_key = url.split("auth_key%3D")[1].split("%26cid")[0]
    print(auth_key)

    cid = url.split("cid%3D")[1].split("%3D%26token")[0]
    print(cid)

    token = url.split("token%3D")[1].split("%3D%26token2")[0]
    print(token)

    token2 = url.split("token2%3D")[1].split("%26version")[0]
    print(token2)

    return live_hp, auth_key, cid, token, token2


if __name__ == "__main__":
    module()

    # url = buildUrl(1, 2, 2, 2, 3, 2)
    # print(url)

    print()
    urls = origin_urls()
    for url in urls:
        if urls[url] != "":
            live_hp, auth_key, cid, token, token2 = getParam(url)

            print()
            download_url = buildUrl(live_hp, auth_key, cid, token, token2)
            print(download_url)