"""
Robots协议：网站通过Robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取，但它仅仅是互联网中的一般约定。
"""


# 怎么查看一个网站的robots协议
# 网站服务器 门口挂了一个牌子，告诉爬虫，哪些东西可以抓取，哪些东西不可以抓取
# 域名/robots.txt
# www.taobao.com/robots.txt

"""
User-agent: Baiduspider   用户代理   Baiduspider 百度爬虫
Disallow: /

User-agent: baiduspider
Disallow: /
"""
# 体现所在

"""
斗鱼robots协议

User-agent: Baiduspider    # 百度爬虫
Disallow: /api/*
Disallow: /member*
Disallow: /admin/*
Disallow: /room/*
Disallow: /search/*
Disallow: /cms/*

User-agent: Bytespider   字节跳动爬虫
Disallow: /api/*
Disallow: /member*
Disallow: /admin/*
Disallow: /room/*
Disallow: /search/*
Disallow: /cms/*

User-agent: Sosospider    搜搜爬虫
Disallow: /api/*
Disallow: /member*
Disallow: /admin/*
Disallow: /room/*
Disallow: /search/*
Disallow: /cms/*

User-agent: Sogou          搜狗爬虫
Disallow: /api/*
Disallow: /member*
Disallow: /admin/*
Disallow: /room/*
Disallow: /search/*
Disallow: /cms/*

User-agent: YodaoBot
Disallow: /api/*
Disallow: /member*
Disallow: /admin/*
Disallow: /room/*
Disallow: /search/*
Disallow: /cms/*

User-agent: Googlebot
Disallow: /api/*
Disallow: /member*
Disallow: /admin/*
Disallow: /room/*
Disallow: /search/*
Disallow: /cms/*

User-agent: Bingbot
Disallow: /api/*
Disallow: /member*
Disallow: /admin/*
Disallow: /room/*
Disallow: /search/*
Disallow: /cms/*

User-agent: Slurp
Disallow: /api/*
Disallow: /member*
Disallow: /admin/*
Disallow: /room/*
Disallow: /search/*
Disallow: /cms/*

User-agent: MSNBot
Disallow: /api/*
Disallow: /member*
Disallow: /admin/*
Disallow: /room/*
Disallow: /search/*
Disallow: /cms/*

User-agent: 360Spider
Disallow: /api/*
Disallow: /member*
Disallow: /admin/*
Disallow: /room/*
Disallow: /search/*
Disallow: /cms/*

User-agent: YisouSpider
Disallow: /api/*
Disallow: /member*
Disallow: /admin/*
Disallow: /room/*
Disallow: /search/*
Disallow: /cms/*

User-agent: Chinasospider
Disallow: /api/*
Disallow: /member*
Disallow: /admin/*
Disallow: /room/*
Disallow: /search/*
Disallow: /cms/*

User-agent: *
Disallow: /
"""


"""
hao123 robots协议

User-agent: Baiduspider
Allow: /

User-agent: Baiduspider-image
Allow: /

User-agent: Baiduspider-video
Allow: /

User-agent: Baiduspider-news
Allow: /

User-agent: Googlebot
Allow: /

User-agent: MSNBot
Allow: /

User-agent: YoudaoBot
Allow: /

User-agent: Sogou web spider
Allow: /

User-agent: Sogou inst spider
Allow: /

User-agent: Sogou spider2
Allow: /

User-agent: Sogou blog
Allow: /

User-agent: Sogou News Spider
Allow: /

User-agent: Sogou Orion spider
Allow: /

User-agent: JikeSpider
Allow: /

User-agent: Sosospider
Allow: /

User-agent: *    所有爬虫
Disallow: /

了解
"""